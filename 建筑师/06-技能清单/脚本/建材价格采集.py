#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
建材价格采集.py —— 按《建材价格数据库.csv》里的产品页 URL，逐条用 curl 抓取零售商公开页面，
尝试从静态 HTML 中提取含 GST 的零售标价，并写出一份新的、带采集日期的 CSV。

用法（在知识库根目录「建筑师/」下运行）：
    python3 -I 06-技能清单/脚本/建材价格采集.py \
        --input  03-成本与省钱/建材价格数据库.csv \
        --output 03-成本与省钱/建材价格数据库_新.csv \
        --date   2027-02-01

    --dry-run       只检查 robots.txt 和列出将要请求的 URL，不抓产品页
    --delay 3       每次请求间隔秒数（默认 3，最低 2）
    --max 150       本次最多请求数（默认 150）

原则（必须遵守）：
  1. 只抓公开页面；遵守 robots.txt；不绕过 Cloudflare 等人机验证；不调用网站内部价格 API。
  2. 取不到价格就写「取不到」和原因，绝不填估计值。
  3. 人工核对：脚本取到的价格要抽查几条，在浏览器里打开同一 URL 对照（含 GST、单位、门店）。

提取顺序：JSON-LD offers.price → meta itemprop/og 价格 → __NEXT_DATA__ 中的 price 字段。
依赖：Python 3 标准库 + 系统 curl（走环境里的 HTTPS 代理设置）。
"""
import argparse
import csv
import json
import re
import subprocess
import sys
import time
import urllib.robotparser
from urllib.parse import urlparse

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/130.0 Safari/537.36")

PRICE_COL = "价格_含GST_AUD"
STATUS_COL = "采集状态"
NOTE_COL = "备注"
DATE_COL = "采集日期"
URL_COL = "产品页URL"


def curl(url, timeout=30):
    """返回 (http_code, final_url, body_text)。失败时 http_code='000'。"""
    marker = "\n__CURL_META__"
    cmd = ["curl", "-sL", "-A", UA, "--max-time", str(timeout),
           "-w", marker + "%{http_code} %{url_effective}", url]
    try:
        out = subprocess.run(cmd, capture_output=True, timeout=timeout + 10).stdout
    except subprocess.TimeoutExpired:
        return "000", url, ""
    text = out.decode("utf-8", errors="replace")
    body, _, meta = text.rpartition(marker)
    parts = meta.split(" ", 1)
    code = parts[0] if parts else "000"
    final = parts[1] if len(parts) > 1 else url
    return code, final, body


_robots_cache = {}


def robots_allows(url, counter):
    host = urlparse(url).scheme + "://" + urlparse(url).netloc
    if host not in _robots_cache:
        code, _, body = curl(host + "/robots.txt")
        counter[0] += 1
        rp = urllib.robotparser.RobotFileParser()
        if code == "200" and "Just a moment" not in body:
            rp.parse(body.splitlines())
            _robots_cache[host] = rp
        else:
            _robots_cache[host] = None  # 取不到 robots：视为网站拦截，不抓
        time.sleep(2)
    rp = _robots_cache[host]
    if rp is None:
        return False, "robots.txt 取不到（多为人机验证拦截）"
    return rp.can_fetch("*", url), "robots.txt 不允许" if not rp.can_fetch("*", url) else ""


def _walk_for_price(obj):
    """在 JSON 里找 offers.price / price 数值。"""
    if isinstance(obj, dict):
        offers = obj.get("offers")
        if offers:
            for o in (offers if isinstance(offers, list) else [offers]):
                if isinstance(o, dict) and o.get("price") not in (None, ""):
                    return str(o.get("price")), o.get("priceCurrency", "")
        for k, v in obj.items():
            if k.lower() == "price" and isinstance(v, (int, float, str)) and re.fullmatch(r"\d+(\.\d+)?", str(v)):
                return str(v), ""
            r = _walk_for_price(v)
            if r:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = _walk_for_price(v)
            if r:
                return r
    return None


def extract_price(html):
    # 1) JSON-LD
    for m in re.finditer(r'<script[^>]+application/ld\+json[^>]*>(.*?)</script>', html, re.S | re.I):
        try:
            r = _walk_for_price(json.loads(m.group(1)))
            if r:
                return r[0], "JSON-LD"
        except ValueError:
            pass
    # 2) meta 标签
    m = re.search(r'<meta[^>]+(?:itemprop="price"|property="product:price:amount")[^>]+content="([\d.]+)"', html, re.I)
    if m:
        return m.group(1), "meta"
    # 3) __NEXT_DATA__
    m = re.search(r'<script[^>]+id="__NEXT_DATA__"[^>]*>(.*?)</script>', html, re.S)
    if m:
        try:
            r = _walk_for_price(json.loads(m.group(1)))
            if r:
                return r[0], "__NEXT_DATA__"
        except ValueError:
            pass
    return None, ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--date", required=True, help="采集日期 YYYY-MM-DD")
    ap.add_argument("--delay", type=float, default=3.0)
    ap.add_argument("--max", type=int, default=150)
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    delay = max(a.delay, 2.0)

    with open(a.input, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    fields = list(rows[0].keys()) if rows else []
    counter = [0]

    for row in rows:
        url = (row.get(URL_COL) or "").strip()
        if not url.startswith("http"):
            continue
        if counter[0] >= a.max:
            print("已达请求上限，停止。", file=sys.stderr)
            break
        ok, why = robots_allows(url, counter)
        if not ok:
            row[STATUS_COL], row[NOTE_COL] = "取不到", why
            row[PRICE_COL], row[DATE_COL] = "", a.date
            print("SKIP", url, why)
            continue
        if a.dry_run:
            print("WOULD FETCH", url)
            continue
        code, final, body = curl(url)
        counter[0] += 1
        row[DATE_COL] = a.date
        if code != "200":
            row[PRICE_COL] = ""
            row[STATUS_COL] = "取不到"
            row[NOTE_COL] = f"HTTP {code}" + ("（Cloudflare 人机验证）" if "Just a moment" in body else "")
        elif urlparse(final).netloc != urlparse(url).netloc:
            row[PRICE_COL], row[STATUS_COL] = "", "取不到"
            row[NOTE_COL] = f"跳转到 {urlparse(final).netloc}"
        else:
            price, how = extract_price(body)
            if price:
                row[PRICE_COL], row[STATUS_COL] = price, "已取得（待人工抽查）"
                row[NOTE_COL] = f"来源：页面{how}；须在浏览器核对是否含 GST、单位与门店"
            else:
                row[PRICE_COL], row[STATUS_COL] = "", "取不到"
                row[NOTE_COL] = "静态 HTML 和嵌入 JSON 中没有价格（价格由前端脚本加载）"
        print(row[STATUS_COL], row[PRICE_COL], url)
        time.sleep(delay)

    with open(a.output, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    print(f"完成：共发出 {counter[0]} 次请求，写入 {a.output}")


if __name__ == "__main__":
    main()
