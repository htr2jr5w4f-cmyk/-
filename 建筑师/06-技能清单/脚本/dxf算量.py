#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
dxf算量.py —— 读取 DXF 图纸，按图层统计工程量。

统计内容（按图层）：
  - 线长：LINE / LWPOLYLINE / POLYLINE / ARC（另含 CIRCLE、ELLIPSE、SPLINE，单独列出）
  - 面积：闭合多段线（LWPOLYLINE / POLYLINE，含弧段）、CIRCLE、HATCH
  - 块插入数量：按块名分别计数（门、窗、灯具等）
  - 文字：TEXT / MTEXT 内容和位置（以及块属性 ATTRIB）
  - 尺寸标注：DIMENSION 的测量值
单位：读取 $INSUNITS，把图纸单位换算成 m、m²；可用 --单位 强制指定。

用法：
  python3 dxf算量.py 输入.dxf [输出.xlsx] [--图层 外墙 内墙 "A-WALL*"] [--单位 mm] [--展开块]

依赖：ezdxf、openpyxl（pip install ezdxf openpyxl）
"""

import argparse
import fnmatch
import math
import sys
from collections import defaultdict, Counter

try:
    import ezdxf
    from ezdxf import path as ezpath
except ImportError:  # 依赖缺失时给出中文提示
    sys.exit("缺少 ezdxf：请先运行 pip install ezdxf")

# ---------------------------------------------------------------------------
# 单位换算：$INSUNITS 代码 → 每个图纸单位等于多少米
# 参考 AutoCAD DXF 参考手册的 $INSUNITS 定义
# ---------------------------------------------------------------------------
INSUNITS_米 = {
    1: ("英寸 in", 0.0254),
    2: ("英尺 ft", 0.3048),
    3: ("英里 mi", 1609.344),
    4: ("毫米 mm", 0.001),
    5: ("厘米 cm", 0.01),
    6: ("米 m", 1.0),
    7: ("千米 km", 1000.0),
    8: ("微英寸", 0.0254e-6),
    9: ("密耳 mil", 0.0254e-3),
    10: ("码 yd", 0.9144),
    14: ("分米 dm", 0.1),
}
# 命令行 --单位 可选值
单位别名 = {"mm": 4, "cm": 5, "m": 6, "in": 1, "ft": 2, "dm": 14}

# 计入「线长」的实体类型（按任务要求）及额外类型（单独列出，避免混淆）
主线型 = {"LINE", "LWPOLYLINE", "POLYLINE", "ARC"}
附加线型 = {"CIRCLE", "ELLIPSE", "SPLINE"}


# ---------------------------------------------------------------------------
# 几何工具函数
# ---------------------------------------------------------------------------
def 凸度段长与弓形面积(p1, p2, bulge):
    """多段线一段的长度，以及弧段相对弦的带符号弓形面积。
    bulge = tan(圆心角/4)；bulge=0 为直线段。"""
    弦 = math.dist(p1, p2)
    if abs(bulge) < 1e-12 or 弦 == 0:
        return 弦, 0.0
    圆心角 = 4.0 * math.atan(abs(bulge))
    半径 = 弦 / (2.0 * math.sin(圆心角 / 2.0))
    弧长 = 半径 * 圆心角
    弓形 = 0.5 * 半径 * 半径 * (圆心角 - math.sin(圆心角))
    # bulge 为正表示逆时针弧，弧向外凸于「逆时针多边形」的左侧，面积按符号累加
    return 弧长, math.copysign(弓形, bulge)


def 多段线长度面积(点列, 闭合):
    """点列：[(x, y, bulge), ...]。返回 (长度, 面积或 None)。
    面积 = 鞋带公式 + 各弧段弓形面积（带符号），最后取绝对值。"""
    n = len(点列)
    if n < 2:
        return 0.0, None
    长度 = 0.0
    带符号面积 = 0.0
    段数 = n if 闭合 else n - 1
    for i in range(段数):
        x1, y1, b = 点列[i]
        x2, y2, _ = 点列[(i + 1) % n]
        段长, 弓形 = 凸度段长与弓形面积((x1, y1), (x2, y2), b)
        长度 += 段长
        带符号面积 += 0.5 * (x1 * y2 - x2 * y1) + 弓形
    return 长度, (abs(带符号面积) if 闭合 else None)


def 鞋带面积(顶点):
    """普通多边形面积（带符号）。"""
    s = 0.0
    n = len(顶点)
    for i in range(n):
        x1, y1 = 顶点[i][0], 顶点[i][1]
        x2, y2 = 顶点[(i + 1) % n][0], 顶点[(i + 1) % n][1]
        s += x1 * y2 - x2 * y1
    return 0.5 * s


def 点在多边形内(pt, 顶点):
    """射线法判断点是否在多边形内。"""
    x, y = pt
    内 = False
    n = len(顶点)
    for i in range(n):
        x1, y1 = 顶点[i][0], 顶点[i][1]
        x2, y2 = 顶点[(i + 1) % n][0], 顶点[(i + 1) % n][1]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if xi > x:
                内 = not 内
    return 内


def 填充面积(hatch):
    """HATCH 面积：把每条边界展平成多边形，按嵌套深度奇偶相加/相减
    （深度为偶数的边界为实体，奇数为孔洞，即 even-odd 规则）。"""
    多边形 = []
    for p in ezpath.from_hatch(hatch):
        # 展平弧、椭圆、样条边界，distance 越小越精确（单位：图纸单位）
        for 子路径 in p.sub_paths():
            pts = [(v.x, v.y) for v in 子路径.flattening(distance=0.01)]
            if len(pts) >= 3:
                if math.dist(pts[0], pts[-1]) < 1e-9:
                    pts = pts[:-1]
                多边形.append(pts)
    if not 多边形:
        return 0.0
    面积表 = [abs(鞋带面积(pg)) for pg in 多边形]
    总面积 = 0.0
    for i, pg in enumerate(多边形):
        # 取第一个顶点检测被其他边界包含的层数
        深度 = sum(
            1 for j, other in enumerate(多边形)
            if j != i and 面积表[j] > 面积表[i] and 点在多边形内(pg[0], other)
        )
        总面积 += 面积表[i] if 深度 % 2 == 0 else -面积表[i]
    return abs(总面积)


def 实体长度(e):
    """返回实体的线长（图纸单位），不能计算时返回 None。"""
    t = e.dxftype()
    if t == "LINE":
        return math.dist(e.dxf.start, e.dxf.end)
    if t == "ARC":
        # 圆心角按逆时针从起始角到终止角
        角 = (e.dxf.end_angle - e.dxf.start_angle) % 360.0
        if 角 == 0:
            角 = 360.0
        return e.dxf.radius * math.radians(角)
    if t == "CIRCLE":
        return 2 * math.pi * e.dxf.radius
    if t == "LWPOLYLINE":
        点列 = [(x, y, b) for x, y, _s, _e, b in e.get_points("xyseb")]
        return 多段线长度面积(点列, e.closed)[0]
    if t == "POLYLINE":
        if e.is_2d_polyline:
            点列 = [(v.dxf.location.x, v.dxf.location.y, v.dxf.get("bulge", 0.0)) for v in e.vertices]
            return 多段线长度面积(点列, e.is_closed)[0]
        if e.is_3d_polyline:
            pts = [v.dxf.location for v in e.vertices]
            if e.is_closed and pts:
                pts = pts + [pts[0]]
            return sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
        return None  # 多面网格等不计长度
    if t in ("ELLIPSE", "SPLINE"):
        try:
            pts = list(ezpath.make_path(e).flattening(distance=0.01))
            return sum(math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1))
        except Exception:
            return None
    return None


def 实体闭合面积(e):
    """闭合多段线、圆的面积（图纸单位²）；不是闭合图形返回 None。"""
    t = e.dxftype()
    if t == "LWPOLYLINE" and e.closed:
        点列 = [(x, y, b) for x, y, _s, _e, b in e.get_points("xyseb")]
        return 多段线长度面积(点列, True)[1]
    if t == "POLYLINE" and e.is_2d_polyline and e.is_closed:
        点列 = [(v.dxf.location.x, v.dxf.location.y, v.dxf.get("bulge", 0.0)) for v in e.vertices]
        return 多段线长度面积(点列, True)[1]
    if t == "CIRCLE":
        return math.pi * e.dxf.radius ** 2
    return None


# ---------------------------------------------------------------------------
# 统计主体
# ---------------------------------------------------------------------------
class 图层统计:
    def __init__(self):
        self.线长 = 0.0          # 主线型（LINE/LWPOLYLINE/POLYLINE/ARC）
        self.线数 = 0
        self.附加线长 = 0.0      # CIRCLE/ELLIPSE/SPLINE
        self.附加线数 = 0
        self.闭合面积 = 0.0      # 闭合多段线 + 圆
        self.闭合数 = 0
        self.填充面积 = 0.0
        self.填充数 = 0
        self.块 = Counter()
        self.文字 = []           # (类型, 内容, x, y)
        self.尺寸 = []           # (类型, 测量值, 显示文字)
        self.类型计数 = Counter()


def 块名(insert):
    """尽量取动态块的真实名字（匿名块 *U 会显示原名）。"""
    名 = insert.dxf.name
    try:
        if 名.startswith("*") and hasattr(insert, "block"):
            blk = insert.block()
            # ezdxf：匿名动态块的 BLOCK_RECORD 可通过 xdata 关联到原块，这里只做安全尝试
            if blk is not None and blk.block_record is not None:
                名 = blk.block_record.dxf.get("name", 名)
    except Exception:
        pass
    return 名


def 尺寸类型(dim):
    """DIMENSION 的子类型（dimtype 的低 3 位）。"""
    码 = dim.dimtype & 0x07 if hasattr(dim, "dimtype") else dim.dxf.dimtype & 0x07
    return {0: "线性/旋转", 1: "对齐", 2: "角度", 3: "直径", 4: "半径", 5: "三点角度", 6: "坐标"}.get(码, str(码))


def 统计(doc, 图层过滤=None, 展开块=False):
    msp = doc.modelspace()
    结果 = defaultdict(图层统计)
    闭合明细 = []  # (图层, 类型, handle, 面积, 周长)

    def 匹配(layer):
        if not 图层过滤:
            return True
        return any(fnmatch.fnmatchcase(layer.lower(), pat.lower()) for pat in 图层过滤)

    def 处理(e, 继承图层=None, 深度=0):
        layer = e.dxf.get("layer", "0")
        # 块内 0 层实体继承插入点所在图层（AutoCAD 规则）
        if 继承图层 and layer == "0":
            layer = 继承图层
        t = e.dxftype()

        if t == "INSERT":
            if 匹配(layer):
                # MINSERT（阵列插入）按行×列计数
                数量 = max(1, e.dxf.get("row_count", 1)) * max(1, e.dxf.get("column_count", 1))
                结果[layer].块[块名(e)] += 数量
                结果[layer].类型计数[t] += 1
                # 块属性（ATTRIB），常用于门窗编号
                for att in e.attribs:
                    结果[layer].文字.append(("ATTRIB:" + att.dxf.tag, att.dxf.text,
                                           att.dxf.insert.x, att.dxf.insert.y))
            if 展开块 and 深度 < 10:
                try:
                    for ve in e.virtual_entities():
                        处理(ve, 继承图层=layer, 深度=深度 + 1)
                except Exception as ex:
                    print(f"  警告：块 {e.dxf.name} 展开失败：{ex}", file=sys.stderr)
            return

        if not 匹配(layer):
            return
        s = 结果[layer]
        s.类型计数[t] += 1

        if t in 主线型 or t in 附加线型:
            L = 实体长度(e)
            if L is not None:
                if t in 主线型:
                    s.线长 += L
                    s.线数 += 1
                else:
                    s.附加线长 += L
                    s.附加线数 += 1
            A = 实体闭合面积(e)
            if A is not None:
                s.闭合面积 += A
                s.闭合数 += 1
                闭合明细.append((layer, t, e.dxf.handle, A, L or 0.0))
        elif t == "HATCH":
            try:
                A = 填充面积(e)
            except Exception as ex:
                print(f"  警告：HATCH {e.dxf.handle} 面积计算失败：{ex}", file=sys.stderr)
                A = 0.0
            s.填充面积 += A
            s.填充数 += 1
            闭合明细.append((layer, t, e.dxf.handle, A, 0.0))
        elif t == "TEXT":
            p = e.dxf.insert
            s.文字.append(("TEXT", e.dxf.text, p.x, p.y))
        elif t == "MTEXT":
            p = e.dxf.insert
            s.文字.append(("MTEXT", e.plain_text(), p.x, p.y))
        elif t == "DIMENSION":
            try:
                值 = e.get_measurement()
                # 角度标注返回 Vec3 以外的数值（度）；坐标标注返回 Vec3
                if hasattr(值, "x"):
                    值 = None
            except Exception:
                值 = None
            显示 = e.dxf.get("text", "")  # "<>" 或空表示显示实测值，否则为手动改写
            s.尺寸.append((尺寸类型(e), 值, 显示))

    for e in msp:
        处理(e)
    return 结果, 闭合明细


def 确定单位(doc, 强制=None):
    """返回 (单位说明, 每单位米数, 提示)。"""
    if 强制:
        码 = 单位别名[强制]
        名, 系数 = INSUNITS_米[码]
        return f"{名}（命令行指定）", 系数, ""
    码 = doc.header.get("$INSUNITS", 0)
    if 码 in INSUNITS_米:
        名, 系数 = INSUNITS_米[码]
        return f"{名}（$INSUNITS={码}）", 系数, ""
    # 0 = 无单位：澳洲建筑图纸绝大多数用 mm，按 mm 处理并提示
    return f"未定义（$INSUNITS={码}），按毫米处理", 0.001, "⚠ 图纸没有定义单位，已按 mm 假设；请用一条已知尺寸核对，必要时加 --单位"


# ---------------------------------------------------------------------------
# 输出
# ---------------------------------------------------------------------------
def 写xlsx(路径, 文件名, 单位说明, k, 结果, 闭合明细, 图层过滤, 提示):
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill, Alignment
    except ImportError:
        print("缺少 openpyxl，跳过 xlsx 输出：pip install openpyxl", file=sys.stderr)
        return
    wb = Workbook()
    粗 = Font(bold=True)
    底色 = PatternFill("solid", fgColor="DDEBF7")

    def 表头(ws, cols, 宽=None):
        ws.append(cols)
        for c in ws[ws.max_row]:
            c.font = 粗
            c.fill = 底色
            c.alignment = Alignment(wrap_text=True, vertical="center")
        ws.freeze_panes = f"A{ws.max_row + 1}"  # 用地址字符串，避免 ws.cell() 提前创建空行
        if 宽:
            for i, w in enumerate(宽):
                ws.column_dimensions[chr(65 + i)].width = w

    # 1. 按图层汇总（每个图层一行）
    ws = wb.active
    ws.title = "按图层汇总"
    表头(ws, ["图层", "线长 m（LINE/LWPOLYLINE/POLYLINE/ARC）", "线段数", "圆/椭圆/样条长 m", "其数量",
             "闭合多段线+圆 面积 m²", "闭合图形数", "填充 HATCH 面积 m²", "填充数",
             "块插入总数", "块明细（块名×数量）", "文字数", "尺寸标注数", "尺寸测量值 m（逐个）", "实体类型计数"],
        [16, 14, 8, 12, 8, 14, 9, 14, 8, 9, 34, 8, 9, 30, 40])
    for layer in sorted(结果):
        s = 结果[layer]
        尺寸值 = ", ".join(
            (f"{v * k:.3f}" if typ not in ("角度", "三点角度") else f"{v:.2f}°") if v is not None else "?"
            for typ, v, _ in s.尺寸)
        ws.append([layer, round(s.线长 * k, 3), s.线数, round(s.附加线长 * k, 3), s.附加线数,
                   round(s.闭合面积 * k * k, 3), s.闭合数, round(s.填充面积 * k * k, 3), s.填充数,
                   sum(s.块.values()), "; ".join(f"{n}×{c}" for n, c in sorted(s.块.items())),
                   len(s.文字), len(s.尺寸), 尺寸值,
                   ", ".join(f"{t}:{c}" for t, c in sorted(s.类型计数.items()))])
    # 合计行
    ws.append(["合计",
               round(sum(s.线长 for s in 结果.values()) * k, 3), sum(s.线数 for s in 结果.values()),
               round(sum(s.附加线长 for s in 结果.values()) * k, 3), sum(s.附加线数 for s in 结果.values()),
               round(sum(s.闭合面积 for s in 结果.values()) * k * k, 3), sum(s.闭合数 for s in 结果.values()),
               round(sum(s.填充面积 for s in 结果.values()) * k * k, 3), sum(s.填充数 for s in 结果.values()),
               sum(sum(s.块.values()) for s in 结果.values())])
    for c in ws[ws.max_row]:
        c.font = 粗

    # 2. 块统计
    ws = wb.create_sheet("块统计")
    表头(ws, ["图层", "块名", "数量"], [16, 30, 8])
    for layer in sorted(结果):
        for n, c in sorted(结果[layer].块.items()):
            ws.append([layer, n, c])

    # 3. 文字
    ws = wb.create_sheet("文字")
    表头(ws, ["图层", "类型", "内容", "X（图纸单位）", "Y（图纸单位）", "X m", "Y m"], [16, 14, 40, 12, 12, 10, 10])
    for layer in sorted(结果):
        for typ, txt, x, y in 结果[layer].文字:
            ws.append([layer, typ, txt, round(x, 3), round(y, 3), round(x * k, 3), round(y * k, 3)])

    # 4. 尺寸
    ws = wb.create_sheet("尺寸标注")
    表头(ws, ["图层", "类型", "测量值（图纸单位/度）", "测量值 m", "图上文字（<> 或空=实测值）"], [16, 12, 16, 12, 24])
    for layer in sorted(结果):
        for typ, v, txt in 结果[layer].尺寸:
            是角度 = typ in ("角度", "三点角度")
            ws.append([layer, typ, None if v is None else round(v, 4),
                       None if (v is None or 是角度) else round(v * k, 4), txt])

    # 5. 闭合图形明细（方便逐个房间核对）
    ws = wb.create_sheet("闭合图形明细")
    表头(ws, ["图层", "类型", "句柄 handle", "面积 m²", "周长 m"], [16, 12, 12, 12, 12])
    for layer, t, h, A, L in 闭合明细:
        ws.append([layer, t, h, round(A * k * k, 4), round(L * k, 4)])

    # 6. 说明
    ws = wb.create_sheet("说明")
    for row in [
        ["源文件", 文件名], ["图纸单位", 单位说明], ["换算系数（米/单位）", k],
        ["图层过滤", ", ".join(图层过滤) if 图层过滤 else "（全部图层）"],
        ["提示", 提示 or "—"],
        ["口径", "只统计模型空间（model space）。块内几何默认不计入线长/面积（加 --展开块 才计入）。"],
        ["口径", "闭合多段线的周长也计入线长；墙体若画双线，线长是两条线之和，不等于墙长。"],
        ["口径", "尺寸测量值是图元几何实测值；图上文字被手动改写时以「尺寸标注」表的文字列为准并核对。"],
        ["衔接", "按图层汇总的长度/面积可填入 05-工具与模板/工程量计算表.xlsx 的黄色参数格（如 R10 墙长、R3 slab 面积）。"],
    ]:
        ws.append(row)
    ws.column_dimensions["A"].width = 20
    ws.column_dimensions["B"].width = 100
    wb.save(路径)


def 打印摘要(文件名, 单位说明, k, 结果, 提示):
    print(f"文件：{文件名}")
    print(f"图纸单位：{单位说明}（1 单位 = {k} m）")
    if 提示:
        print(提示)
    print("-" * 78)
    print(f"{'图层':<16}{'线长m':>10}{'闭合面积m²':>12}{'填充面积m²':>12}{'块数':>6}{'文字':>6}{'尺寸':>6}")
    for layer in sorted(结果):
        s = 结果[layer]
        print(f"{layer:<16}{s.线长 * k:>10.3f}{s.闭合面积 * k * k:>12.3f}{s.填充面积 * k * k:>12.3f}"
              f"{sum(s.块.values()):>6}{len(s.文字):>6}{len(s.尺寸):>6}")
    print("-" * 78)
    for layer in sorted(结果):
        s = 结果[layer]
        if s.附加线数:
            print(f"[{layer}] 圆/椭圆/样条 {s.附加线数} 个，长 {s.附加线长 * k:.3f} m（未计入上表线长）")
        if s.块:
            print(f"[{layer}] 块：" + "，".join(f"{n} × {c}" for n, c in sorted(s.块.items())))
        for typ, v, txt in s.尺寸:
            if v is None:
                print(f"[{layer}] 尺寸（{typ}）：无法读取测量值，图上文字「{txt}」")
            elif typ in ("角度", "三点角度"):
                print(f"[{layer}] 尺寸（{typ}）：{v:.2f}°")
            else:
                改写 = f"，图上文字被改写为「{txt}」" if txt not in ("", "<>") else ""
                print(f"[{layer}] 尺寸（{typ}）：{v * k:.3f} m{改写}")
        for typ, txt, x, y in s.文字:
            print(f"[{layer}] 文字（{typ}）「{txt}」 @ ({x * k:.2f}, {y * k:.2f}) m")


def main(argv=None):
    ap = argparse.ArgumentParser(description="DXF 按图层算量：线长、面积、块数量、文字、尺寸标注 → xlsx")
    ap.add_argument("输入", help="DXF 文件路径（DWG 请先转换为 DXF）")
    ap.add_argument("输出", nargs="?", help="输出 xlsx 路径（省略则只打印摘要）")
    ap.add_argument("--图层", nargs="+", metavar="图层名", help="只统计这些图层，可用通配符，如 \"A-WALL*\"（不区分大小写）")
    ap.add_argument("--单位", choices=sorted(单位别名), help="强制指定图纸单位，覆盖 $INSUNITS")
    ap.add_argument("--展开块", action="store_true", help="把块内的线、面积也计入（块内 0 层继承插入图层）")
    args = ap.parse_args(argv)

    try:
        doc = ezdxf.readfile(args.输入)
    except IOError:
        sys.exit(f"打不开文件：{args.输入}")
    except ezdxf.DXFStructureError:
        # 结构损坏时尝试恢复模式
        from ezdxf import recover
        doc, auditor = recover.readfile(args.输入)
        print(f"⚠ 文件结构有误，已用恢复模式读取（{len(auditor.errors)} 个错误）", file=sys.stderr)

    单位说明, k, 提示 = 确定单位(doc, args.单位)
    结果, 闭合明细 = 统计(doc, args.图层, args.展开块)
    if not 结果:
        print("没有找到符合条件的实体（检查图层名或图层过滤）。")
    打印摘要(args.输入, 单位说明, k, 结果, 提示)
    if args.输出:
        写xlsx(args.输出, args.输入, 单位说明, k, 结果, 闭合明细, args.图层, 提示)
        print(f"已写出：{args.输出}")
    return 结果, k


if __name__ == "__main__":
    main()
