import os, pickle, json, subprocess, time, requests, random
from datetime import datetime

# --- CONFIGURAZIONE CORE ---
TELEGRAM_BOT_TOKEN = "8736329123:AAFa9k_rtKOGQmpwXGICRu-jjdAGEUuWTZM"
TELEGRAM_CHAT_ID = "@KeygapTerminal" 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "Report_Finanziari")

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

# --- MOTORE DI INTELLIGENCE ---

def get_real_news():
    """Recupera flussi di notizie reali dai mercati globali."""
    try:
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        r = requests.get(url, timeout=10).json()
        news_data = r.get('Data', [])
        if not isinstance(news_data, list) or len(news_data) == 0:
            raise ValueError("Dati non pervenuti")
        
        return [{"time": datetime.fromtimestamp(n.get('published_on')).strftime('%H:%M'), 
                 "text": n.get('title')} for n in news_data[:8]]
    except:
        return [{"time": "LIVE", "text": "Analisi dei flussi istituzionali in corso su canali criptati."}]

def generate_market_analysis():
    """Genera un confronto CeFi vs DeFi professionale e dettagliato."""
    
    # Matrice CeFi (Centralized Finance / Istituzionale)
    cefi_intel = [
        "Le riserve di Bitcoin sugli exchange centralizzati sono ai minimi storici, segnalando una crisi di liquidità lato offerta (Supply Shock).",
        "Si osserva un incremento massiccio dell'Open Interest sui contratti future CME, indicando un posizionamento netto degli hedge fund.",
        "I desk OTC riportano volumi record di acquisto 'non-market', suggerendo un accumulo silenzioso da parte di entità corporate.",
        "I flussi verso i custodian regolamentati indicano che il capitale istituzionale sta drenando la liquidità dagli order book pubblici."
    ]
    
    # Matrice DeFi (Decentralized Finance / On-Chain)
    defi_intel = [
        "Il Total Value Locked (TVL) nei protocolli di Liquid Staking sta assorbendo la pressione di vendita, creando un pavimento di prezzo on-chain.",
        "Rilevata un'accelerazione nei volumi dei DEX su Layer-2, dove lo Smart Money sta operando strategie di arbitraggio cross-chain.",
        "L'attività di prestito (Lending) on-chain mostra tassi di utilizzo elevati per le stablecoin, segno di una leva finanziaria in accumulo.",
        "I bridge cross-chain intercettano flussi in uscita verso ecosistemi a rendimento reale (Real Yield), ignorando la volatilità degli exchange."
    ]
    
    # Sintesi Comparativa
    confronto = [
        "La divergenza è netta: la CeFi gestisce l'accumulo fisico, mentre la DeFi sta catturando la velocità della moneta tramite protocolli di rendita.",
        "Mentre gli exchange centralizzati soffrono di una mancanza di fiducia retail, le balene on-chain stanno consolidando le posizioni nei vault DeFi.",
        "Il mercato sta prezzando uno scenario di 'decoupling' dove l'infrastruttura decentralizzata sovraperforma i circuiti di regolamento classici."
    ]

    # Composizione dinamica del dossier
    return f"{random.choice(cefi_intel)} {random.choice(defi_intel)} {random.choice(confronto)}"

# --- GESTIONE SITO WEB ---

def update_index_github():
    """Rigenera index.html e archivio.html per eliminare errori 404 e aggiornare il link LIVE."""
    try:
        reports = sorted([f for f in os.listdir(REPORT_DIR) if f.endswith('.html')], reverse=True)
        ultimo_report = f"Report_Finanziari/{reports[0]}" if reports else "archivio.html"
        
        # 1. Generazione Archivio
        links_html = "".join([f'<a href="Report_Finanziari/{r}" class="report-link">> DOSSIER {r.replace("Report_Mondiale_","").replace(".html","")}</a>' for r in reports[:30]])
        
        with open(os.path.join(BASE_DIR, "archivio.html"), "w", encoding='utf-8') as f:
            f.write(f"""<!DOCTYPE html><html><head><meta charset='UTF-8'><title>KEYGAP | Archive</title>
            <link href='https://fonts.googleapis.com/css2?family=JetBrains+Mono&display=swap' rel='stylesheet'>
            <style>body{{background:#05070a;color:#fff;font-family:"JetBrains Mono";padding:40px;}} .report-link{{display:block;color:#00e5ff;text-decoration:none;margin-bottom:12px;border:1px solid #1a2332;padding:15px;border-radius:8px;}}</style>
            </head><body><h1>ARCHIVIO INTELLIGENCE</h1><hr>{links_html}</body></html>""")

        # 2. Generazione Index (Basata sulla tua dashboard)
        with open(os.path.join(BASE_DIR, "index.html"), "w", encoding='utf-8') as f:
            f.write(f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>KEYGAP | Terminal</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@700;900&family=JetBrains+Mono&display=swap" rel="stylesheet">
    <style>
        :root {{ --bg: #06080a; --card: #0d1117; --accent: #00ff88; --border: #21262d; }}
        body {{ background: var(--bg); color: #f0f2f5; font-family: 'Inter', sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}
        header {{ background: var(--card); border-bottom: 1px solid var(--border); display: grid; grid-template-columns: 250px 1fr 350px; align-items: center; padding: 10px 20px; }}
        .btn-live {{ background: #ff0055; color: #fff; text-decoration: none; padding: 10px 15px; border-radius: 6px; font-weight: 900; font-size: 0.75rem; animation: pulse 1.5s infinite; text-align: center; }}
        main {{ display: grid; grid-template-columns: 300px 1fr 380px; gap: 5px; flex-grow: 1; padding: 5px; background: #000; }}
        .panel {{ background: var(--card); border: 1px solid var(--border); display: flex; flex-direction: column; }}
        .panel-title {{ font-size: 0.65rem; color: #848e9c; padding: 8px 15px; background: rgba(255,255,255,0.02); font-family: 'JetBrains Mono'; }}
        @keyframes pulse {{ 0% {{ box-shadow: 0 0 0 0 rgba(255,0,85,0.7); }} 70% {{ box-shadow: 0 0 0 10px rgba(255,0,85,0); }} 100% {{ box-shadow: 0 0 0 0 rgba(255,0,85,0); }} }}
    </style>
</head>
<body>
<header>
    <div style="font-weight:900; font-size:1.4rem;">KEY<span style="color:var(--accent);">GAP</span></div>
    <div style="text-align:center;"><script src="https://pl28819682.effectivegatecpm.com/07/47/37/074737f2d1be0f3c0e9de0585a695fd7.js"></script></div>
    <div style="display: flex; gap: 10px; justify-content: flex-end;">
        <a href="{ultimo_report}" class="btn-live">🔴 ULTIMO DOSSIER LIVE</a>
        <a href="archivio.html" style="background:var(--accent); color:#000; text-decoration:none; padding:10px 15px; border-radius:6px; font-weight:800; font-size:0.7rem;">📂 ARCHIVIO</a>
    </div>
</header>
<main>
    <div class="panel"><div class="panel-title">MARKET_WATCH</div><iframe src="https://s.tradingview.com/embed-widget/market-overview/?colorTheme=dark" width="100%" height="100%" frameborder="0"></iframe></div>
    <div class="panel"><div class="panel-title">TERMINAL_CHART</div><iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCEUR&interval=1&theme=dark" width="100%" height="100%" frameborder="0"></iframe></div>
    <div style="display: grid; grid-template-rows: 1fr 1fr; gap: 5px;">
        <div class="panel"><div class="panel-title">INTEL_FEED</div><iframe src="https://cryptopanic.com/widgets/news/?bg_color=0d1117&link_color=00ff88&text_color=f0f2f5" width="100%" height="100%" frameborder="0"></iframe></div>
        <div class="panel"><div class="panel-title">MACRO_CALENDAR</div><iframe src="https://sslecal2.investing.com?importance=2,3&calType=day&timeZone=58&lang=5" width="100%" height="100%" frameborder="0" style="filter: invert(0.9) hue-rotate(180deg);"></iframe></div>
    </div>
</main>
</body></html>""")
    except Exception as e:
        print(f"⚠️ Errore Indici: {e}")

# --- MOTORE DI ESECUZIONE ---

def send_telegram_alert(prezzo_btc, id_report, scenario, analisi, news_list):
    """Invia il dossier professionale al canale Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    notizie_testo = ""
    for n in news_list[:3]:
        notizie_testo += f"⚠️ {n['text']}\n"

    msg = f"""🚨 <b>[{scenario}]</b> 🚨

📊 <b>ID Sincronizzazione:</b> #KG-{id_report}
🕒 <b>Analisi delle:</b> {datetime.now().strftime('%H:%M CET')}

⬛️ <b>CONFRONTO CeFi vs DeFi</b>
{analisi}

⬛️ <b>LIVE NEWS FEED</b>
{notizie_testo}

💰 <b>VALORE BTC:</b> {prezzo_btc}

⚡️ <b>LEGGI IL DOSSIER COMPLETO SUL TERMINALE:</b>
👉 <a href="https://giampierodeluca676-lgtm.github.io/">Accedi ai Dati Decriptati</a>
"""
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "HTML", "disable_web_page_preview": False})
    except: pass

def run_update():
    """Esegue il ciclo completo di aggiornamento."""
    try:
        # 1. Recupero dati reali
        res = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR", timeout=5).json()
        prezzo_btc = f"€ {res.get('EUR', 60000.0):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        notizie = get_real_news()
        report_id = random.randint(1000, 9999)
        analisi_dinamica = generate_market_analysis()
        scenario = random.choice(["INSTITUTIONAL ROTATION", "LIQUIDITY COMPRESSION", "NETWORK BREAKOUT"])

        # 2. Generazione HTML Dossier (Dettagliato e Professionale)
        news_html = "".join([f"<p style='color:#00ff88;'>[{n['time']}] > {n['text']}</p>" for n in notizie])
        
        html_content = f"""
        <!DOCTYPE html><html><head><meta charset='UTF-8'><style>
        body{{background:#020408; color:#a1b2c3; font-family:"JetBrains Mono",monospace; padding:40px; line-height:1.8;}}
        .terminal{{max-width:850px; margin:0 auto; border:1px solid #1a2332; padding:45px; background:#060913;}}
        h1{{color:#00e5ff; font-size:1.3rem; border-bottom:1px solid #1a2332; padding-bottom:10px;}}
        .analysis-box{{background:#03050a; padding:25px; border-left:4px solid #00ff88; color:#eee; margin:20px 0;}}
        </style></head><body><div class='terminal'>
        <h1>KEYGAP // DOSSIER INTELLIGENCE #{report_id}</h1>
        <p>SCENARIO RILEVATO: <strong>[{scenario}]</strong></p>
        <div class='analysis-box'>
            <strong>ANALISI TECNICA CEFI vs DEFI:</strong><br><br>
            {analisi_dinamica}
        </div>
        <p style='font-size:1.8rem; color:#fff;'>BTC VALUE: {prezzo_btc}</p>
        <hr style='border:1px solid #1a2332;'>
        <h3>INTERCETTAZIONI GLOBALI (RAW DATA):</h3>
        {news_html}
        <p style='margin-top:40px; font-size:0.7rem; color:#445;'>KEYGAP ADVANTAGE CORE // DOCUMENTO DECRIPTATO</p>
        </div></body></html>"""

        # 3. Salvataggio e Sincronizzazione Git
        filename = f"Report_Mondiale_{datetime.now().strftime('%d_%m_%Y_%H_%M')}.html"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, "w", encoding='utf-8') as f: f.write(html_content)
        
        update_index_github()
        
        subprocess.run(["git", "add", "."], cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"📊 Dossier {report_id}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main", "--force"], cwd=BASE_DIR)
        
        print(f"✅ [KEYGAP] Sincronizzazione Dossier {report_id} completata.")
        send_telegram_alert(prezzo_btc, report_id, scenario, analisi_dinamica, notizie)

    except Exception as e:
        print(f"❌ Errore critico: {e}")

if __name__ == "__main__":
    print("🚀 KEYGAP_ADVANTAGE CORE - Generatore Dossier Attivo.")
    while True:
        run_update()
        time.sleep(1800)