"""为每个知识库文件夹生成 索引.md：从各文件的「## 摘要」提取首段，并读取元数据行中的状态。
用法: python3 生成索引.py <文件夹>"""
import sys, pathlib, re
d = pathlib.Path(sys.argv[1])
rows = []
for f in sorted(d.iterdir()):
    if f.name == "索引.md" or f.is_dir(): continue
    if f.suffix != ".md":
        rows.append((f.name, "（非 Markdown 文件，见同目录说明文件）", "—")); continue
    t = f.read_text(encoding="utf-8")
    m = re.search(r"## 摘要\s*\n+(.+?)(?:\n\s*\n|\n#)", t, re.S)
    summ = re.sub(r"\s+", " ", m.group(1)).strip() if m else "（无摘要）"
    summ = re.sub(r"\[S\d+\]", "", summ)
    if len(summ) > 160: summ = summ[:158] + "…"
    st = re.search(r"状态[：:]\s*([^｜|\n]+)", t)
    rows.append((f.name, summ.replace("|", "/"), st.group(1).strip() if st else "—"))
out = [f"# {d.name} 索引", "", "## 摘要", f"本文件夹共 {len(rows)} 个文件。下表列出每个文件的内容摘要和核实状态（「部分待证实」表示部分数字未能打开官方原文核对，见文件内标记）。", "",
       "| 文件 | 内容摘要 | 状态 |", "|---|---|---|"]
out += [f"| [{n}]({n.replace(' ', '%20')}) | {s} | {st} |" for n, s, st in rows]
(d / "索引.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(d, len(rows))
