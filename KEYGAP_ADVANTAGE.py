#!/usr/bin/env python3
import json
import os
import pickle
import random
import subprocess
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET
import requests

ROOT = Path(__file__).resolve().parent
REPORTS_DIR = ROOT / "Report_Finanziari"
LATEST_NEWS = ROOT / "latest_news.json"
LATEST_REPORT_JSON = ROOT / "latest_report.json"
LATEST_REPORT_HTML = ROOT / "latest_report.html"
ARCHIVIO = ROOT / "archivio.html"
USED_NEWS = ROOT / "used_news.json"

# LINK CORRETTO PER I TUOI CLIENTI FACEBOOK
SITE_URL = "https://keygap-official.github.io/https-keygap-official.github.io/"

TELEGRAM_BOT_TOKEN = "8736329123:AAFa9k_rtKOGQmpwXGICRu-jjdAGEUuWTZM"
TELEGRAM_CHAT_ID = "@KeygapTerminal"

AD_POPUNDER = """
<script src="https://pl28819682.profitablecpmratenetwork.com/07/47/37/074737f2d1be0f3c0e9de0585a695fd7.js"></script>
"""

def fmt_eur(v):
    return f"€ {v:,.0f}".replace(",", ".")

def now_it():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def filename_stamp():
    return datetime.now().strftime("%d_%m_%Y_%H_%M")

def fetch_btc():
    r = requests.get("https://api.coingecko.com/api/v3/coins/markets", params={"vs_currency": "eur", "ids": "bitcoin", "price_change_percentage": "24h"}, timeout=20)
    r.raise_for_status()
    data = r.json()[0]
    price = float(data.get("current_price") or 0)
    high = float(data.get("high_24h") or price)
    low = float(data.get("low_24h") or price)
    change = float(data.get("price_change_percentage_24h") or 0)
    span = max(high - low, max(price * 0.002, 1))
    support = round(max(low, price - span * 0.25), 2)
    resistance = round(max(price + span * 0.25, high if high > price else price * 1.0025), 2)
    bias = "rialzista" if change > 1 else "ribassista" if change < -1 else "neutrale"
    return {
        "id": random.randint(10000, 99999), "updated_at": now_it(), "price_eur": round(price, 2),
        "change_24h_pct": round(change, 2), "high_24h_eur": round(high, 2), "low_24h_eur": round(low, 2),
        "support_eur": round(support, 2), "resistance_eur": round(resistance, 2), "bias": bias,
        "volatility": "alta" if abs(change) > 3 else "media",
        "quick_read": f"Prezzo in equilibrio. {fmt_eur(support)} supporto chiave, {fmt_eur(resistance)} resistenza utile."
    }

def fetch_news():
    r = requests.get("https://news.google.com/rss/search?q=bitcoin+OR+crypto+when:1d&hl=it&gl=IT&ceid=IT:it", timeout=20)
    root = ET.fromstring(r.text)
    items = []
    for item in root.findall(".//item")[:12]:
        title = item.findtext("title").strip()
        items.append({"title": title, "link": item.findtext("link"), "source": "Google News", "published_at": item.findtext("pubDate")})
    return {"updated_at": now_it(), "items": items}

def write_latest_report_html(report):
    html = f"""<!DOCTYPE html><html lang="it"><head><meta charset="UTF-8">{AD_POPUNDER}<style>body{{background:#060b14;color:#edf4ff;font-family:sans-serif;padding:20px;}} .card{{background:#0e1728;padding:20px;border-radius:15px;margin-bottom:20px;}}</style></head>
    <body><div class="card"><h1>BTC Live {fmt_eur(report["price_eur"])}</h1><p>Aggiornato: {report["updated_at"]}</p><p>Bias: {report["bias"]}</p><a href="{SITE_URL}" style="color:#6ee7ff;">Torna alla Dashboard</a></div></body></html>"""
    LATEST_REPORT_HTML.write_text(html, encoding="utf-8")
    (REPORTS_DIR / f"Report_Mondiale_{filename_stamp()}.html").write_text(html, encoding="utf-8")

def rebuild_archivio():
    files = sorted(REPORTS_DIR.glob("*.html"), reverse=True)
    items = "\n".join([f'<li><a href="Report_Finanziari/{f.name}">{f.name}</a></li>' for f in files[:100]])
    ARCHIVIO.write_text(f"<html><body><ul>{items}</ul></body></html>", encoding="utf-8")

def send_telegram(report, news):
    text = f"⚡ KEYGAP UPDATE\nBTC: {fmt_eur(report['price_eur'])}\nBias: {report['bias']}\n\nDashboard: {SITE_URL}"
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", data={"chat_id": TELEGRAM_CHAT_ID, "text": text})

def git_publish(report_id):
    if not (ROOT / ".git").exists(): return
    with open(ROOT / ".nojekyll", "w") as f: f.write("")
    subprocess.run(["git", "add", "."], cwd=ROOT)
    subprocess.run(["git", "commit", "-m", f"Update {report_id}"], cwd=ROOT)
    subprocess.run(["git", "push", "-f", "origin", "main"], cwd=ROOT)

def run_cycle():
    REPORTS_DIR.mkdir(exist_ok=True)
    report = fetch_btc()
    news = fetch_news()
    write_latest_report_html(report)
    LATEST_REPORT_JSON.write_text(json.dumps(report, indent=2), encoding="utf-8")
    LATEST_NEWS.write_text(json.dumps(news, indent=2), encoding="utf-8")
    rebuild_archivio()
    send_telegram(report, news)
    git_publish(report["id"])

if __name__ == "__main__":
    import time
    while True:
        try: run_cycle()
        except Exception as e: print(f"Errore: {e}")
        time.sleep(1800)