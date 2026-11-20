#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
运行装修平面测试.py —— 用示例办公清单检验 装修平面出图.py 的输出，并用 dxf算量.py、pdf图纸量尺.py 读回核对面积。
用法：python3 运行装修平面测试.py   （临时输出写到系统临时目录，最后打印 通过/失败）

已知答案（示例办公清单.json，18.0 × 12.0 m，走道 1.5 m，下侧进深 4.5 m，上侧 6.0 m）：
  外轮廓 216 m²；房间 7 个，面积 18 / 22.5 / 13.5 / 13.5 / 9 / 96 / 12，合计 184.5 m²；
  门块 8 个（7 个房间 + 租户入口）；隔墙中心线 57.06 m（下侧走道墙 17 − 5×0.92 + 侧墙 5×4.5，
  上侧走道墙 18 − 2×0.92 + 侧墙 1×6.0）；总尺寸 18 m、12 m；下侧余量 4.5 m²。
"""
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

这里 = os.path.dirname(os.path.abspath(__file__))
脚本目录 = os.path.dirname(os.path.dirname(这里))
sys.path.insert(0, 脚本目录)

import importlib.util  # noqa: E402

import ezdxf  # noqa: E402
import pymupdf  # noqa: E402


def 载入(文件名, 模块名):
    spec = importlib.util.spec_from_file_location(模块名, os.path.join(脚本目录, 文件名))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


出图 = 载入("装修平面出图.py", "装修平面出图")
dxf = 载入("dxf算量.py", "dxf算量")
pdf = 载入("pdf图纸量尺.py", "pdf图纸量尺")

结果表 = []


def 核对(名, 实测, 期望, 容差=1e-3):
    if isinstance(期望, (int, float)) and not isinstance(期望, bool):
        ok = 实测 is not None and abs(实测 - 期望) <= 容差
    else:
        ok = 实测 == 期望
    结果表.append((名, ok, 实测, 期望))


def 静默运行(argv):
    """运行出图主程序，屏蔽终端输出，返回 (报告, 退出码)。"""
    with contextlib.redirect_stdout(io.StringIO()):
        return 出图.运行(argv)


def 结论(报告, 项目):
    return next(c["结果"] for c in 报告["校核"] if c["项目"] == 项目)


临时 = tempfile.mkdtemp(prefix="装修平面测试_")
清单json = os.path.join(这里, "示例办公清单.json")
清单csv = os.path.join(这里, "示例办公清单.csv")
期望面积 = sorted([18.0, 22.5, 13.5, 13.5, 9.0, 96.0, 12.0])
必需图层 = ["外轮廓", "隔墙", "门", "房间名", "面积标注", "疏散通道示意"]

# 1. JSON 输入：排布和校核
前缀 = os.path.join(临时, "示例")
报告, 码 = 静默运行([清单json, "-o", 前缀])
核对("JSON：退出码 0", 码, 0)
核对("JSON：布局为双侧", 报告["布局"], "双侧")
核对("JSON：排入房间数", len(报告["房间"]), 7)
核对("JSON：排布面积合计", sum(r["排布面积"] for r in 报告["房间"]), 184.5)
核对("JSON：排布面积 = 需求面积（逐间）", all(abs(r["排布面积"] - r["需求面积"]) < 0.05 for r in 报告["房间"]), True)
核对("JSON：下侧余量", sum(g["面积"] for g in 报告["余量"]), 4.5)
核对("JSON：门数（含入口）", 报告["门数"], 8)
核对("JSON：隔墙中心线长", 报告["隔墙中心线长m"], 57.06)
for 项 in ["总面积", "排布", "走道净宽", "每间至少一扇门", "门宽"]:
    核对(f"JSON：校核「{项}」合格", 结论(报告, 项), "合格")
核对("JSON：PDF 比例 1:100", 报告["PDF比例"], "1:100")
核对("JSON：输出文件齐全", all(os.path.exists(前缀 + 后) for 后 in [".dxf", ".pdf", "_校核.json"]), True)

# 2. 用 dxf算量.py 读回 DXF
doc = ezdxf.readfile(前缀 + ".dxf")
单位说明, k, _ = dxf.确定单位(doc)
统计, 明细 = dxf.统计(doc)
核对("DXF：单位 mm", k, 0.001, 1e-12)
核对("DXF：6 个必需图层都存在", all(doc.layers.has_entry(n) for n in 必需图层), True)
核对("DXF：外轮廓闭合面积", 统计["外轮廓"].闭合面积 * k * k, 216.0)
核对("DXF：房间边界闭合个数", 统计["房间边界"].闭合数, 7)
核对("DXF：房间边界面积合计", 统计["房间边界"].闭合面积 * k * k, 184.5)
核对("DXF：逐间面积与清单一致",
   [round(m[3] * k * k, 3) for m in sorted(明细, key=lambda m: m[3]) if m[0] == "房间边界"], 期望面积)
核对("DXF：门块数量", sum(统计["门"].块.values()), 8)
核对("DXF：隔墙线长", 统计["隔墙"].线长 * k, 57.06)
名称集 = {t[1] for t in 统计["房间名"].文字}
核对("DXF：房间名齐全", {"前台接待", "会议室", "经理室", "茶水间", "库房", "开放办公区", "打印区"} <= 名称集, True)
核对("DXF：面积标注含 96.0 m²", any(t[1] == "96.0 m²" for t in 统计["面积标注"].文字), True)
核对("DXF：疏散通道示意有线", 统计["疏散通道示意"].线数 > 0, True)
尺寸值 = sorted(round(v * k, 3) for _, v, _ in 统计["尺寸"].尺寸 if v is not None)
核对("DXF：总尺寸 12 m、18 m", 尺寸值, [12.0, 18.0])
# 命令行方式写 xlsx 也要成功
xlsx = 前缀 + "_算量.xlsx"
r = subprocess.run([sys.executable, os.path.join(脚本目录, "dxf算量.py"), 前缀 + ".dxf", xlsx], capture_output=True, text=True)
核对("DXF：dxf算量.py 命令行写出 xlsx", r.returncode == 0 and os.path.exists(xlsx), True)

# 3. 用 pdf图纸量尺.py 读回 PDF（按 1:100）
d = pymupdf.open(前缀 + ".pdf")
ocg = {v["name"] for v in d.get_ocgs().values()}
核对("PDF：1 页", d.page_count, 1)
核对("PDF：6 个必需图层（OCG）都存在", set(必需图层) <= ocg, True)
for 层, 期望, 个数 in [("外轮廓", 216.0, 1), ("房间边界", 184.5, 7)]:
    with contextlib.redirect_stdout(io.StringIO()):
        res = pdf.main(["量尺", 前缀 + ".pdf", "--比例", "1:100", "--图层", 层])
    核对(f"PDF：{层}闭合面积（1:100）", res["合计闭合面积m2"], 期望, 0.01)
    核对(f"PDF：{层}闭合个数", sum(g["闭合数"] for g in res["分组"].values()), 个数)
with contextlib.redirect_stdout(io.StringIO()):
    res = pdf.main(["量尺", 前缀 + ".pdf", "--比例", "1:100", "--图层", "门"])
核对("PDF：门弧不闭合（门图层闭合面积为 0）", sum(g["闭合数"] for g in res["分组"].values()), 0)
核对("PDF：门图层线长 = 8 ×（门扇 0.92 + 四分之一弧）", res["合计线长m"], 8 * (0.92 + 3.14159265 / 2 * 0.92), 0.01)
文字 = d[0].get_text()
核对("PDF：含概念草图声明", "合资格的设计人员" in 文字, True)
核对("PDF：含房间名", "开放办公区" in 文字 and "前台接待" in 文字, True)

# 4. CSV 输入与 JSON 结果一致
报告csv, _ = 静默运行([清单csv, "-o", os.path.join(临时, "示例csv"), "--走道宽", "1.5", "--下侧进深", "4.5"])
核对("CSV：房间与 JSON 一致",
   [(r["名称"], r["排布面积"]) for r in 报告csv["房间"]], [(r["名称"], r["排布面积"]) for r in 报告["房间"]])

# 4b. 第二出口：门数 +1，最远行走距离缩短
def 行走(报告_):
    说明 = next(c["说明"] for c in 报告_["校核"] if c["项目"] == "行走距离（提示）")
    return float(说明.split("约 ")[1].split(" m")[0])


前缀2 = os.path.join(临时, "双出口")
报告2, _ = 静默运行([清单json, "-o", 前缀2, "--第二出口"])
核对("第二出口：门数 9", 报告2["门数"], 9)
统计2, _ = dxf.统计(ezdxf.readfile(前缀2 + ".dxf"))
核对("第二出口：DXF 门块 9 个", sum(统计2["门"].块.values()), 9)
核对("第二出口：最远行走距离缩短", 行走(报告2) < 行走(报告), True)
核对("第二出口：房间面积不变", 统计2["房间边界"].闭合面积 * 1e-6, 184.5)

# 5. 反例：校核要能报不合格
with open(清单json, encoding="utf-8") as f:
    超 = json.load(f)
超["房间"].append({"名称": "加建会议室", "类型": "会议室", "面积": 60.0})
超json = os.path.join(临时, "超面积.json")
with open(超json, "w", encoding="utf-8") as f:
    json.dump(超, f, ensure_ascii=False)
报告超, 码超 = 静默运行([超json, "-o", os.path.join(临时, "超面积"), "--严格"])
核对("反例：总面积超出可用面积 → 不合格", 结论(报告超, "总面积"), "不合格")
核对("反例：放不下的房间 → 排布不合格", 结论(报告超, "排布"), "不合格")
核对("反例：--严格 时退出码 1", 码超, 1)
报告窄, _ = 静默运行([清单json, "-o", os.path.join(临时, "窄走道"), "--走道宽", "1.0", "--门宽", "0.7"])
核对("反例：走道中心距 1.0 − 墙厚 0.1 = 0.9 < 1.0 → 不合格", 结论(报告窄, "走道净宽"), "不合格")
核对("反例：门宽 0.7 < 0.75 → 不合格", 结论(报告窄, "门宽"), "不合格")
报告参, _ = 静默运行([清单json, "-o", os.path.join(临时, "参数"), "--最小走道宽", "1.5"])
核对("反例：最小走道宽参数 1.5 > 净宽 1.4 → 不合格", 结论(报告参, "走道净宽"), "不合格")

# 6. D2D8 宽度公式（NCC 2022：100–200 人每 25 人加 250 mm；>200 人 2 m + 每 75 人加 500 mm）
for 人数, 期望 in [(99, 1.0), (100, 1.0), (101, 1.25), (125, 1.25), (126, 1.5), (200, 2.0), (201, 2.5), (275, 2.5), (276, 3.0)]:
    核对(f"D2D8：{人数} 人 → {期望} m", 出图.D2D8所需宽度(人数), 期望)

# 汇总
通过 = sum(1 for _, ok, _, _ in 结果表 if ok)
for 名, ok, 实测, 期望 in 结果表:
    print(f"{'通过' if ok else '失败'}  {名}" + ("" if ok else f"  实测={实测!r} 期望={期望!r}"))
print(f"临时输出：{临时}")
print(f"共 {len(结果表)} 项，通过 {通过}，失败 {len(结果表) - 通过}")
sys.exit(0 if 通过 == len(结果表) else 1)
