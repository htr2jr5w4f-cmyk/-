#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
pdf图纸量尺.py —— 在矢量 PDF 图纸上量长度、面积，提取文字及位置，渲染 PNG。

子命令：
  信息   列出每页尺寸（mm）、对应纸张、矢量路径数、文字数、是否像扫描件
  渲染   把某页渲染成 PNG（可只渲染一个区域），方便人工看图和找坐标
  文字   列出页面文字及位置（可按关键字筛选），找房间名、尺寸标注
  量尺   按比例或两点校准，统计指定区域内线段总长、闭合路径面积，并列出区域内文字

坐标约定：
  默认用 PDF 点（pt，1 pt = 1/72 英寸），原点在页面左上角，x 向右、y 向下（与 PyMuPDF 一致）。
  加 --像素dpi N 表示你给的坐标是「本工具按 N dpi 渲染出的 PNG 上的像素坐标」，便于直接在图片上量取。

比例设定（量尺时二选一）：
  --比例 1:100 [--纸张 A1]   图纸标注的比例；若 PDF 不是按原纸张大小输出（如 A1 图存成 A3），
                             用 --纸张 写原图纸张（A0–A4 或 宽x高 mm），工具自动按页面尺寸换算
  --校准 x1,y1,x2,y2,已知长度m  在图上取两点（例如一条已知 20 m 的尺寸线两端），反算比例

例子：
  python3 pdf图纸量尺.py 信息 图纸.pdf
  python3 pdf图纸量尺.py 渲染 图纸.pdf --页 1 --dpi 150 -o 第1页.png
  python3 pdf图纸量尺.py 文字 图纸.pdf --页 1 --关键字 BED 卧室
  python3 pdf图纸量尺.py 量尺 图纸.pdf --页 1 --比例 1:100 --区域 140,140,720,440 --输出 结果.xlsx

依赖：pymupdf（pip install pymupdf）；xlsx 输出需 openpyxl；渲染也可用 poppler 的 pdftoppm。
"""

import argparse
import json
import math
import re
import shutil
import subprocess
import sys
from collections import defaultdict

try:
    import pymupdf
except ImportError:
    try:
        import fitz as pymupdf  # 旧版 PyMuPDF 的导入名
    except ImportError:
        sys.exit("缺少 PyMuPDF：请先运行 pip install pymupdf")

PT_MM = 25.4 / 72.0  # 1 pt 等于多少 mm

# ISO A 系列纸张（mm，竖向 宽×高）
纸张表 = {"A0": (841, 1189), "A1": (594, 841), "A2": (420, 594), "A3": (297, 420), "A4": (210, 297)}


# ---------------------------------------------------------------------------
# 基础工具
# ---------------------------------------------------------------------------
def 解析数列(s, 个数=None, 名="参数"):
    try:
        v = [float(x) for x in re.split(r"[,，\s]+", s.strip()) if x]
    except ValueError:
        sys.exit(f"{名} 格式错误：{s}")
    if 个数 and len(v) != 个数:
        sys.exit(f"{名} 需要 {个数} 个数字，用逗号分隔：{s}")
    return v


def 解析纸张(s):
    """返回 (短边 mm, 长边 mm)。"""
    s = s.strip().upper()
    if s in 纸张表:
        return tuple(sorted(纸张表[s]))
    m = re.match(r"^(\d+(?:\.\d+)?)\s*[X×*]\s*(\d+(?:\.\d+)?)$", s)
    if not m:
        sys.exit(f"纸张格式错误：{s}（用 A0–A4 或 594x841）")
    return tuple(sorted((float(m.group(1)), float(m.group(2)))))


def 识别纸张(w_mm, h_mm):
    短, 长 = sorted((w_mm, h_mm))
    for 名, (a, b) in 纸张表.items():
        if abs(短 - a) < 3 and abs(长 - b) < 3:
            return 名 + ("横向" if w_mm > h_mm else "竖向")
    return "非标准"


def 取页(doc, 页号):
    if not 1 <= 页号 <= doc.page_count:
        sys.exit(f"页号超出范围：共 {doc.page_count} 页")
    return doc[页号 - 1]


def 坐标转pt(vals, 像素dpi):
    """把用户给的坐标换成 PDF pt（像素坐标按 dpi 换算）。"""
    if 像素dpi:
        return [v * 72.0 / 像素dpi for v in vals]
    return vals


def 贝塞尔长度(p0, p1, p2, p3, 段=64):
    """三次贝塞尔曲线长度（折线逼近）。"""
    pts = [贝塞尔点(p0, p1, p2, p3, i / 段) for i in range(段 + 1)]
    return sum(math.dist(pts[i], pts[i + 1]) for i in range(段)), pts


def 贝塞尔点(p0, p1, p2, p3, t):
    u = 1 - t
    return (u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
            u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1])


def 鞋带面积(pts):
    s = 0.0
    for i in range(len(pts)):
        x1, y1 = pts[i]
        x2, y2 = pts[(i + 1) % len(pts)]
        s += x1 * y2 - x2 * y1
    return abs(s) / 2.0


# ---------------------------------------------------------------------------
# 矢量提取：把 get_drawings() 的每条路径拆成「段」和「闭合多边形」
# 坐标统一转换到「显示坐标」（考虑页面旋转，与渲染出的 PNG 一致）
# ---------------------------------------------------------------------------
def 提取矢量(page):
    m = page.rotation_matrix  # 未旋转坐标 → 显示坐标
    def T(p):
        q = pymupdf.Point(p) * m
        return (q.x, q.y)

    路径表 = []
    for d in page.get_drawings():
        段列 = []      # 每段：(长度pt, 点列)
        环 = []        # 当前子路径的折线点
        多边形 = []    # 闭合子路径的点列
        def 收环():
            nonlocal 环
            if len(环) >= 3 and d.get("closePath"):
                多边形.append(环)
            elif len(环) >= 4 and math.dist(环[0], 环[-1]) < 0.01:
                多边形.append(环[:-1])
            环 = []
        for it in d["items"]:
            op = it[0]
            if op == "l":
                a, b = T(it[1]), T(it[2])
                if 环 and math.dist(环[-1], a) > 0.01:
                    收环()
                if not 环:
                    环.append(a)
                环.append(b)
                段列.append((math.dist(a, b), [a, b]))
            elif op == "c":
                p = [T(x) for x in it[1:5]]
                if 环 and math.dist(环[-1], p[0]) > 0.01:
                    收环()
                L, pts = 贝塞尔长度(*p)
                if not 环:
                    环.append(pts[0])
                环.extend(pts[1:])
                段列.append((L, pts))
            elif op == "re":
                收环()
                r = it[1]
                q = [T(r.tl), T(r.tr), T(r.br), T(r.bl)]
                for i in range(4):
                    段列.append((math.dist(q[i], q[(i + 1) % 4]), [q[i], q[(i + 1) % 4]]))
                多边形.append(q)
            elif op == "qu":
                收环()
                qd = it[1]
                q = [T(qd.ul), T(qd.ur), T(qd.lr), T(qd.ll)]
                for i in range(4):
                    段列.append((math.dist(q[i], q[(i + 1) % 4]), [q[i], q[(i + 1) % 4]]))
                多边形.append(q)
        # closePath 时补上收尾段的长度
        if d.get("closePath") and len(环) >= 3 and math.dist(环[0], 环[-1]) > 0.01:
            段列.append((math.dist(环[-1], 环[0]), [环[-1], 环[0]]))
        收环()
        路径表.append({
            "类型": d.get("type", ""),            # 's' 描边，'f' 填充，'fs' 两者
            "颜色": d.get("color"),
            "填充色": d.get("fill"),
            "线宽": d.get("width") or 0.0,
            "图层": d.get("layer") or "",          # PDF 可选内容组（OCG），CAD 导出的 PDF 常保留图层名
            "段": 段列,
            "多边形": 多边形,
        })
    return 路径表


def 颜色文字(c):
    if not c:
        return "无"
    return "#" + "".join(f"{int(round(v * 255)):02X}" for v in c[:3])


def 点在区域(p, 区):
    return 区 is None or (区[0] - 0.01 <= p[0] <= 区[2] + 0.01 and 区[1] - 0.01 <= p[1] <= 区[3] + 0.01)


def 提取文字(page):
    """按「行」提取文字，坐标转换到显示坐标。"""
    m = page.rotation_matrix
    行表 = []
    for b in page.get_text("dict")["blocks"]:
        for ln in b.get("lines", []):
            txt = "".join(sp["text"] for sp in ln["spans"]).strip()
            if not txt:
                continue
            r = pymupdf.Rect(ln["bbox"]) * m
            size = max(sp["size"] for sp in ln["spans"])
            行表.append({"文字": txt, "x0": r.x0, "y0": r.y0, "x1": r.x1, "y1": r.y1, "字号": size})
    return 行表


# ---------------------------------------------------------------------------
# 子命令：信息
# ---------------------------------------------------------------------------
def 命令_信息(a):
    doc = pymupdf.open(a.pdf)
    print(f"文件：{a.pdf}，共 {doc.page_count} 页")
    for i, page in enumerate(doc, 1):
        w, h = page.rect.width * PT_MM, page.rect.height * PT_MM
        n路径 = len(page.get_drawings())
        n字 = len(page.get_text("words"))
        n图 = len(page.get_images())
        提示 = ""
        if n路径 < 5 and n字 == 0 and n图 > 0:
            提示 = "  ⚠ 只有图片没有矢量和文字，像扫描件：不能量矢量，只能渲染后人工看，或按比例在图片上手量"
        print(f"第 {i} 页：{w:.1f} × {h:.1f} mm（{识别纸张(w, h)}），旋转 {page.rotation}°，"
              f"矢量路径 {n路径}，文字词 {n字}，图片 {n图}{提示}")
    ocg = doc.get_ocgs() if hasattr(doc, "get_ocgs") else {}
    if ocg:
        print("PDF 图层（OCG）：" + "，".join(sorted({v["name"] for v in ocg.values()})))


# ---------------------------------------------------------------------------
# 子命令：渲染
# ---------------------------------------------------------------------------
def 命令_渲染(a):
    输出 = a.o or f"第{a.页}页.png"
    if a.引擎 == "pdftoppm":
        if not shutil.which("pdftoppm"):
            sys.exit("找不到 pdftoppm（poppler-utils），改用 --引擎 pymupdf")
        前缀 = 输出[:-4] if 输出.lower().endswith(".png") else 输出
        cmd = ["pdftoppm", "-png", "-r", str(a.dpi), "-f", str(a.页), "-l", str(a.页), "-singlefile", a.pdf, 前缀]
        subprocess.run(cmd, check=True)
        print(f"已用 pdftoppm 渲染：{前缀}.png（{a.dpi} dpi）")
        return
    doc = pymupdf.open(a.pdf)
    page = 取页(doc, a.页)
    clip = None
    if a.区域:
        x0, y0, x1, y1 = 坐标转pt(解析数列(a.区域, 4, "--区域"), a.像素dpi)
        # 用户给的是显示坐标，渲染裁剪要换回未旋转坐标
        clip = pymupdf.Rect(x0, y0, x1, y1) * page.derotation_matrix
    pix = page.get_pixmap(dpi=a.dpi, clip=clip)
    pix.save(输出)
    print(f"已渲染：{输出}（{pix.width} × {pix.height} 像素，{a.dpi} dpi；"
          f"像素坐标 ÷ {a.dpi} × 72 = PDF pt{'，注意裁剪图的原点是区域左上角' if clip else ''}）")


# ---------------------------------------------------------------------------
# 子命令：文字
# ---------------------------------------------------------------------------
def 命令_文字(a):
    doc = pymupdf.open(a.pdf)
    page = 取页(doc, a.页)
    行表 = 提取文字(page)
    if a.关键字:
        行表 = [t for t in 行表 if any(k.lower() in t["文字"].lower() for k in a.关键字)]
    if a.区域:
        区 = 坐标转pt(解析数列(a.区域, 4, "--区域"), a.像素dpi)
        行表 = [t for t in 行表 if 点在区域(((t["x0"] + t["x1"]) / 2, (t["y0"] + t["y1"]) / 2), 区)]
    print(f"{'x(pt)':>8}{'y(pt)':>8}{'x(mm)':>8}{'y(mm)':>8}{'字号':>6}  文字")
    for t in 行表:
        print(f"{t['x0']:>8.1f}{t['y0']:>8.1f}{t['x0'] * PT_MM:>8.1f}{t['y0'] * PT_MM:>8.1f}{t['字号']:>6.1f}  {t['文字']}")
    print(f"共 {len(行表)} 行；可疑尺寸数字：" +
          "，".join(t["文字"] for t in 行表 if re.fullmatch(r"\d{3,6}", t["文字"]))[:500])


# ---------------------------------------------------------------------------
# 子命令：量尺
# ---------------------------------------------------------------------------
def 求比例(a, page):
    """返回 (每 pt 等于多少实际米, 说明)。"""
    if a.校准:
        x1, y1, x2, y2, 已知 = 解析数列(a.校准, 5, "--校准")
        x1, y1, x2, y2 = 坐标转pt([x1, y1, x2, y2], a.像素dpi)
        d = math.hypot(x2 - x1, y2 - y1)
        if d == 0:
            sys.exit("校准两点重合")
        k = 已知 / d
        等效 = k * 1000 / PT_MM  # 等效比例分母（按页面实际纸张）
        return k, f"两点校准：图上 {d:.2f} pt（{d * PT_MM:.2f} mm）= {已知} m，相当于本页 1:{等效:.1f}"
    if a.比例:
        m = re.match(r"^\s*1\s*[:：]\s*(\d+(?:\.\d+)?)\s*$", a.比例)
        if not m:
            sys.exit("--比例 格式应为 1:100")
        分母 = float(m.group(1))
        缩放 = 1.0
        说明 = f"比例 1:{分母:g}"
        if a.纸张:
            短, 长 = 解析纸张(a.纸张)
            页长 = max(page.rect.width, page.rect.height) * PT_MM
            页短 = min(page.rect.width, page.rect.height) * PT_MM
            # 原图纸与本 PDF 页面的尺寸比。打印/导出「适合页面」时保持长宽比，
            # 实际缩放取决于更受限的一边，所以取两边比值中较大者
            缩放 = max(长 / 页长, 短 / 页短)
            说明 += f"（原图 {a.纸张}，本页 {页长:.1f}×{页短:.1f} mm，放大系数 {缩放:.4f}）"
            if abs(长 / 页长 - 短 / 页短) / 缩放 > 0.02:
                说明 += " ⚠ 纸张长宽比与页面相差超过 2%，请用 --校准 核对"
        k = PT_MM * 缩放 * 分母 / 1000.0
        return k, 说明
    sys.exit("量尺需要 --比例 或 --校准 之一")


def 命令_量尺(a):
    doc = pymupdf.open(a.pdf)
    page = 取页(doc, a.页)
    k, 比例说明 = 求比例(a, page)
    区 = 坐标转pt(解析数列(a.区域, 4, "--区域"), a.像素dpi) if a.区域 else None
    if 区:
        区 = [min(区[0], 区[2]), min(区[1], 区[3]), max(区[0], 区[2]), max(区[1], 区[3])]

    路径表 = 提取矢量(page)
    分组 = defaultdict(lambda: {"长度": 0.0, "段数": 0, "面积": 0.0, "闭合数": 0})
    闭合明细 = []
    已计面积 = set()  # 去重：同一几何的「填充」和「描边」可能是两条路径
    for p in 路径表:
        if a.最小线宽 is not None and p["线宽"] < a.最小线宽:
            continue
        if a.颜色 and 颜色文字(p["颜色"]).upper() != a.颜色.upper():
            continue
        if a.图层 and p["图层"] not in a.图层:
            continue
        键 = (p["图层"] or "—") + " | 线色" + 颜色文字(p["颜色"]) + f" | 线宽{p['线宽']:.2f}"
        # 线长只计描边路径（纯填充没有线）
        if "s" in p["类型"]:
            for L, pts in p["段"]:
                if all(点在区域(q, 区) for q in pts):
                    分组[键]["长度"] += L
                    分组[键]["段数"] += 1
        for pg in p["多边形"]:
            if not all(点在区域(q, 区) for q in pg):
                continue
            A = 鞋带面积(pg)
            if A < 1e-6:
                continue
            xs, ys = [q[0] for q in pg], [q[1] for q in pg]
            指纹 = (round(min(xs), 1), round(min(ys), 1), round(max(xs), 1), round(max(ys), 1), round(A, 0))
            if 指纹 in 已计面积:
                continue
            已计面积.add(指纹)
            分组[键]["面积"] += A
            分组[键]["闭合数"] += 1
            闭合明细.append({"分组": 键, "面积m2": A * k * k, "x0": min(xs), "y0": min(ys),
                         "x1": max(xs), "y1": max(ys), "顶点数": len(pg)})

    文字 = [t for t in 提取文字(page) if 点在区域(((t["x0"] + t["x1"]) / 2, (t["y0"] + t["y1"]) / 2), 区)]

    # 终端摘要
    print(f"文件：{a.pdf} 第 {a.页} 页；{比例说明}；1 pt = {k:.6f} m")
    print(f"区域（pt）：{'整页' if not 区 else ', '.join(f'{v:.1f}' for v in 区)}（只计完全落在区域内的线段和闭合路径）")
    print("-" * 78)
    总长 = 总面积 = 0.0
    for 键 in sorted(分组):
        g = 分组[键]
        总长 += g["长度"]
        总面积 += g["面积"]
        print(f"{键:<40} 线长 {g['长度'] * k:>9.3f} m（{g['段数']} 段）  闭合面积 {g['面积'] * k * k:>9.3f} m²（{g['闭合数']} 个）")
    print("-" * 78)
    print(f"合计：线长 {总长 * k:.3f} m；闭合面积 {总面积 * k * k:.3f} m²（闭合面积可能含嵌套重复，逐个核对见明细）")
    for c in sorted(闭合明细, key=lambda c: -c["面积m2"])[:20]:
        print(f"  闭合：{c['面积m2']:.3f} m²  外包 ({c['x0']:.1f},{c['y0']:.1f})–({c['x1']:.1f},{c['y1']:.1f}) pt  {c['分组']}")
    print(f"区域内文字 {len(文字)} 行：")
    for t in 文字:
        print(f"  ({t['x0']:.1f}, {t['y0']:.1f}) pt  {t['文字']}")

    结果 = {"文件": a.pdf, "页": a.页, "比例说明": 比例说明, "每pt米": k, "区域pt": 区,
            "分组": {键: {"线长m": g["长度"] * k, "段数": g["段数"], "闭合面积m2": g["面积"] * k * k,
                        "闭合数": g["闭合数"]} for 键, g in 分组.items()},
            "合计线长m": 总长 * k, "合计闭合面积m2": 总面积 * k * k,
            "闭合明细": 闭合明细, "文字": 文字}
    if a.输出:
        if a.输出.lower().endswith(".json"):
            with open(a.输出, "w", encoding="utf-8") as f:
                json.dump(结果, f, ensure_ascii=False, indent=2)
        else:
            写xlsx(a.输出, 结果)
        print(f"已写出：{a.输出}")
    return 结果


def 写xlsx(路径, r):
    try:
        from openpyxl import Workbook
        from openpyxl.styles import Font
    except ImportError:
        sys.exit("缺少 openpyxl：pip install openpyxl，或把 --输出 改成 .json")
    wb = Workbook()
    ws = wb.active
    ws.title = "汇总"
    for row in [["文件", r["文件"]], ["页", r["页"]], ["比例", r["比例说明"]], ["每 pt 米", r["每pt米"]],
                ["区域 pt", str(r["区域pt"] or "整页")], []]:
        ws.append(row)
    ws.append(["分组（图层 | 线色 | 线宽）", "线长 m", "段数", "闭合面积 m²", "闭合数"])
    for c in ws[ws.max_row]:
        c.font = Font(bold=True)
    for 键, g in sorted(r["分组"].items()):
        ws.append([键, round(g["线长m"], 3), g["段数"], round(g["闭合面积m2"], 3), g["闭合数"]])
    ws.append(["合计", round(r["合计线长m"], 3), None, round(r["合计闭合面积m2"], 3)])
    ws.column_dimensions["A"].width = 44
    ws2 = wb.create_sheet("闭合路径")
    ws2.append(["分组", "面积 m²", "x0 pt", "y0 pt", "x1 pt", "y1 pt", "顶点数"])
    for c in r["闭合明细"]:
        ws2.append([c["分组"], round(c["面积m2"], 4), round(c["x0"], 1), round(c["y0"], 1),
                    round(c["x1"], 1), round(c["y1"], 1), c["顶点数"]])
    ws3 = wb.create_sheet("文字")
    ws3.append(["文字", "x0 pt", "y0 pt", "x1 pt", "y1 pt", "字号"])
    for t in r["文字"]:
        ws3.append([t["文字"], round(t["x0"], 1), round(t["y0"], 1), round(t["x1"], 1), round(t["y1"], 1), round(t["字号"], 1)])
    wb.save(路径)


# ---------------------------------------------------------------------------
def main(argv=None):
    ap = argparse.ArgumentParser(description="矢量 PDF 图纸量尺：长度、面积、文字位置、渲染 PNG")
    sub = ap.add_subparsers(dest="命令", required=True)

    def 公共(p, 页=True):
        p.add_argument("pdf", help="PDF 文件")
        if 页:
            p.add_argument("--页", type=int, default=1, help="页号，从 1 开始（默认 1）")

    p = sub.add_parser("信息", help="列出各页尺寸、矢量和文字数量")
    公共(p, 页=False)
    p.set_defaults(func=命令_信息)

    p = sub.add_parser("渲染", help="把某页渲染成 PNG")
    公共(p)
    p.add_argument("--dpi", type=int, default=150, help="分辨率（默认 150）")
    p.add_argument("-o", help="输出 PNG 路径")
    p.add_argument("--区域", help="只渲染区域 x0,y0,x1,y1（pt，或配合 --像素dpi 用像素）")
    p.add_argument("--像素dpi", type=float, help="--区域 用的是该 dpi 下的像素坐标")
    p.add_argument("--引擎", choices=["pymupdf", "pdftoppm"], default="pymupdf", help="渲染引擎（默认 pymupdf）")
    p.set_defaults(func=命令_渲染)

    p = sub.add_parser("文字", help="列出文字及位置")
    公共(p)
    p.add_argument("--关键字", nargs="+", help="只显示含这些关键字的行（不区分大小写）")
    p.add_argument("--区域", help="只看区域 x0,y0,x1,y1")
    p.add_argument("--像素dpi", type=float, help="坐标为该 dpi 下的像素")
    p.set_defaults(func=命令_文字)

    p = sub.add_parser("量尺", help="按比例统计区域内线长、闭合面积和文字")
    公共(p)
    p.add_argument("--比例", help="图纸比例，如 1:100")
    p.add_argument("--纸张", help="原图纸张（A0–A4 或 宽x高 mm），PDF 缩放输出时使用")
    p.add_argument("--校准", help="两点校准 x1,y1,x2,y2,已知长度m")
    p.add_argument("--区域", help="统计区域 x0,y0,x1,y1（默认整页）")
    p.add_argument("--像素dpi", type=float, help="--区域/--校准 的坐标为该 dpi 下的像素")
    p.add_argument("--最小线宽", type=float, help="忽略线宽小于该值（pt）的路径，用于排除填充图案、细线")
    p.add_argument("--颜色", help="只统计该线色，如 #0000FF")
    p.add_argument("--图层", nargs="+", help="只统计这些 PDF 图层（OCG 名）")
    p.add_argument("--输出", help="输出 .xlsx 或 .json")
    p.set_defaults(func=命令_量尺)

    a = ap.parse_args(argv)
    return a.func(a)


if __name__ == "__main__":
    main()
