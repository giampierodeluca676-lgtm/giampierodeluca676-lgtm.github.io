import os, pickle, json, subprocess, time, requests, random
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# --- SISTEMA DI IDENTIFICAZIONE PROCESSO ---
with open("KEYGAP_ADVANTAGE.pid", "w") as f:
    f.write(str(os.getpid()))

# --- CONFIGURAZIONE CORE ---
SCOPES = ['https://www.googleapis.com/auth/blogger']
BLOG_ID = '2744764892823107807'
SITO_MONETIZZATO = 'https://giampierodeluca676-lgtm.github.io/'

# --- CONFIGURAZIONE TELEGRAM ---
TELEGRAM_BOT_TOKEN = "8736329123:AAFa9k_rtKOGQmpwXGICRu-jjdAGEUuWTZM"
TELEGRAM_CHAT_ID = "@KeygapTerminal"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "Report_Finanziari")

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

# --- MOTORE DI AUTENTICAZIONE BLOGGER ---
def get_service():
    creds = None
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
    return build('blogger', 'v3', credentials=creds)

# --- MOTORE DI INTELLIGENCE DINAMICA ---
def generate_pro_analysis():
    cefi_intel = [
        "Le riserve degli exchange centralizzati (CeFi) mostrano un drenaggio costante verso i cold wallet istituzionali.",
        "Si osserva un consolidamento dei volumi sugli order book CeFi, suggerendo una fase di accumulo silenzioso.",
        "I flussi verso le piattaforme regolamentate segnalano un repricing del rischio da parte dei grandi fondi.",
        "Rilevata una riduzione dello spread di arbitraggio tra i principali exchange centralizzati Tier-1."
    ]
    defi_intel = [
        "In ambito DeFi, il Total Value Locked (TVL) on-chain sta migrando verso protocolli di rendimento reale (Real Yield).",
        "L'attività sui DEX mostra un'impennata dei volumi legata a manovre di whale che operano fuori dai radar centralizzati.",
        "I protocolli di lending decentralizzato stanno assorbendo la volatilità tramite pool di liquidità automatizzate.",
        "Si intercettano flussi massicci verso i bridge cross-chain, indicando una riallocazione tattica di capitale."
    ]
    confronto = [
        "La convergenza tra questi due mondi sta creando un'inefficienza strutturale che favorisce lo Smart Money.",
        "Mentre la CeFi gestisce l'on-ramp istituzionale, la DeFi sta catturando il valore tramite protocolli di staking avanzato.",
        "La divergenza rilevata indica che il mercato sta spostando la fiducia verso l'infrastruttura decentralizzata resiliente."
    ]
    return f"{random.choice(cefi_intel)} {random.choice(defi_intel)} {random.choice(confronto)}"

def get_real_news():
    try:
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        r = requests.get(url, timeout=5).json()
        news_list = []
        for item in r.get('Data', [])[:6]:
            t = datetime.fromtimestamp(item['published_on']).strftime('%H:%M')
            news_list.append({"time": t, "text": item['title'], "link": item['url']})
        return news_list
    except:
        return [{"time": "INTEL", "text": "Analisi flussi istituzionali in corso.", "link": "#"}]

# --- GESTIONE SITO, ARCHIVIO & RESPONSIVE DESIGN ---
def update_index_github():
    try:
        all_files = sorted([f for f in os.listdir(REPORT_DIR) if f.endswith('.html')], reverse=True)
        if len(all_files) > 50:
            for old_file in all_files[50:]:
                os.remove(os.path.join(REPORT_DIR, old_file))
            all_files = all_files[:50]

        ultimo_report = f"Report_Finanziari/{all_files[0]}" if all_files else "archivio.html"
        
        # FIX ARCHIVIO: Aggiunto 'word-break: break-word;' per evitare l'uscita dai rettangoli
        links_html = "".join([f'<a href="Report_Finanziari/{r}" style="display:block; color:#00e5ff; text-decoration:none; margin-bottom:15px; border:1px solid #1a2332; padding:20px; border-radius:12px; font-size:1.1rem; background:#0d1117; word-break: break-word; box-sizing: border-box; line-height: 1.4;">> KEYGAP DOSSIER {r.replace("Report_Mondiale_","").replace(".html","")}</a>' for r in all_files])
        
        with open(os.path.join(BASE_DIR, "archivio.html"), "w", encoding='utf-8') as f:
            f.write(f"<html><meta name='viewport' content='width=device-width, initial-scale=1.0'><body style='background:#05070a; color:#fff; font-family:monospace; padding:5%; box-sizing: border-box;'><h1>KEYGAP ARCHIVIO</h1><hr style='border:1px solid #1a2332; margin-bottom: 20px;'>{links_html}</body></html>")

        # FIX INDEX: Aggiunto Footer con data e ora fluida (Javascript)
        index_content = f"""<!DOCTYPE html><html><head><meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Keygap Terminal</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono:wght@500&display=swap" rel="stylesheet">
        <style>
            body {{ background: #06080a; color: #f0f2f5; font-family: 'Inter', sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}
            header {{ background: #0d1117; border-bottom: 2px solid #21262d; display: flex; justify-content: space-between; align-items: center; padding: 15px 30px; flex-wrap: wrap; gap: 15px; }}
            .logo {{ font-weight: 900; font-size: 1.8rem; letter-spacing: -1px; }}
            .btn-container {{ display: flex; gap: 15px; }}
            .btn-live {{ background: #ff0055; color: #fff; text-decoration: none; padding: 12px 25px; border-radius: 8px; font-weight: 900; font-size: 1rem; animation: pulse 1.5s infinite; text-align: center; border: 2px solid #ff0055; text-transform: uppercase; }}
            .btn-archive {{ background: #00ff88; color: #000; text-decoration: none; padding: 12px 25px; border-radius: 8px; font-weight: 900; font-size: 1rem; text-align: center; text-transform: uppercase; }}
            main {{ display: grid; grid-template-columns: 350px 1fr 400px; gap: 8px; flex-grow: 1; padding: 8px; background: #000; overflow: hidden; }}
            .panel {{ background: #0d1117; border: 1px solid #21262d; display: flex; flex-direction: column; overflow: hidden; }}
            .panel-title {{ font-size: 0.85rem; text-transform: uppercase; color: #848e9c; padding: 10px 15px; background: rgba(255,255,255,0.02); font-family: 'JetBrains Mono'; border-bottom: 1px solid #21262d; }}
            iframe {{ flex-grow: 1; border: none; width: 100%; height: 100%; }}
            .grid-sidebar {{ display: flex; flex-direction: column; gap: 8px; }}
            footer {{ background: #0d1117; border-top: 2px solid #21262d; text-align: center; padding: 10px; font-family: 'JetBrains Mono', monospace; color: #00ff88; font-size: 0.85rem; }}
            @keyframes pulse {{ 0% {{ box-shadow: 0 0 0 0 rgba(255,0,85,0.7); }} 70% {{ box-shadow: 0 0 0 15px rgba(255,0,85,0); }} 100% {{ box-shadow: 0 0 0 0 rgba(255,0,85,0); }} }}
            
            @media (max-width: 1024px) {{
                body {{ height: auto; overflow: visible; }}
                header {{ flex-direction: column; justify-content: center; text-align: center; padding: 15px; }}
                .btn-container {{ width: 100%; flex-direction: column; }}
                main {{ display: flex; flex-direction: column; overflow: visible; padding: 10px; gap: 15px; }}
                .panel {{ min-height: 450px; }}
                .grid-sidebar {{ display: contents; }}
            }}
        </style>
        </head><body><header>
            <div class="logo">KEY<span style="color:#00ff88;">GAP</span></div>
            <div style="text-align:center; max-width:100%; overflow:hidden;"><script src="https://pl28819682.effectivegatecpm.com/07/47/37/074737f2d1be0f3c0e9de0585a695fd7.js"></script></div>
            <div class="btn-container">
                <a href="{ultimo_report}" class="btn-live">🔴 DOSSIER LIVE</a>
                <a href="archivio.html" class="btn-archive">📂 ARCHIVIO</a>
            </div>
        </header><main>
            <div class="panel"><div class="panel-title">MARKET_WATCH</div><iframe src="https://s.tradingview.com/embed-widget/market-overview/?colorTheme=dark" frameborder="0"></iframe></div>
            <div class="panel"><div class="panel-title">TERMINAL_CHART</div><iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCEUR&interval=1&theme=dark" frameborder="0"></iframe></div>
            <div class="grid-sidebar">
                <div class="panel"><div class="panel-title">NEWS_FEED</div><iframe src="https://cryptopanic.com/widgets/news/?bg_color=0d1117&link_color=00ff88&text_color=f0f2f5" frameborder="0"></iframe></div>
                <div class="panel"><div class="panel-title">MACRO_CALENDAR</div><iframe src="https://sslecal2.investing.com?importance=2,3&calType=day&timeZone=58&lang=5" frameborder="0" style="filter: invert(0.9) hue-rotate(180deg);"></iframe></div>
            </div></main>
            <footer>
                KEYGAP TERMINAL ACTIVE // <span id="clock"></span>
            </footer>
            <script>
                setInterval(function() {{
                    var now = new Date();
                    document.getElementById('clock').innerHTML = now.toLocaleDateString('it-IT') + ' - ' + now.toLocaleTimeString('it-IT');
                }}, 1000);
            </script>
        </body></html>"""
        
        with open(os.path.join(BASE_DIR, "index.html"), "w", encoding='utf-8') as f:
            f.write(index_content)
    except Exception as e:
        print(f"⚠️ Errore Indici: {e}")

# --- INVIO TELEGRAM ---
def send_telegram_alert(prezzo_btc, id_report, scenario, analisi):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    msg = f"🚨 <b>[{scenario}]</b> 🚨\n\n📊 <b>ID:</b> #KG-{id_report}\n🕒 <b>LIVE:</b> {datetime.now().strftime('%H:%M CET')}\n\n⬛️ <b>VALUTAZIONE CEFI vs DEFI</b>\n{analisi}\n\n💰 <b>VALUE:</b> {prezzo_btc}\n\n⚡️ <b>DOSSIER COMPLETO:</b>\n👉 <a href='{SITO_MONETIZZATO}'>Accedi al Terminale Live</a>"
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "HTML"})
    except: pass

def run_update():
    try:
        res = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR", timeout=5).json()
        prezzo_btc = f"€ {res.get('EUR', 60000.0):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        notizie = get_real_news()
        report_id = random.randint(1000, 9999)
        analisi_pro = generate_pro_analysis()
        scenario = random.choice(["INSTITUTIONAL ROTATION", "LIQUIDITY BRIDGE", "VOLATILITY SHOCK", "NETWORK INTELLIGENCE"])

        html_content = f"""
        <!DOCTYPE html><html><head><meta charset='UTF-8'>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
        body{{background:#020408; color:#a1b2c3; font-family:monospace; padding:50px; line-height:1.8; font-size:1.1rem;}}
        .terminal{{max-width:950px; margin:0 auto; border:2px solid #1a2332; padding:50px; background:#060913; box-shadow:0 0 60px rgba(0,229,255,0.07);}}
        h1{{color:#00e5ff; border-bottom:2px solid #1a2332; font-size:1.8rem; margin-bottom:25px; padding-bottom:15px;}}
        .intel-box{{background:#03050a; padding:35px; border-left:6px solid #00ff88; color:#fff; font-size:1.25rem; margin:30px 0; line-height:1.7;}}
        .price{{font-size:2.8rem; color:#fff; font-weight:bold; margin:30px 0; letter-spacing:-1px;}}
        .news-line{{color:#00ff88; font-size:1.05rem; margin-bottom:10px; border-bottom:1px solid #111; padding-bottom:5px;}}
        
        @media (max-width: 768px) {{
            body {{ padding: 15px; font-size: 1rem; }}
            .terminal {{ padding: 20px; border: 1px solid #1a2332; }}
            h1 {{ font-size: 1.4rem; }}
            .intel-box {{ padding: 20px; font-size: 1.1rem; border-left: 4px solid #00ff88; }}
            .price {{ font-size: 2rem; }}
        }}
        </style></head><body><div class='terminal'>
        <h1>KEYGAP // DOSSIER INTELLIGENCE #{report_id}</h1>
        <p style="font-size:1rem; opacity:0.6;">TIMESTAMP: {datetime.now().strftime('%d/%m/%Y %H:%M')} CET | SCENARIO: {scenario}</p>
        <div class='intel-box'>
            <strong>VALUTAZIONE CEFI vs DEFI:</strong><br><br>
            {analisi_pro}
        </div>
        <div class='price'>BTC: {prezzo_btc}</div>
        <hr style="border:1px solid #1a2332; margin:40px 0;">
        <h3 style="color:#00e5ff; text-transform:uppercase;">Live Data Interceptions:</h3>
        {"".join([f"<div class='news-line'>> {n['text']}</div>" for n in notizie])}
        <p style='margin-top:60px; font-size:0.8rem; color:#445; text-align:center; letter-spacing:4px;'>KEYGAP ADVANTAGE CORE // ENCRYPTED DOCUMENT</p>
        </div></body></html>"""

        filename = f"Report_Mondiale_{datetime.now().strftime('%d_%m_%Y_%H_%M')}.html"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, "w", encoding='utf-8') as f: f.write(html_content)

        update_index_github()
        
        try:
            service = get_service()
            body = {'title': f'Keygap Intelligence #{report_id} - BTC {prezzo_btc}', 'content': html_content}
            service.posts().insert(blogId=BLOG_ID, body=body).execute()
        except: pass

        subprocess.run(["git", "add", "index.html", "archivio.html", "Report_Finanziari/"], cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"📊 Dossier {report_id}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main", "--force"], cwd=BASE_DIR)

        print(f"✅ [KEYGAP] Sincronizzazione completata alle {datetime.now().strftime('%H:%M')}")
        send_telegram_alert(prezzo_btc, report_id, scenario, analisi_pro)

    except Exception as e: print(f"❌ Errore Ciclo: {e}")

if __name__ == "__main__":
    print("🚀 KEYGAP_ADVANTAGE CORE - Mobile Optimized Engine Active.")
    while True:
        run_update()
        time.sleep(1800)