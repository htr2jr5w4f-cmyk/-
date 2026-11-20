"""把 Markdown 报告转成 PDF（中文用文泉驿正黑/系统中文字体）。
用法: python3 md转pdf.py 输入.md 输出.pdf
依赖: pandoc, Chromium（无头模式打印 PDF）
"""
import subprocess, sys, pathlib
import shutil
CHROME = shutil.which('chromium') or '/opt/pw-browsers/chromium'

CSS = """
@page { size: A4; margin: 18mm 16mm 18mm 16mm; }
body { font-family: 'WenQuanYi Zen Hei','Noto Sans CJK SC','Microsoft YaHei',sans-serif;
       font-size: 10.5pt; line-height: 1.6; color: #1a1a1a; }
h1 { font-size: 20pt; border-bottom: 2px solid #2b5797; padding-bottom: 4px; color:#2b5797; }
h2 { font-size: 14.5pt; color: #2b5797; margin-top: 18px; border-left: 4px solid #2b5797; padding-left: 8px; }
h3 { font-size: 12pt; margin-top: 12px; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9pt; page-break-inside: auto; }
tr { page-break-inside: avoid; }
th, td { border: 1px solid #999; padding: 4px 6px; vertical-align: top; text-align: left; }
th { background: #e8eef7; }
code { font-size: 9pt; background:#f3f3f3; padding: 0 2px; word-break: break-all; }
a { color: #2b5797; word-break: break-all; }
.pagebreak { page-break-after: always; }
blockquote { border-left: 3px solid #ccc; margin-left: 0; padding-left: 10px; color: #444; }
"""

def main(src, dst):
    html = subprocess.run(["pandoc", src, "-f", "gfm", "-t", "html5", "--standalone",
                           "--metadata", "title= ", "--css", "/dev/null"],
                          capture_output=True, text=True, check=True).stdout
    html = html.replace("</head>", f"<style>{CSS}</style></head>")
    tmp = pathlib.Path(dst).with_suffix(".tmp.html")
    tmp.write_text(html, encoding="utf-8")
    subprocess.run([CHROME, "--headless", "--no-sandbox", "--disable-gpu",
                    "--no-pdf-header-footer", f"--print-to-pdf={pathlib.Path(dst).resolve()}",
                    tmp.resolve().as_uri()], check=True, capture_output=True)
    tmp.unlink()

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
