#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成读图量图工具的测试数据（已知答案）：
  测试平面_mm.dxf   10 m × 20 m 平面，单位 mm（$INSUNITS=4）
  测试平面_m.dxf    同一平面，单位 m（$INSUNITS=6），用于检验单位换算
  测试平面_1比100_A3.pdf   同一平面按 1:100 画在 A3 横向矢量 PDF 上
  测试平面_A3缩印到A4.pdf  把上面的 A3 图缩印到 A4（检验「比例 + 纸张尺寸」换算）

已知答案（见文末 已知值，运行测试.py 会逐项核对）：
  外墙：闭合多段线 20 × 10 m（中心线），周长 60 m，面积 200 m²
  内墙：3 条直线 10 + 12 + 5 = 27 m
  门：块 DOOR × 5；窗：块 WINDOW × 8
  尺寸：一个线性标注 20.000 m
  文字：卧室1、卧室2、客厅、厨房、浴室（5 个），其中 MTEXT 1 个
  地面填充：浴室 HATCH 3 × 2.5 = 7.5 m²，其中挖去 0.5 × 0.5 的孔 → 7.25 m²
  弧线测试：ARC 半径 1 m、90° → 1.5708 m；凸度圆（两段 bulge=1）半径 1 m → 周长 6.2832 m、面积 3.1416 m²
用法：python3 生成测试数据.py   （在本文件夹生成全部测试文件）
"""
import math
import os

import ezdxf

这里 = os.path.dirname(os.path.abspath(__file__))

# 已知值（单位 m / m²），运行测试.py 引用
已知值 = {
    "外墙_线长": 60.0, "外墙_面积": 200.0,
    "内墙_线长": 27.0,
    "门_数量": 5, "窗_数量": 8,
    "尺寸_值": 20.0,
    "房间文字": {"卧室1", "卧室2", "客厅", "厨房", "浴室"},
    "填充_面积": 7.25,
    "弧线测试_线长": math.pi / 2 + 2 * math.pi,   # ARC + 凸度圆周长
    "弧线测试_面积": math.pi,
}


def 生成dxf(路径, 单位米):
    """单位米：每个图纸单位等于多少米（mm 图为 0.001，m 图为 1）。"""
    s = 1.0 / 单位米 / 1000.0  # 把「毫米数值」换成图纸单位的系数（mm 图 s=1，m 图 s=0.001）

    def P(x, y):  # 输入坐标按毫米书写
        return (x * s, y * s)

    doc = ezdxf.new("R2018", setup=True)
    doc.header["$INSUNITS"] = 4 if 单位米 == 0.001 else 6
    for 名, 色 in [("外墙", 1), ("内墙", 3), ("门", 2), ("窗", 5), ("尺寸", 7), ("文字", 7),
                  ("地面填充", 8), ("弧线测试", 6)]:
        doc.layers.add(名, color=色)

    # 门块：门扇线 + 90° 开启弧（块内图元放在 0 层，插入后继承插入图层）
    门 = doc.blocks.new("DOOR")
    门.add_line(P(0, 0), P(0, 820))
    门.add_arc(P(0, 0), 820 * s, 0, 90)
    # 窗块：三条平行线表示 1800 宽窗
    窗 = doc.blocks.new("WINDOW")
    for y in (0, 45, 90):
        窗.add_line(P(0, y), P(1800, y))

    msp = doc.modelspace()
    # 外墙：闭合矩形 20 m × 10 m
    msp.add_lwpolyline([P(0, 0), P(20000, 0), P(20000, 10000), P(0, 10000)], close=True,
                       dxfattribs={"layer": "外墙"})
    # 内墙：x=8000 竖墙 10 m；y=5000 横墙 12 m；x=14000 竖墙 5 m
    msp.add_line(P(8000, 0), P(8000, 10000), dxfattribs={"layer": "内墙"})
    msp.add_line(P(8000, 5000), P(20000, 5000), dxfattribs={"layer": "内墙"})
    msp.add_line(P(14000, 0), P(14000, 5000), dxfattribs={"layer": "内墙"})
    # 门 5 个
    for x, y in [(1000, 0), (8000, 2000), (8000, 7000), (15000, 5000), (10000, 5000)]:
        msp.add_blockref("DOOR", P(x, y), dxfattribs={"layer": "门"})
    # 窗 8 个
    for x, y in [(2000, 10000), (5000, 10000), (10000, 10000), (15000, 10000),
                 (3000, 0), (10000, 0), (16000, 0), (18000, 0)]:
        msp.add_blockref("WINDOW", P(x, y), dxfattribs={"layer": "窗"})
    # 尺寸：外墙长边 20 m
    dim = msp.add_linear_dim(base=P(0, -1500), p1=P(0, 0), p2=P(20000, 0),
                             dxfattribs={"layer": "尺寸"})
    dim.render()
    # 房间文字（4 个 TEXT + 1 个 MTEXT）
    for 名, x, y in [("卧室1", 3000, 7500), ("卧室2", 3000, 2500), ("客厅", 13000, 7500), ("厨房", 10500, 2500)]:
        msp.add_text(名, height=300 * s, dxfattribs={"layer": "文字"}).set_placement(P(x, y))
    msp.add_mtext("浴室", dxfattribs={"layer": "文字", "char_height": 300 * s}).set_location(P(16500, 2500))
    # 地面填充：浴室 3 m × 2.5 m（x 14000–17000, y 0–2500），中间挖 0.5 m × 0.5 m 孔
    h = msp.add_hatch(color=8, dxfattribs={"layer": "地面填充"})
    h.paths.add_polyline_path([P(14000, 0), P(17000, 0), P(17000, 2500), P(14000, 2500)], is_closed=True, flags=1)
    h.paths.add_polyline_path([P(15000, 1000), P(15500, 1000), P(15500, 1500), P(15000, 1500)], is_closed=True, flags=0)
    # 弧线测试：ARC 半径 1 m 90°；凸度圆（两段半圆）半径 1 m
    msp.add_arc(P(25000, 5000), 1000 * s, 0, 90, dxfattribs={"layer": "弧线测试"})
    msp.add_lwpolyline([(*P(24000, 2000), 0, 0, 1.0), (*P(26000, 2000), 0, 0, 1.0)],
                       format="xyseb", close=True, dxfattribs={"layer": "弧线测试"})
    doc.saveas(路径)


# ---------------------------------------------------------------------------
# PDF：1:100、A3 横向（420 × 297 mm）。1 mm 纸面 = 72/25.4 pt；1:100 → 1 m 实际 = 10 mm 纸面
# ---------------------------------------------------------------------------
def 生成pdf(路径A3, 路径A4):
    import pymupdf

    pt = 72.0 / 25.4          # 每毫米多少 pt
    米 = 10.0 * pt            # 1:100 时实际 1 m 在纸面上的 pt 数
    x0, y0 = 50 * pt, 50 * pt  # 平面左上角放在纸面 (50 mm, 50 mm)

    def Q(x, y):  # 实际坐标（m，y 向上）→ PDF 坐标（pt，y 向下）
        return pymupdf.Point(x0 + x * 米, y0 + (10 - y) * 米)

    doc = pymupdf.open()
    page = doc.new_page(width=420 * pt, height=297 * pt)
    # 外墙：闭合矩形 20 × 10 m（用 draw_rect 生成 're' 路径）
    page.draw_rect(pymupdf.Rect(Q(0, 10), Q(20, 0)), color=(0, 0, 0), width=1.0)
    # 内墙 27 m
    for a, b in [((8, 0), (8, 10)), ((8, 5), (20, 5)), ((14, 0), (14, 5))]:
        page.draw_line(Q(*a), Q(*b), color=(0, 0, 1), width=0.5)
    # 圆形柱（半径 0.5 m → 面积 0.7854 m²，周长 3.1416 m），用贝塞尔曲线表示，检验曲线长度和面积
    page.draw_circle(Q(4, 5), 0.5 * 米, color=(1, 0, 0), width=0.5)
    # 房间名：优先嵌入系统中文字体（文泉驿正黑），使 pdftoppm 也能正常显示；找不到时退回内置 china-s
    字体文件 = "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc"
    字体参数 = dict(fontname="wqy", fontfile=字体文件) if os.path.exists(字体文件) else dict(fontname="china-s")
    for 名, x, y in [("卧室1", 3, 7.5), ("卧室2", 3, 2.5), ("客厅", 13, 7.5), ("厨房", 10.5, 2.5), ("浴室", 16.5, 2.5)]:
        page.insert_text(Q(x, y), 名, fontsize=9, **字体参数)
    page.draw_line(Q(0, -1.5), Q(20, -1.5), color=(0.5, 0.5, 0.5), width=0.3)  # 尺寸线 20 m（区域外不计）
    page.insert_text(Q(9.5, -1.3), "20000", fontsize=8)
    page.insert_text(pymupdf.Point(300 * pt, 280 * pt), "SCALE 1:100 @ A3", fontsize=10)
    doc.subset_fonts()  # 只嵌入用到的字形，减小文件
    doc.save(路径A3, garbage=3, deflate=True)

    # A3 图缩印到 A4（297 × 210 mm），比例变成 1:100 × 420/297
    src = pymupdf.open(路径A3)
    out = pymupdf.open()
    p4 = out.new_page(width=297 * pt, height=210 * pt)
    p4.show_pdf_page(p4.rect, src, 0)
    out.save(路径A4)


if __name__ == "__main__":
    生成dxf(os.path.join(这里, "测试平面_mm.dxf"), 0.001)
    生成dxf(os.path.join(这里, "测试平面_m.dxf"), 1.0)
    生成pdf(os.path.join(这里, "测试平面_1比100_A3.pdf"), os.path.join(这里, "测试平面_A3缩印到A4.pdf"))
    print("测试数据已生成：", 这里)
