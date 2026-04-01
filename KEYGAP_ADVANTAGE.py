#!/usr/bin/env python3
import json
import os
import random
import subprocess
from datetime import datetime
from pathlib import Path
from xml.etree import ElementTree as ET
import requests
import time

ROOT = Path(__file__).resolve().parent
REPORTS_DIR = ROOT / "Report_Finanziari"
LATEST_NEWS = ROOT / "latest_news.json"
LATEST_REPORT_JSON = ROOT / "latest_report.json"
LATEST_REPORT_HTML = ROOT / "latest_report.html"
ARCHIVIO = ROOT / "archivio.html"
USED_NEWS = ROOT / "used_news.json"

# LINK CORRETTO PER IL TUO REPOSITORY ATTUALE
SITE_URL = "https://keygap-official.github.io/https-keygap-official.github.io/"

TELEGRAM_BOT_TOKEN = "8736329123:AAFa9k_rtKOGQmpwXGICRu-jjdAGEUuWTZM"
TELEGRAM_CHAT_ID = "@KeygapTerminal"

AD_POPUNDER = '<script src="https://pl28819682.profitablecpmratenetwork.com/07/47/37/074737f2d1be0f3c0e9de0585a695fd7.js"></script>'

def fmt_eur(v):
    return f"€ {v:,.0f}".replace(",", ".")

def now_it():
    return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def fetch_btc():
    try:
        r = requests.get("https://api.coingecko.com/api/v3/coins/markets", params={"vs_currency": "eur", "ids": "bitcoin", "price_change_percentage": "24h"}, timeout=20)
        data = r.json()[0]
        price = data["current_price"]
        return {
            "id": random.randint(1000, 9999),
            "updated_at": now_it(),
            "price_eur": price,
            "change_24h_pct": data["price_change_percentage_24h"],
            "support_eur": price * 0.98,
            "resistance_eur": price * 1.02,
            "bias": "neutrale",
            "quick_read": f"Market live a {fmt_eur(price)}."
        }
    except: return None

def run_cycle():
    REPORTS_DIR.mkdir(exist_ok=True)
    report = fetch_btc()
    if not report: 
        print("Impossibile recuperare dati BTC")
        return
    
    # Salvataggio dati locali
    LATEST_REPORT_JSON.write_text(json.dumps(report), encoding="utf-8")
    LATEST_REPORT_HTML.write_text(f"<html><body><h1>Report {report['id']}</h1>{AD_POPUNDER}</body></html>", encoding="utf-8")
    
    # Push su GitHub
    if (ROOT / ".git").exists():
        with open(ROOT / ".nojekyll", "w") as f: f.write("")
        subprocess.run(["git", "add", "."], cwd=ROOT)
        subprocess.run(["git", "commit", "-m", f"Fix 404 update {report['id']}"], cwd=ROOT)
        subprocess.run(["git", "push", "-f", "origin", "main"], cwd=ROOT)
        print(f"✅ File inviati a GitHub per il report {report['id']}")

    # Messaggio Telegram
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", 
                  data={"chat_id": TELEGRAM_CHAT_ID, "text": f"🚀 Keygap Online!\nBTC: {fmt_eur(report['price_eur'])}\nLink: {SITE_URL}"})

if __name__ == "__main__":
    print("Avvio ciclo automatico (30 min)...")
    while True:
        try:
            run_cycle()
        except Exception as e:
            print(f"Errore nel ciclo: {e}")
        time.sleep(1800)