#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
装修平面出图.py —— 按房间清单自动排出商业装修（办公为主）平面「概念草图」，输出 DXF + PDF，并做基本校核。

用途：给出一个可以拿来讨论的方案草图（条带式排布：中间或一侧走道，房间沿走道排开），
      不是施工图，也不是最终设计。正式设计须由合资格的设计人员完成，并经 landlord 和 certifier 审查。

用法：
  python3 装修平面出图.py 清单.json -o 输出目录/前缀
  python3 装修平面出图.py 清单.csv  -o 输出目录/前缀 --宽 20 --深 15
  常用参数：--走道宽 1.5  --最小走道宽 1.0  --门宽 0.92  --隔墙厚 0.1  --人均面积 10
           --布局 自动|双侧|单侧  --下侧进深 4.5  --第二出口  --余量并入 办公区  --标题 "..."  --备注 "..."  --严格

输入格式：
  JSON：{"标题": "...", "备注": "...", "租户区": {"宽": 20, "深": 15},
         "参数": {"走道宽": 1.5, ...},            # 可选，命令行参数优先
         "房间": [{"名称": "前台", "类型": "前台", "面积": 18},
                  {"名称": "会议室1", "类型": "会议室", "长": 5, "宽": 4}, ...]}
  CSV（UTF-8，首行表头）：名称,类型,面积,长,宽[,条带]   （面积与长宽二选一；英文表头 name,type,area,length,width,strip 也可）
       「条带」可选：双侧布局填 下侧 / 上侧，单侧布局填 单侧；不填按顺序自动放（先下侧后上侧）。
       可以有一行 类型=租户区 ，用 长、宽 给出租户区外轮廓（宽 = x 方向，深 = y 方向）；也可用 --宽 --深 给出。

输出（前缀为 P）：
  P.dxf        图层：外轮廓、隔墙、门、房间名、面积标注、疏散通道示意，另加 房间边界（每个房间一条闭合多段线，
               供 dxf算量.py 读回面积和周长）、尺寸、图签。单位 mm（$INSUNITS=4）。
  P.pdf        A3 横向，自动选比例（1:50/1:100/1:200…），PDF 图层（OCG）名与 DXF 图层同名，可用 pdf图纸量尺.py 量取。
  P_校核.json  排布结果和校核结论（也打印在终端）。

校核（数值依据见 01-法规标准/商业装修法规与审批.md，NCC 2022 Volume One，已读原文）：
  1. 房间总面积是否超出租户区（毛面积）以及扣除走道后的可用面积；
  2. 走道净宽（走道中心距减隔墙厚）≥ 最小走道宽（默认 1.0 m，NCC 2022 D2D8 疏散路线一般不小于 1 m；
     人数 100 人以上按 D2D8 公式加宽；人数按 Table D2D18 办公 10 m²/人估算，可用 --人均面积 改）；
  3. 每个房间至少有一扇门，且门开向走道；门宽 ≥ 0.75 m（D2D9 门洞净宽一般不小于 750 mm；
     本工具把「门宽」当作净宽检查，实际门扇规格以设计和五金表为准）。
  另给出提示（不判合格与否）：租户区内到租户入口门的最远行走距离（NCC D2D5 的疏散距离要算到楼宇的出口，
  须由 certifier 或消防顾问判断）、房间形状过窄、湿区位置须对 base building 给排水立管。
"""
import argparse
import csv
import json
import math
import os
import sys

import ezdxf
from ezdxf.enums import TextEntityAlignment

# ---------------------------------------------------------------------------
# 常量：已核实的 NCC 2022 数值（出处见 01-法规标准/商业装修法规与审批.md 第 3.2 节、第 2 节）
# ---------------------------------------------------------------------------
NCC_最小疏散宽度_m = 1.0        # D2D8：疏散路线净宽一般不小于 1 m
NCC_最小门洞净宽_m = 0.75       # D2D9：门洞净宽一般不小于 750 mm（通往卫生间或浴室的门除外）
NCC_办公人均面积_m2 = 10.0      # Table D2D18：办公 10 m²/人

已知类型 = ["前台", "办公区", "会议室", "经理室", "茶水间", "卫生间", "库房", "设备间", "打印区", "其他"]
湿区类型 = {"茶水间", "卫生间"}

# 图层名、颜色（AutoCAD 颜色号）、PDF 线色和线宽（pt）
图层表 = {
    "外轮廓":     (7, (0, 0, 0), 1.4),
    "隔墙":       (5, (0.0, 0.2, 0.8), 0.8),
    "门":         (3, (0.0, 0.55, 0.0), 0.5),
    "房间名":     (7, (0, 0, 0), 0),
    "面积标注":   (8, (0.35, 0.35, 0.35), 0),
    "疏散通道示意": (1, (0.85, 0.0, 0.0), 0.8),
    "房间边界":   (9, (0.75, 0.75, 0.75), 0.25),
    "尺寸":       (2, (0.4, 0.4, 0.4), 0.3),
    "图签":       (7, (0, 0, 0), 0.5),
}

声明 = "概念草图：仅供方案讨论，不是施工图。正式设计须由合资格的设计人员完成，并经 landlord 和 certifier 审查。"


# ---------------------------------------------------------------------------
# 读输入
# ---------------------------------------------------------------------------
def _数(v):
    """把单元格转成浮点数；空白返回 None。"""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return float(v)
    v = str(v).strip().replace("m²", "").replace("m2", "")
    return float(v) if v else None


def 读清单(路径):
    """返回 (配置 dict, 房间列表)。房间：{名称, 类型, 面积, 长, 宽}。"""
    配置 = {"参数": {}}
    房间 = []
    if 路径.lower().endswith(".json"):
        with open(路径, encoding="utf-8") as f:
            d = json.load(f)
        配置["标题"] = d.get("标题")
        配置["备注"] = d.get("备注")
        配置["参数"] = d.get("参数", {}) or {}
        区 = d.get("租户区") or {}
        配置["宽"] = _数(区.get("宽"))
        配置["深"] = _数(区.get("深"))
        for r in d.get("房间", []):
            房间.append({"名称": str(r.get("名称", "")).strip(), "类型": str(r.get("类型", "其他")).strip(),
                       "面积": _数(r.get("面积")), "长": _数(r.get("长")), "宽": _数(r.get("宽")),
                       "条带": (str(r.get("条带")).strip() or None) if r.get("条带") else None})
    else:
        别名 = {"name": "名称", "type": "类型", "area": "面积", "length": "长", "width": "宽",
              "strip": "条带", "房间名": "名称", "面积m2": "面积", "面积(m2)": "面积"}
        with open(路径, encoding="utf-8-sig", newline="") as f:
            for row in csv.DictReader(f):
                r = {别名.get(k.strip().lower(), 别名.get(k.strip(), k.strip())): v for k, v in row.items() if k}
                类型 = (r.get("类型") or "其他").strip()
                if 类型 == "租户区":
                    配置["宽"], 配置["深"] = _数(r.get("长")), _数(r.get("宽"))
                    continue
                房间.append({"名称": (r.get("名称") or "").strip(), "类型": 类型,
                           "面积": _数(r.get("面积")), "长": _数(r.get("长")), "宽": _数(r.get("宽")),
                           "条带": (r.get("条带") or "").strip() or None})
    for i, r in enumerate(房间, 1):
        if not r["名称"]:
            r["名称"] = f"房间{i}"
        if r["面积"] is None:
            if r["长"] and r["宽"]:
                r["面积"] = r["长"] * r["宽"]
            else:
                raise SystemExit(f"房间「{r['名称']}」既没有面积也没有长宽")
        if r["面积"] <= 0:
            raise SystemExit(f"房间「{r['名称']}」面积必须大于 0")
    return 配置, 房间


# ---------------------------------------------------------------------------
# 排布（条带式）
# 坐标：租户区左下角为原点，x 向右（宽 W），y 向上（深 D），单位 m。租户入口门在左墙（x=0）的走道端。
# 双侧：下条带 y∈[0,dA]，走道 y∈[dA,dA+c]，上条带 y∈[dA+c,D]。
# 单侧：房间条带 y∈[0,D−c]，走道 y∈[D−c,D]（沿上墙）。
# 房间按清单顺序（前台排第一，靠近入口）依次放入条带，宽度 = 面积 / 条带进深，取整到 10 mm。
# ---------------------------------------------------------------------------
def 取整(v, 步=0.01):
    return round(round(v / 步) * 步, 6)


def 排布(W, D, 房间, 走道宽, 布局="自动", 余量并入=None, 最小进深=3.0, 下侧进深=None):
    提示 = []
    if 布局 == "自动":
        布局 = "双侧" if (D - 走道宽) / 2 >= 最小进深 else "单侧"
        提示.append(f"布局自动选择：{布局}（双侧时每侧进深 {(D - 走道宽) / 2:.2f} m，阈值 {最小进深} m）")
    if 布局 == "双侧":
        dA = 取整(下侧进深) if 下侧进深 else 取整((D - 走道宽) / 2)
        if not (0 < dA < D - 走道宽):
            raise SystemExit(f"下侧进深 {dA} m 不合理（应在 0 与 {D - 走道宽:.2f} m 之间）")
        条带 = [{"名": "下侧", "y0": 0.0, "y1": dA, "门边": "上"},
              {"名": "上侧", "y0": dA + 走道宽, "y1": D, "门边": "下"}]
        走道 = (0.0, dA, W, dA + 走道宽)
    else:
        条带 = [{"名": "单侧", "y0": 0.0, "y1": D - 走道宽, "门边": "上"}]
        走道 = (0.0, D - 走道宽, W, D)
    for s in 条带:
        s["进深"] = s["y1"] - s["y0"]
        s["x"] = 0.0
        s["房间"] = []
    if any(s["进深"] <= 0 for s in 条带):
        raise SystemExit("走道宽大于租户区进深，无法排布")

    # 前台排第一（靠近入口）；其余按清单顺序
    顺序 = sorted(range(len(房间)), key=lambda i: (0 if 房间[i]["类型"] == "前台" else 1, i))
    已排, 未排 = [], []
    for i in 顺序:
        r = dict(房间[i])
        if r["类型"] not in 已知类型:
            提示.append(f"房间「{r['名称']}」类型「{r['类型']}」不在常用类型表内，按「其他」画")
        放下 = False
        指定 = r.get("条带")
        候选 = [s for s in 条带 if s["名"] == 指定] if 指定 else 条带
        if 指定 and not 候选:
            提示.append(f"房间「{r['名称']}」指定条带「{指定}」不存在（本布局条带：{'、'.join(s['名'] for s in 条带)}），改为自动")
            候选 = 条带
        for s in 候选:
            w = 取整(r["面积"] / s["进深"])
            if s["x"] + w <= W + 1e-6:
                r.update(x0=s["x"], x1=取整(s["x"] + w), y0=s["y0"], y1=s["y1"], 条带=s["名"], 门边=s["门边"])
                s["x"] = r["x1"]
                s["房间"].append(r)
                已排.append(r)
                放下 = True
                if r.get("长") and r.get("宽") and abs(min(r["长"], r["宽"]) - s["进深"]) > 0.3:
                    提示.append(f"房间「{r['名称']}」原定 {r['长']}×{r['宽']} m，按条带进深 {s['进深']:.2f} m 改成 "
                              f"{w:.2f}×{s['进深']:.2f} m（面积不变）")
                if w < 1.5:
                    提示.append(f"房间「{r['名称']}」开间只有 {w:.2f} m，形状过窄，须人工调整")
                break
        if not 放下:
            未排.append(r)

    # 条带末端的余量：并入指定类型的最后一个房间，或标为「余量（未分配）」
    余量 = []
    for s in 条带:
        剩 = W - s["x"]
        if 剩 <= 0.05:
            continue
        目标 = [r for r in s["房间"] if 余量并入 and r["类型"] == 余量并入]
        if 目标 and 目标[-1] is s["房间"][-1]:
            r = 目标[-1]
            r["x1"] = W
            提示.append(f"{s['名']}条带余量 {剩 * s['进深']:.2f} m² 并入「{r['名称']}」")
        else:
            余量.append({"名称": "余量（未分配）", "类型": "余量", "x0": s["x"], "x1": W,
                       "y0": s["y0"], "y1": s["y1"], "条带": s["名"], "门边": s["门边"]})
    for r in 已排:
        r["排布面积"] = (r["x1"] - r["x0"]) * (r["y1"] - r["y0"])
    return {"布局": 布局, "条带": 条带, "走道": 走道, "已排": 已排, "未排": 未排, "余量": 余量, "提示": 提示}


def 布门(排, 门宽, 离墙=0.15, 第二出口=False):
    """每个房间在靠走道的墙上开一扇门，门向房间内开。门洞位置：办公区放在开间中部（缩短最远行走距离）；
    其他房间放在靠入口的左端（离左墙 离墙 m），但房间紧挨租户入口（x0 < 门宽 + 0.5 m）时改放右端，避免与入口门打架；
    有第二出口（右墙走道端）时，紧挨第二出口的房间放左端，两头都挨着的放中部。"""
    W = 排["走道"][2]
    门 = []
    for r in 排["已排"]:
        开间 = r["x1"] - r["x0"]
        宽 = min(门宽, max(开间 - 2 * 离墙, 0.0))
        if 宽 <= 0:
            r["门"] = None
            continue
        挨左 = r["x0"] < 门宽 + 0.5
        挨右 = 第二出口 and r["x1"] > W - 门宽 - 0.5
        if r["类型"] == "办公区" or (挨左 and 挨右):
            x0 = r["x0"] + (开间 - 宽) / 2
        elif 挨左:
            x0 = r["x1"] - min(离墙, (开间 - 宽) / 2) - 宽
        else:
            x0 = r["x0"] + min(离墙, (开间 - 宽) / 2)
        y = r["y1"] if r["门边"] == "上" else r["y0"]
        d = {"房间": r["名称"], "x0": x0, "x1": x0 + 宽, "y": y, "宽": 宽,
             "向内": -1 if r["门边"] == "上" else 1}  # 门扇转向房间内：门边在上 → 向 -y 开
        r["门"] = d
        门.append(d)
    # 租户入口门：左墙走道段的中点
    c0, c1 = 排["走道"][1], 排["走道"][3]
    宽 = min(门宽, c1 - c0 - 0.1)
    yc = (c0 + c1) / 2
    排["入口门"] = {"房间": "租户入口", "x": 0.0, "y0": yc - 宽 / 2, "y1": yc + 宽 / 2, "宽": 宽}
    # 第二出口（可选）：右墙走道段的中点，通向楼宇公共走道（是否可行取决于楼层平面，须设计和 landlord 确认）
    排["第二出口"] = {"房间": "第二出口", "x": W, "y0": yc - 宽 / 2, "y1": yc + 宽 / 2, "宽": 宽} if 第二出口 else None
    return 门


# ---------------------------------------------------------------------------
# 校核
# ---------------------------------------------------------------------------
def D2D8所需宽度(人数):
    """NCC 2022 D2D8 疏散路线净宽（同一层，不经楼梯/陡坡道的水平路线）。"""
    if 人数 < 100:
        return NCC_最小疏散宽度_m
    if 人数 <= 200:
        return 1.0 + 0.25 * math.ceil(max(人数 - 100, 0) / 25)
    return 2.0 + 0.5 * math.ceil((人数 - 200) / 75)


def 校核(W, D, 房间, 排, 参数):
    结论 = []

    def 记(项, 结果, 说明):
        结论.append({"项目": 项, "结果": 结果, "说明": 说明})

    毛面积 = W * D
    走道面积 = (排["走道"][2] - 排["走道"][0]) * (排["走道"][3] - 排["走道"][1])
    可用 = 毛面积 - 走道面积
    需求 = sum(r["面积"] for r in 房间)
    if 需求 > 毛面积 + 1e-6:
        记("总面积", "不合格", f"房间需求合计 {需求:.2f} m² 超出租户区毛面积 {毛面积:.2f} m²")
    elif 需求 > 可用 + 1e-6:
        记("总面积", "不合格", f"房间需求合计 {需求:.2f} m² 未超出毛面积 {毛面积:.2f} m²，但超出扣除走道 "
                         f"{走道面积:.2f} m² 后的可用面积 {可用:.2f} m²")
    else:
        记("总面积", "合格", f"房间需求合计 {需求:.2f} m² ≤ 可用 {可用:.2f} m²（毛面积 {毛面积:.2f} − 走道 {走道面积:.2f}）")
    if 排["未排"]:
        记("排布", "不合格", "放不下的房间：" + "、".join(f"{r['名称']}（{r['面积']:.1f} m²）" for r in 排["未排"]))
    else:
        记("排布", "合格", f"全部 {len(排['已排'])} 个房间已排入")

    # 走道净宽
    人数 = math.ceil(毛面积 / 参数["人均面积"])
    所需 = max(参数["最小走道宽"], D2D8所需宽度(人数))
    净宽 = (排["走道"][3] - 排["走道"][1]) - 参数["隔墙厚"]
    依据 = (f"最小走道宽参数 {参数['最小走道宽']:.2f} m；按 {参数['人均面积']:.0f} m²/人估算 {人数} 人，"
          f"D2D8 要求 {D2D8所需宽度(人数):.2f} m")
    记("走道净宽", "合格" if 净宽 + 1e-9 >= 所需 else "不合格",
      f"走道净宽 {净宽:.2f} m（中心距 {排['走道'][3] - 排['走道'][1]:.2f} − 隔墙厚 {参数['隔墙厚']:.2f}），要求 ≥ {所需:.2f} m（{依据}）")

    # 门
    无门 = [r["名称"] for r in 排["已排"] if not r.get("门")]
    窄门 = [f"{r['名称']}（{r['门']['宽']:.2f} m）" for r in 排["已排"]
          if r.get("门") and r["门"]["宽"] + 1e-9 < NCC_最小门洞净宽_m and r["类型"] != "卫生间"]
    走道y = (排["走道"][1], 排["走道"][3])
    不临走道 = [r["名称"] for r in 排["已排"] if r.get("门") and
             min(abs(r["门"]["y"] - 走道y[0]), abs(r["门"]["y"] - 走道y[1])) > 1e-6]
    if 无门 or 不临走道:
        记("每间至少一扇门", "不合格", "没有门：" + ("、".join(无门) or "无") + "；门不开向走道：" + ("、".join(不临走道) or "无"))
    else:
        记("每间至少一扇门", "合格", f"{len(排['已排'])} 个房间各有 1 扇门开向走道，另有租户入口门 1 扇"
                              + ("、第二出口门 1 扇" if 排.get("第二出口") else ""))
    if 窄门:
        记("门宽", "不合格", "门宽小于 0.75 m（D2D9）：" + "、".join(窄门))
    else:
        记("门宽", "合格", f"门宽 {参数['门宽']:.2f} m ≥ 0.75 m（D2D9；卫生间门除外）")

    # 提示类
    # 直角路径近似：房间最远角 → 本房间门 → 走道中心线 → 沿走道到入口门（x=0）；余量区直接接走道
    yc = (排["走道"][1] + 排["走道"][3]) / 2
    最远, 最远处 = 0.0, ""
    for r in 排["已排"] + 排["余量"]:
        d = r.get("门")
        门x = (d["x0"] + d["x1"]) / 2 if d else r["x0"]
        门y = d["y"] if d else (r["y1"] if r["门边"] == "上" else r["y0"])
        for cx in (r["x0"], r["x1"]):
            for cy in (r["y0"], r["y1"]):
                L = abs(cx - 门x) + abs(cy - 门y) + abs(门y - yc) + (min(门x, W - 门x) if 排.get("第二出口") else 门x)
                if L > 最远:
                    最远, 最远处 = L, r["名称"]
    记("行走距离（提示）", "提示", f"租户区内最远点（{最远处}）到{'最近的租户门' if 排.get('第二出口') else '租户入口门'}约 {最远:.1f} m（直角路径近似，未扣家具）。NCC 2022 D2D5：Class 5 任一点到出口 "
                          f"≤20 m，或到分岔点 ≤20 m 且到其一出口 ≤40 m——出口在楼宇公共部分，须加上公共走道距离，由 certifier/消防顾问核")
    湿 = [r["名称"] for r in 排["已排"] if r["类型"] in 湿区类型]
    if 湿:
        记("湿区位置（提示）", "提示", "、".join(湿) + "：须对照 base building 给排水立管和楼板降板/坡度条件调整位置（本工具不知道立管位置）")
    if 排["余量"]:
        记("余量（提示）", "提示", "未分配面积：" + "、".join(f"{g['条带']} {(g['x1'] - g['x0']) * (g['y1'] - g['y0']):.2f} m²" for g in 排["余量"]))
    return 结论


# ---------------------------------------------------------------------------
# 写 DXF（单位 mm）
# ---------------------------------------------------------------------------
def 写dxf(路径, W, D, 排, 门, 标题, 备注):
    MM = 1000.0
    doc = ezdxf.new("R2010", setup=True)
    doc.header["$INSUNITS"] = 4  # mm
    doc.header["$MEASUREMENT"] = 1
    if "中文" not in doc.styles:
        doc.styles.add("中文", font="simsun.ttc")  # Windows 宋体；其他系统由 CAD 自动替换
    for 名, (色, _, _) in 图层表.items():
        doc.layers.add(名, color=色)
    doc.layers.get("疏散通道示意").dxf.linetype = "DASHED"
    msp = doc.modelspace()

    # 门块：单位宽 1，门扇为竖线 + 90° 弧，插入时按门宽缩放
    blk = doc.blocks.new("门")
    blk.add_line((0, 0), (0, 1))
    blk.add_arc((0, 0), 1, 0, 90)

    # 外轮廓
    msp.add_lwpolyline([(0, 0), (W * MM, 0), (W * MM, D * MM), (0, D * MM)], close=True, dxfattribs={"layer": "外轮廓"})

    # 房间边界（闭合，供读回面积）
    for r in 排["已排"]:
        msp.add_lwpolyline([(r["x0"] * MM, r["y0"] * MM), (r["x1"] * MM, r["y0"] * MM),
                            (r["x1"] * MM, r["y1"] * MM), (r["x0"] * MM, r["y1"] * MM)],
                           close=True, dxfattribs={"layer": "房间边界"})

    # 隔墙（单线中心线，不重复画外轮廓上的边）
    for 段 in 隔墙线段(W, D, 排):
        (x0, y0), (x1, y1) = 段
        msp.add_line((x0 * MM, y0 * MM), (x1 * MM, y1 * MM), dxfattribs={"layer": "隔墙"})

    # 门
    for d in 门:
        if d["向内"] < 0:   # 门边在房间上方：铰链在左端，门扇向下（-y）开
            msp.add_blockref("门", (d["x0"] * MM, d["y"] * MM), dxfattribs={
                "layer": "门", "xscale": d["宽"] * MM, "yscale": -d["宽"] * MM})
        else:
            msp.add_blockref("门", (d["x0"] * MM, d["y"] * MM), dxfattribs={
                "layer": "门", "xscale": d["宽"] * MM, "yscale": d["宽"] * MM})
    e = 排["入口门"]
    # 入口门：铰链在下端，门扇向租户区内（+x）开；块旋转 -90° 使门扇沿 y
    msp.add_blockref("门", (0, e["y1"] * MM), dxfattribs={
        "layer": "门", "xscale": e["宽"] * MM, "yscale": e["宽"] * MM, "rotation": -90})
    msp.add_text("租户入口", height=200, dxfattribs={"layer": "门", "style": "中文"}).set_placement(
        (-300, e["y1"] * MM + 450), align=TextEntityAlignment.MIDDLE_RIGHT)
    e2 = 排.get("第二出口")
    if e2:
        # 第二出口：铰链在右墙下端，块旋转 90° 使门扇向租户区内（-x）开
        msp.add_blockref("门", (W * MM, e2["y0"] * MM), dxfattribs={
            "layer": "门", "xscale": e2["宽"] * MM, "yscale": e2["宽"] * MM, "rotation": 90})
        msp.add_text("第二出口", height=200, dxfattribs={"layer": "门", "style": "中文"}).set_placement(
            (W * MM + 300, e2["y1"] * MM + 450), align=TextEntityAlignment.MIDDLE_LEFT)

    # 房间名、面积
    for r in 排["已排"] + 排["余量"]:
        cx, cy = (r["x0"] + r["x1"]) / 2 * MM, (r["y0"] + r["y1"]) / 2 * MM
        A = (r["x1"] - r["x0"]) * (r["y1"] - r["y0"])
        h = 适配字高(r["名称"], (r["x1"] - r["x0"]) * MM, 250)
        msp.add_text(r["名称"], height=h, dxfattribs={"layer": "房间名", "style": "中文"}).set_placement(
            (cx, cy + 180), align=TextEntityAlignment.MIDDLE_CENTER)
        msp.add_text(f"{A:.1f} m²", height=min(200, h), dxfattribs={"layer": "面积标注", "style": "中文"}).set_placement(
            (cx, cy - 180), align=TextEntityAlignment.MIDDLE_CENTER)
    xa, ya, xb, yb = 排["走道"]
    msp.add_text(f"走道 {yb - ya:.2f} m", height=200, dxfattribs={"layer": "面积标注", "style": "中文"}).set_placement(
        ((xa + xb) / 2 * MM, (ya + yb) / 2 * MM + 250), align=TextEntityAlignment.MIDDLE_CENTER)

    # 疏散通道示意：走道中心线，从远端指向入口门，再出租户区；箭头为开口折线
    for 段 in 疏散线(排):
        msp.add_lwpolyline([(x * MM, y * MM) for x, y in 段], dxfattribs={"layer": "疏散通道示意"})
    msp.add_text("疏散方向示意（经租户门至楼宇公共走道和出口）", height=180,
                 dxfattribs={"layer": "疏散通道示意", "style": "中文"}).set_placement(
        ((xa + xb) / 2 * MM, (ya + yb) / 2 * MM - 300), align=TextEntityAlignment.MIDDLE_CENTER)

    # 总尺寸
    for p1, p2, base, ang in [((0, 0), (W * MM, 0), (0, -800), 0), ((W * MM, 0), (W * MM, D * MM), (W * MM + 1600, 0), 90)]:
        dim = msp.add_linear_dim(base=base, p1=p1, p2=p2, angle=ang, dxfattribs={"layer": "尺寸"})
        dim.render()

    # 图签
    y = -1800
    for 行 in [标题 or "装修平面概念草图", 声明] + ([备注] if 备注 else []) + ["生成：06-技能清单/脚本/装修平面出图.py；单位 mm"]:
        msp.add_text(行, height=220, dxfattribs={"layer": "图签", "style": "中文"}).set_placement((0, y))
        y -= 400
    doc.saveas(路径)


def 适配字高(文字, 可用宽, 最大):
    """按房间开间缩小字高，避免房间名超出房间（中文字宽约等于字高，拉丁字符约 0.6 倍）。"""
    字宽 = sum(1.0 if ord(ch) > 255 else 0.6 for ch in 文字) or 1
    return max(最大 * 0.35, min(最大, 0.9 * 可用宽 / 字宽))


def 隔墙线段(W, D, 排):
    """生成隔墙中心线段（m）：每个房间靠走道的墙（门洞处断开）+ 房间之间和房间末端的侧墙。外轮廓上的边不画。"""
    段 = []
    for s in 排["条带"]:
        rs = s["房间"]
        if not rs:
            continue
        y走 = s["y1"] if s["门边"] == "上" else s["y0"]
        内侧墙 = 0 < y走 < D  # 单侧布局时走道墙也在租户区内
        for r in rs:
            if 内侧墙:
                d = r.get("门")
                if d:
                    if d["x0"] > r["x0"] + 1e-9:
                        段.append(((r["x0"], y走), (d["x0"], y走)))
                    if d["x1"] < r["x1"] - 1e-9:
                        段.append(((d["x1"], y走), (r["x1"], y走)))
                else:
                    段.append(((r["x0"], y走), (r["x1"], y走)))
            # 右侧墙（最后一个房间若到外墙则不画）
            if r["x1"] < W - 1e-9:
                段.append(((r["x1"], s["y0"]), (r["x1"], s["y1"])))
    return 段


def 疏散线(排):
    xa, ya, xb, yb = 排["走道"]
    yc = (ya + yb) / 2
    if 排.get("第二出口"):
        # 两个出口：从走道中点分别指向两端
        中 = (xa + xb) / 2
        线组 = [[(中 - 0.3, yc), (-1.2, yc)], [(中 + 0.3, yc), (xb + 1.2, yc)]]
        for x in [xb * 0.25, -1.2]:
            线组.append([(x + 0.35, yc + 0.2), (x, yc), (x + 0.35, yc - 0.2)])
        for x in [xb * 0.75, xb + 1.2]:
            线组.append([(x - 0.35, yc + 0.2), (x, yc), (x - 0.35, yc - 0.2)])
        return 线组
    主线 = [(xb - 0.5, yc), (-1.2, yc)]
    箭 = []
    for x in [xb * 0.75, xb * 0.5, xb * 0.25, -1.2]:
        箭.append([(x + 0.35, yc + 0.2), (x, yc), (x + 0.35, yc - 0.2)])
    return [主线] + 箭


# ---------------------------------------------------------------------------
# 写 PDF（A3 横向，PyMuPDF 直接绘制同一套几何；PDF 图层名与 DXF 图层同名）
# ---------------------------------------------------------------------------
def _文字分段(s):
    """按字符分成「CJK 字体」和「Helvetica」两类连续段（Helvetica 能显示 ²、数字、拉丁字母）。"""
    段, 当前, 类 = [], "", None
    for ch in s:
        c = "helv" if ord(ch) < 256 else "china-s"
        if c != 类 and 当前:
            段.append((类, 当前))
            当前 = ""
        类 = c
        当前 += ch
    if 当前:
        段.append((类, 当前))
    return 段


def _写字(page, x, y, s, 字号, oc, 对齐="左", 颜色=(0, 0, 0)):
    import pymupdf
    段 = _文字分段(s)
    宽 = sum(pymupdf.get_text_length(t, fontname=f, fontsize=字号) for f, t in 段)
    if 对齐 == "中":
        x -= 宽 / 2
    elif 对齐 == "右":
        x -= 宽
    for f, t in 段:
        page.insert_text((x, y), t, fontname=f, fontsize=字号, color=颜色, oc=oc)
        x += pymupdf.get_text_length(t, fontname=f, fontsize=字号)


def 写pdf(路径, W, D, 排, 门, 标题, 备注):
    import pymupdf
    pt_mm = 72 / 25.4
    纸宽, 纸高 = 420 * pt_mm, 297 * pt_mm   # A3 横向
    边 = 15 * pt_mm
    图签高 = 26 * pt_mm
    可宽, 可高 = 纸宽 - 2 * 边 - 30 * pt_mm, 纸高 - 2 * 边 - 图签高 - 20 * pt_mm
    比例 = next((s for s in [50, 100, 200, 250, 500, 1000]
               if W * 1000 / s * pt_mm <= 可宽 and D * 1000 / s * pt_mm <= 可高), 1000)
    k = 1000 / 比例 * pt_mm   # 每米多少 pt
    ox = 边 + 25 * pt_mm + (可宽 - W * k) / 2
    oy = 边 + 10 * pt_mm + (可高 - D * k) / 2 + D * k  # 原点（租户区左下角）在页面上的位置；PDF y 向下

    def P(x, y):
        return pymupdf.Point(ox + x * k, oy - y * k)

    doc = pymupdf.open()
    page = doc.new_page(width=纸宽, height=纸高)
    oc = {名: doc.add_ocg(名) for 名 in 图层表}

    def 线(层, pts, 闭合=False, 虚线=None):
        _, 色, 宽 = 图层表[层]
        page.draw_polyline([P(*p) for p in pts], color=色, width=宽, closePath=闭合, dashes=虚线, oc=oc[层])

    线("外轮廓", [(0, 0), (W, 0), (W, D), (0, D)], 闭合=True)
    for r in 排["已排"]:
        线("房间边界", [(r["x0"], r["y0"]), (r["x1"], r["y0"]), (r["x1"], r["y1"]), (r["x0"], r["y1"])], 闭合=True)
    for (a, b) in 隔墙线段(W, D, 排):
        线("隔墙", [a, b])
    _, 门色, 门线宽 = 图层表["门"]

    def 门弧(c, a, b):
        """画门扇开启弧（四分之一圆，三次贝塞尔近似，不闭合）：圆心 c，从 c+a 转到 c+b（a、b 垂直等长，单位 m）。"""
        kk = 0.5523
        A = (c[0] + a[0], c[1] + a[1])
        B = (c[0] + b[0], c[1] + b[1])
        sh = page.new_shape()
        sh.draw_bezier(P(*A), P(A[0] + kk * b[0], A[1] + kk * b[1]), P(B[0] + kk * a[0], B[1] + kk * a[1]), P(*B))
        sh.finish(color=门色, width=门线宽, closePath=False, oc=oc["门"])
        sh.commit()
    for d in 门:
        y扇 = d["y"] + d["向内"] * d["宽"]
        线("门", [(d["x0"], d["y"]), (d["x0"], y扇)])
        门弧((d["x0"], d["y"]), (d["宽"], 0), (0, d["向内"] * d["宽"]))
    e = 排["入口门"]
    线("门", [(0, e["y1"]), (e["宽"], e["y1"])])
    门弧((0, e["y1"]), (e["宽"], 0), (0, -e["宽"]))
    字 = max(5.0, min(9.0, 0.25 * k))  # 房间名字号（pt）
    _写字(page, P(-0.3, 0)[0], P(0, e["y1"] + 0.45)[1], "租户入口", 字 * 0.8, oc["门"], 对齐="右")
    e2 = 排.get("第二出口")
    if e2:
        线("门", [(W, e2["y0"]), (W - e2["宽"], e2["y0"])])
        门弧((W, e2["y0"]), (-e2["宽"], 0), (0, e2["宽"]))
        _写字(page, P(W + 0.3, 0)[0], P(0, e2["y1"] + 0.45)[1], "第二出口", 字 * 0.8, oc["门"])
    for r in 排["已排"] + 排["余量"]:
        c = P((r["x0"] + r["x1"]) / 2, (r["y0"] + r["y1"]) / 2)
        A = (r["x1"] - r["x0"]) * (r["y1"] - r["y0"])
        f = 适配字高(r["名称"], (r["x1"] - r["x0"]) * k, 字)
        _写字(page, c.x, c.y - 1, r["名称"], f, oc["房间名"], 对齐="中")
        _写字(page, c.x, c.y + f + 1, f"{A:.1f} m²", min(字 * 0.85, f), oc["面积标注"], 对齐="中", 颜色=图层表["面积标注"][1])
    xa, ya, xb, yb = 排["走道"]
    for 段 in 疏散线(排):
        线("疏散通道示意", 段, 虚线="[4 2] 0")
    _写字(page, P((xa + xb) / 2, 0)[0], P(0, (ya + yb) / 2)[1] + 字 + 1,
        f"走道 {yb - ya:.2f} m  疏散方向示意（经租户门至楼宇公共走道和出口）", 字 * 0.75, oc["疏散通道示意"],
        对齐="中", 颜色=图层表["疏散通道示意"][1])
    # 总尺寸（简化画法：尺寸线 + 文字）
    线("尺寸", [(0, -0.8), (W, -0.8)])
    线("尺寸", [(W + 1.6, 0), (W + 1.6, D)])
    _写字(page, P(W / 2, -0.8)[0], P(0, -0.8)[1] + 9, f"{W * 1000:.0f}", 7, oc["尺寸"], 对齐="中")
    _写字(page, P(W + 1.8, 0)[0], P(0, D / 2)[1], f"{D * 1000:.0f}", 7, oc["尺寸"])
    # 图签
    y0 = 纸高 - 边 - 图签高
    page.draw_rect(pymupdf.Rect(边, y0, 纸宽 - 边, 纸高 - 边), color=(0, 0, 0), width=0.5, oc=oc["图签"])
    行 = [标题 or "装修平面概念草图", f"比例 1:{比例}（A3）  单位 mm  租户区 {W:.2f} × {D:.2f} m = {W * D:.1f} m²", 声明]
    if 备注:
        行.append(备注)
    for i, s in enumerate(行):
        _写字(page, 边 + 6, y0 + 13 + i * 9.5, s, 10 if i == 0 else 7.5, oc["图签"])
    # 比例尺（5 m）
    线("尺寸", [(0, -2.0), (5, -2.0)])
    _写字(page, P(5.2, 0)[0], P(0, -2.0)[1] + 2, "5 m", 6.5, oc["尺寸"])
    doc.set_metadata({"title": 标题 or "装修平面概念草图", "subject": 声明, "creator": "装修平面出图.py"})
    doc.save(路径)
    return 比例


# ---------------------------------------------------------------------------
# 主程序
# ---------------------------------------------------------------------------
def 运行(argv=None):
    ap = argparse.ArgumentParser(description="按房间清单排出商业装修平面概念草图（DXF + PDF）并校核")
    ap.add_argument("清单", help="房间清单 .json 或 .csv")
    ap.add_argument("-o", "--输出", required=True, help="输出前缀（不含扩展名），如 out/方案A")
    ap.add_argument("--宽", type=float, help="租户区外轮廓宽（x 向，m）")
    ap.add_argument("--深", type=float, help="租户区外轮廓深（y 向，m）")
    ap.add_argument("--走道宽", type=float, help="走道中心距（m，默认 1.5）")
    ap.add_argument("--最小走道宽", type=float, help=f"校核用的最小走道净宽（m，默认 {NCC_最小疏散宽度_m}，NCC 2022 D2D8）")
    ap.add_argument("--门宽", type=float, help="房间门净宽（m，默认 0.92）")
    ap.add_argument("--隔墙厚", type=float, help="隔墙厚（m，默认 0.1，用于算走道净宽）")
    ap.add_argument("--人均面积", type=float, help=f"估算人数用的 m²/人（默认 {NCC_办公人均面积_m2}，Table D2D18 办公）")
    ap.add_argument("--布局", choices=["自动", "双侧", "单侧"], help="条带布局（默认 自动）")
    ap.add_argument("--下侧进深", type=float, help="双侧布局时下侧条带进深（m），默认两侧平分；上侧 = 深 − 走道宽 − 下侧进深")
    ap.add_argument("--第二出口", action="store_true", help="在右墙走道端加第二道租户门（通向楼宇公共走道，须确认楼层平面允许）")
    ap.add_argument("--余量并入", help="条带末端余量并入该类型的房间（如 办公区）；默认标为「余量（未分配）」")
    ap.add_argument("--标题")
    ap.add_argument("--备注")
    ap.add_argument("--严格", action="store_true", help="有不合格项时退出码为 1")
    a = ap.parse_args(argv)

    配置, 房间 = 读清单(a.清单)
    p = 配置.get("参数", {})

    def 取(名, 默认):
        v = getattr(a, 名)
        return v if v is not None else (p.get(名) if p.get(名) is not None else 默认)

    W = a.宽 or 配置.get("宽")
    D = a.深 or 配置.get("深")
    if not W or not D:
        raise SystemExit("缺少租户区外轮廓：JSON 写 \"租户区\": {\"宽\":..,\"深\":..}，CSV 加一行 类型=租户区，或用 --宽 --深")
    参数 = {"走道宽": float(取("走道宽", 1.5)), "最小走道宽": float(取("最小走道宽", NCC_最小疏散宽度_m)),
          "门宽": float(取("门宽", 0.92)), "隔墙厚": float(取("隔墙厚", 0.1)),
          "人均面积": float(取("人均面积", NCC_办公人均面积_m2)), "布局": 取("布局", "自动"),
          "余量并入": 取("余量并入", None), "下侧进深": 取("下侧进深", None),
          "第二出口": bool(a.第二出口 or p.get("第二出口"))}
    标题 = a.标题 or 配置.get("标题")
    备注 = a.备注 or 配置.get("备注")

    排 = 排布(W, D, 房间, 参数["走道宽"], 参数["布局"], 参数["余量并入"], 下侧进深=参数["下侧进深"])
    门 = 布门(排, 参数["门宽"], 第二出口=参数["第二出口"])
    结论 = 校核(W, D, 房间, 排, 参数)

    前缀 = a.输出
    os.makedirs(os.path.dirname(os.path.abspath(前缀)), exist_ok=True)
    写dxf(前缀 + ".dxf", W, D, 排, 门, 标题, 备注)
    比例 = 写pdf(前缀 + ".pdf", W, D, 排, 门, 标题, 备注)
    隔墙长 = sum(math.dist(a_, b_) for a_, b_ in 隔墙线段(W, D, 排))
    报告 = {
        "标题": 标题, "备注": 备注, "声明": 声明, "租户区": {"宽": W, "深": D, "面积": W * D}, "参数": 参数,
        "布局": 排["布局"], "PDF比例": f"1:{比例}",
        "走道": {"y0": 排["走道"][1], "y1": 排["走道"][3], "面积": W * (排["走道"][3] - 排["走道"][1])},
        "房间": [{"名称": r["名称"], "类型": r["类型"], "需求面积": round(r["面积"], 3),
                "排布面积": round((r["x1"] - r["x0"]) * (r["y1"] - r["y0"]), 3),
                "x0": r["x0"], "y0": r["y0"], "x1": r["x1"], "y1": r["y1"], "条带": r["条带"],
                "门宽": r["门"]["宽"] if r.get("门") else None} for r in 排["已排"]],
        "未排": [{"名称": r["名称"], "面积": r["面积"]} for r in 排["未排"]],
        "余量": [{"条带": g["条带"], "面积": round((g["x1"] - g["x0"]) * (g["y1"] - g["y0"]), 3)} for g in 排["余量"]],
        "门数": len(门) + 1 + (1 if 排.get("第二出口") else 0), "隔墙中心线长m": round(隔墙长, 3),
        "校核": 结论, "排布提示": 排["提示"],
    }
    with open(前缀 + "_校核.json", "w", encoding="utf-8") as f:
        json.dump(报告, f, ensure_ascii=False, indent=2)

    # 终端摘要（文件已先写出）
    print(f"租户区 {W:.2f} × {D:.2f} m = {W * D:.2f} m²；布局：{排['布局']}；PDF 比例 1:{比例}")
    for r in 报告["房间"]:
        print(f"  {r['名称']:<10} {r['类型']:<5} 需求 {r['需求面积']:>7.2f} m²  排布 {r['排布面积']:>7.2f} m²  ({r['条带']})")
    for g in 报告["余量"]:
        print(f"  余量（未分配）  {g['条带']}  {g['面积']:.2f} m²")
    print(f"门 {报告['门数']} 扇（含租户门）；隔墙中心线 {隔墙长:.2f} m")
    for c in 结论:
        print(f"[{c['结果']}] {c['项目']}：{c['说明']}")
    for t in 排["提示"]:
        print(f"  提示：{t}")
    print(声明)
    print(f"已写出：{前缀}.dxf、{前缀}.pdf、{前缀}_校核.json")
    不合格 = [c for c in 结论 if c["结果"] == "不合格"]
    return 报告, (1 if (a.严格 and 不合格) else 0)


if __name__ == "__main__":
    try:
        _, 码 = 运行()
        sys.exit(码)
    except BrokenPipeError:   # 终端输出被 head 截断：文件已先写出，安静退出
        sys.stderr.close()
