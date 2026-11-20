#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
运行测试.py —— 用已知答案的测试图核对 dxf算量.py 和 pdf图纸量尺.py。
用法：python3 运行测试.py   （先自动重新生成测试数据，再逐项核对，最后打印 通过/失败）
临时输出（xlsx、png、旋转页 PDF）写到系统临时目录，不留在知识库里。
"""
import contextlib
import io
import math
import os
import sys
import tempfile

sys.dont_write_bytecode = True  # 不在测试数据文件夹留下 __pycache__

这里 = os.path.dirname(os.path.abspath(__file__))
脚本目录 = os.path.dirname(这里)
sys.path.insert(0, 脚本目录)
sys.path.insert(0, 这里)

import 生成测试数据 as 生成   # noqa: E402
import importlib.util       # noqa: E402


def 载入(文件名, 模块名):
    spec = importlib.util.spec_from_file_location(模块名, os.path.join(脚本目录, 文件名))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


dxf = 载入("dxf算量.py", "dxf算量")
pdf = 载入("pdf图纸量尺.py", "pdf图纸量尺")
已知 = 生成.已知值
结果表 = []


def 核对(名, 实测, 期望, 容差=1e-3):
    if isinstance(期望, (int, float)) and not isinstance(期望, bool):
        ok = 实测 is not None and abs(实测 - 期望) <= 容差 * max(1.0, abs(期望))
        结果表.append((ok, f"{名}：实测 {实测:.4f}，期望 {期望:.4f}" if 实测 is not None else f"{名}：无结果"))
    else:
        ok = 实测 == 期望
        结果表.append((ok, f"{名}：实测 {实测}，期望 {期望}"))


def 静默(fn, *a):
    """运行时屏蔽脚本的终端输出，只保留核对结果。"""
    with contextlib.redirect_stdout(io.StringIO()):
        return fn(*a)


# ---------------------------------------------------------------- 生成数据
静默(lambda: (生成.生成dxf(os.path.join(这里, "测试平面_mm.dxf"), 0.001),
              生成.生成dxf(os.path.join(这里, "测试平面_m.dxf"), 1.0),
              生成.生成pdf(os.path.join(这里, "测试平面_1比100_A3.pdf"), os.path.join(这里, "测试平面_A3缩印到A4.pdf"))))
临时 = tempfile.mkdtemp(prefix="读图量图测试_")

# ---------------------------------------------------------------- DXF 测试
for 文件 in ("测试平面_mm.dxf", "测试平面_m.dxf"):
    xlsx = os.path.join(临时, 文件 + ".xlsx")
    r, k = 静默(dxf.main, [os.path.join(这里, 文件), xlsx])
    核对(f"[{文件}] 外墙线长 m", r["外墙"].线长 * k, 已知["外墙_线长"])
    核对(f"[{文件}] 外墙面积 m²", r["外墙"].闭合面积 * k * k, 已知["外墙_面积"])
    核对(f"[{文件}] 内墙线长 m", r["内墙"].线长 * k, 已知["内墙_线长"])
    核对(f"[{文件}] 门块数量", r["门"].块["DOOR"], 已知["门_数量"])
    核对(f"[{文件}] 窗块数量", r["窗"].块["WINDOW"], 已知["窗_数量"])
    核对(f"[{文件}] 尺寸测量值 m", r["尺寸"].尺寸[0][1] * k, 已知["尺寸_值"])
    核对(f"[{文件}] 房间文字", {t[1] for t in r["文字"].文字}, 已知["房间文字"])
    核对(f"[{文件}] HATCH 面积（含孔洞）m²", r["地面填充"].填充面积 * k * k, 已知["填充_面积"])
    核对(f"[{文件}] 弧线/凸度线长 m", r["弧线测试"].线长 * k, 已知["弧线测试_线长"])
    核对(f"[{文件}] 凸度圆面积 m²", r["弧线测试"].闭合面积 * k * k, 已知["弧线测试_面积"])
    # 读回 xlsx：每个图层一行 + 合计
    from openpyxl import load_workbook
    ws = load_workbook(xlsx)["按图层汇总"]
    行 = {row[0]: row for row in ws.iter_rows(min_row=2, values_only=True)}
    核对(f"[{文件}] xlsx 图层行数", len([k_ for k_ in 行 if k_ != "合计"]), 8)
    核对(f"[{文件}] xlsx 外墙面积", 行["外墙"][5], 200.0)
    核对(f"[{文件}] xlsx 块合计", 行["合计"][9], 13)

# 图层过滤（含通配符）
r, k = 静默(dxf.main, [os.path.join(这里, "测试平面_mm.dxf"), "--图层", "外墙", "内*"])
核对("[图层过滤] 只剩 2 个图层", sorted(r), ["内墙", "外墙"])
# 展开块：门 5 ×（门扇 0.82 + 弧 0.82×π/2），窗 8 × 3 × 1.8
r, k = 静默(dxf.main, [os.path.join(这里, "测试平面_mm.dxf"), "--图层", "门", "窗", "--展开块"])
核对("[展开块] 门图层线长 m", r["门"].线长 * k, 5 * (0.82 + 0.82 * math.pi / 2))
核对("[展开块] 窗图层线长 m", r["窗"].线长 * k, 8 * 3 * 1.8)
# 强制单位：把 mm 图当作 m 读，长度应放大 1000 倍
r, k = 静默(dxf.main, [os.path.join(这里, "测试平面_mm.dxf"), "--图层", "外墙", "--单位", "m"])
核对("[--单位 覆盖] 外墙线长", r["外墙"].线长 * k, 60000.0)

# ---------------------------------------------------------------- PDF 测试
A3 = os.path.join(这里, "测试平面_1比100_A3.pdf")
A4 = os.path.join(这里, "测试平面_A3缩印到A4.pdf")
pt = 72 / 25.4
区域 = "130,130,720,440"          # 平面所在区域（pt），不含下方尺寸线
期望长 = 60 + 27 + math.pi * 1.0  # 外墙 + 内墙 + 圆柱周长（半径 0.5 m）
期望面积 = 200 + math.pi * 0.25

r = 静默(pdf.main, ["量尺", A3, "--比例", "1:100", "--区域", 区域, "--输出", os.path.join(临时, "a3.xlsx")])
核对("[PDF A3 1:100] 合计线长 m", r["合计线长m"], 期望长)
核对("[PDF A3 1:100] 合计闭合面积 m²（圆为贝塞尔近似，容差 0.1%）", r["合计闭合面积m2"], 期望面积)
核对("[PDF A3 1:100] 区域内文字", {t["文字"] for t in r["文字"]}, 已知["房间文字"])

r = 静默(pdf.main, ["量尺", A3, "--比例", "1:100", "--区域", 区域, "--颜色", "#0000FF"])
核对("[PDF 按线色] 内墙（蓝线）长 m", r["合计线长m"], 27.0)

r = 静默(pdf.main, ["量尺", A4, "--比例", "1:100", "--纸张", "A3", "--区域", "90,90,510,315"])
核对("[PDF A3 缩印 A4 + --纸张 A3] 合计线长 m", r["合计线长m"], 期望长)
核对("[PDF A3 缩印 A4 + --纸张 A3] 外墙面积 m²", max(c["面积m2"] for c in r["闭合明细"]), 200.0)

# 两点校准：外墙下边两端点 (50 mm, 150 mm)–(250 mm, 150 mm) = 20 m
校准 = f"{50 * pt},{150 * pt},{250 * pt},{150 * pt},20"
r = 静默(pdf.main, ["量尺", A3, "--校准", 校准, "--区域", 区域])
核对("[PDF 两点校准] 合计线长 m", r["合计线长m"], 期望长)
# 像素坐标：按 150 dpi 渲染后的像素坐标给区域和校准点
d = 150 / 72
像素区域 = ",".join(str(v * d) for v in (130, 130, 720, 440))
像素校准 = f"{50 * pt * d},{150 * pt * d},{250 * pt * d},{150 * pt * d},20"
r = 静默(pdf.main, ["量尺", A3, "--校准", 像素校准, "--区域", 像素区域, "--像素dpi", "150"])
核对("[PDF 像素坐标 150dpi] 外墙面积 m²", max(c["面积m2"] for c in r["闭合明细"]), 200.0)

# 旋转页：把 A3 页面设为旋转 90°，坐标按显示方向处理，量出的长度不变
import pymupdf  # noqa: E402
旋 = os.path.join(临时, "旋转90.pdf")
dd = pymupdf.open(A3)
dd[0].set_rotation(90)
dd.save(旋)
r = 静默(pdf.main, ["量尺", 旋, "--比例", "1:100"])
核对("[PDF 旋转 90° 整页] 外墙面积 m²", max(c["面积m2"] for c in r["闭合明细"]), 200.0)
核对("[PDF 旋转 90° 整页] 文字数（含尺寸和图签）", len(r["文字"]), 7)

# 渲染 PNG（两种引擎）
静默(pdf.main, ["渲染", A3, "--dpi", "100", "-o", os.path.join(临时, "p1.png")])
核对("[渲染 pymupdf] PNG 存在", os.path.getsize(os.path.join(临时, "p1.png")) > 1000, True)
import shutil  # noqa: E402
if shutil.which("pdftoppm"):
    静默(pdf.main, ["渲染", A3, "--dpi", "100", "--引擎", "pdftoppm", "-o", os.path.join(临时, "p2.png")])
    核对("[渲染 pdftoppm] PNG 存在", os.path.exists(os.path.join(临时, "p2.png")), True)

# ---------------------------------------------------------------- 汇总
通过 = sum(1 for ok, _ in 结果表 if ok)
for ok, msg in 结果表:
    print(("通过  " if ok else "失败  ") + msg)
print(f"\n共 {len(结果表)} 项，通过 {通过}，失败 {len(结果表) - 通过}。临时输出：{临时}")
sys.exit(0 if 通过 == len(结果表) else 1)
