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
LATEST_REPORT_JSON = ROOT / "latest_report.json"
LATEST_REPORT_HTML = ROOT / "latest_report.html"
ARCHIVIO = ROOT / "archivio.html"

# --- CONFIGURAZIONE ---
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
        p = data["current_price"]
        return {
            "id": random.randint(10000, 99999),
            "updated_at": now_it(),
            "price_eur": p,
            "change": round(data["price_change_percentage_24h"], 2),
            "high": data["high_24h"],
            "low": data["low_24h"],
            "support": round(p * 0.982, 2),
            "resistance": round(p * 1.021, 2),
            "bias": "Rialzista" if data["price_change_percentage_24h"] > 0 else "Ribassista"
        }
    except: return None

def write_professional_report(report):
    # TEMPLATE PROFESSIONALE LUNGO (Stile Report 4018)
    html = f"""<!DOCTYPE html><html lang="it"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
    <title>Keygap Intelligence Report #{report['id']}</title>{AD_POPUNDER}
    <style>
        :root {{ --bg:#060b14; --panel:#0e1728; --accent:#6ee7ff; --text:#edf4ff; }}
        body {{ background:var(--bg); color:var(--text); font-family:sans-serif; line-height:1.6; padding:20px; margin:0; }}
        .container {{ max-width:800px; margin:0 auto; }}
        .header {{ border-left:4px solid var(--accent); padding-left:20px; margin-bottom:40px; }}
        .card {{ background:var(--panel); padding:25px; border-radius:15px; margin-bottom:20px; border:1px solid rgba(255,255,255,0.05); }}
        .grid {{ display:grid; grid-template-columns: 1fr 1fr; gap:15px; }}
        .label {{ color:#98abc7; font-size:12px; text-transform:uppercase; }}
        .value {{ font-size:22px; font-weight:bold; color:var(--accent); }}
        .status {{ padding:5px 15px; border-radius:20px; font-size:14px; background:rgba(110,231,255,0.1); }}
    </style></head><body><div class="container">
        <div class="header">
            <p class="label">Market Intelligence Terminal</p>
            <h1>Dossier Operativo #{report['id']}</h1>
            <p>Data emissione: {report['updated_at']}</p>
        </div>
        <div class="card">
            <div class="label">Quotazione Attuale BTC/EUR</div>
            <div style="font-size:40px; font-weight:bold;">{fmt_eur(report['price_eur'])}</div>
            <span class="status">Trend: {report['bias']} ({report['change']}%)</span>
        </div>
        <div class="grid">
            <div class="card"><div class="label">Supporto Critico</div><div class="value">{fmt_eur(report['support'])}</div></div>
            <div class="card"><div class="label">Resistenza Target</div><div class="value">{fmt_eur(report['resistance'])}</div></div>
        </div>
        <div class="card">
            <h2>Analisi Tecnica e Sentiment</h2>
            <p>Il mercato presenta una struttura {report['bias'].lower()}. Le metriche on-chain indicano un consolidamento volumetrico nell'area dei {fmt_eur(report['price_eur'])}. 
            La tenuta del supporto a {fmt_eur(report['support'])} è fondamentale per evitare una capitolazione verso i minimi settimanali. 
            In caso di breakout sopra i {fmt_eur(report['resistance'])}, il prossimo target tecnico è posizionato significativamente più in alto.</p>
            <p><i>Nota: Questo report è generato automaticamente dal terminale Keygap AdVantage Elite per scopi informativi.</i></p>
        </div>
        <div style="text-align:center; margin-top:40px;">
            <a href="{SITE_URL}" style="color:var(--accent); text-decoration:none;">&larr; Torna alla Dashboard Terminal</a>
        </div>
    </div></body></html>"""
    
    filename = f"Report_Mondiale_{datetime.now().strftime('%d_%m_%Y_%H_%M')}.html"
    LATEST_REPORT_HTML.write_text(html, encoding="utf-8")
    (REPORTS_DIR / filename).write_text(html, encoding="utf-8")
    return filename

def run_cycle():
    REPORTS_DIR.mkdir(exist_ok=True)
    report = fetch_btc()
    if not report: return
    
    # 1. Scrittura Report Professionale
    rep_file = write_professional_report(report)
    LATEST_REPORT_JSON.write_text(json.dumps(report), encoding="utf-8")
    
    # 2. Caricamento su GitHub (Sblocco 404)
    if (ROOT / ".git").exists():
        subprocess.run(["git", "add", "."], cwd=ROOT)
        subprocess.run(["git", "commit", "-m", f"Elite Report {report['id']}"], cwd=ROOT)
        subprocess.run(["git", "push", "-f", "origin", "main"], cwd=ROOT)
        print(f"✅ Report {report['id']} online")

    # 3. Notifica Telegram
    msg = f"⚡ KEYGAP ELITE DOSSIER #{report['id']}\n\n💰 BTC: {fmt_eur(report['price_eur'])}\n📊 Trend: {report['bias']}\n\nAnalisi completa disponibile online:\n🔗 {SITE_URL}"
    requests.post(f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage", data={"chat_id": TELEGRAM_CHAT_ID, "text": msg})

if __name__ == "__main__":
    while True:
        try: run_cycle()
        except Exception as e: print(f"Errore: {e}")
        time.sleep(1800)