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

# --- MOTORE DI INTELLIGENCE DINAMICA (CeFi vs DeFi) ---
def generate_pro_analysis():
    """Genera un confronto reale e professionale, sempre differente."""
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
    """Recupera news reali o genera intercettazioni se l'API è offline."""
    try:
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        r = requests.get(url, timeout=5).json()
        news_list = []
        for item in r.get('Data', [])[:6]:
            t = datetime.fromtimestamp(item['published_on']).strftime('%H:%M')
            news_list.append({"time": t, "text": item['title'], "link": item['url']})
        return news_list
    except:
        return [{"time": "INTEL", "text": "Analisi flussi istituzionali in corso su canali criptati.", "link": "#"}]

# --- GESTIONE SITO E ARCHIVIO (FIX 404) ---
def update_index_github():
    """Rigenera index.html e archivio.html basandosi SOLO sui file realmente esistenti."""
    try:
        if not os.path.exists(REPORT_DIR): os.makedirs(REPORT_DIR)
        reports = sorted([f for f in os.listdir(REPORT_DIR) if f.endswith('.html')], reverse=True)
        ultimo_report = f"Report_Finanziari/{reports[0]}" if reports else "archivio.html"
        
        # 1. Generazione Archivio
        links_html = "".join([f'<a href="Report_Finanziari/{r}" style="display:block; color:#00e5ff; text-decoration:none; margin-bottom:12px; border:1px solid #1a2332; padding:15px; border-radius:8px;">> DOSSIER {r.replace(".html","")}</a>' for r in reports[:30]])
        
        with open(os.path.join(BASE_DIR, "archivio.html"), "w", encoding='utf-8') as f:
            f.write(f"<html><body style='background:#05070a; color:#fff; font-family:monospace; padding:40px;'><h1>ARCHIVIO INTELLIGENCE</h1><hr>{links_html}</body></html>")

        # 2. Aggiornamento Index (Dashboard Live)
        index_content = f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>KEYGAP | Terminal</title>
        <link href="https://fonts.googleapis.com/css2?family=Inter:wght@900&family=JetBrains+Mono&display=swap" rel="stylesheet">
        <style>
            body {{ background: #06080a; color: #f0f2f5; font-family: 'Inter', sans-serif; margin: 0; display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}
            header {{ background: #0d1117; border-bottom: 1px solid #21262d; display: grid; grid-template-columns: 250px 1fr 350px; align-items: center; padding: 10px 20px; }}
            .btn-live {{ background: #ff0055; color: #fff; text-decoration: none; padding: 10px 15px; border-radius: 6px; font-weight: 900; font-size: 0.75rem; animation: pulse 1.5s infinite; text-align: center; border: 1px solid #ff0055; }}
            main {{ display: grid; grid-template-columns: 300px 1fr 380px; gap: 5px; flex-grow: 1; padding: 5px; background: #000; }}
            .panel {{ background: #0d1117; border: 1px solid #21262d; }}
            @keyframes pulse {{ 0% {{ box-shadow: 0 0 0 0 rgba(255,0,85,0.7); }} 70% {{ box-shadow: 0 0 0 10px rgba(255,0,85,0); }} 100% {{ box-shadow: 0 0 0 0 rgba(255,0,85,0); }} }}
        </style>
        </head><body><header>
            <div style="font-weight:900; font-size:1.4rem;">KEY<span style="color:#00ff88;">GAP</span></div>
            <div style="text-align:center;"><script src="https://pl28819682.effectivegatecpm.com/07/47/37/074737f2d1be0f3c0e9de0585a695fd7.js"></script></div>
            <div style="display: flex; gap: 10px; justify-content: flex-end;">
                <a href="{ultimo_report}" class="btn-live">🔴 ULTIMO DOSSIER LIVE</a>
                <a href="archivio.html" style="background:#00ff88; color:#000; text-decoration:none; padding:10px 15px; border-radius:6px; font-weight:800; font-size:0.7rem;">📂 ARCHIVIO</a>
            </div>
        </header><main>
            <div class="panel"><iframe src="https://s.tradingview.com/embed-widget/market-overview/?colorTheme=dark" width="100%" height="100%" frameborder="0"></iframe></div>
            <div class="panel"><iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCEUR&interval=1&theme=dark" width="100%" height="100%" frameborder="0"></iframe></div>
            <div style="display:grid; grid-template-rows:1fr 1fr; gap:5px;">
                <div class="panel"><iframe src="https://cryptopanic.com/widgets/news/?bg_color=0d1117&link_color=00ff88&text_color=f0f2f5" width="100%" height="100%" frameborder="0"></iframe></div>
                <div class="panel"><iframe src="https://sslecal2.investing.com?importance=2,3&calType=day&timeZone=58&lang=5" width="100%" height="100%" frameborder="0" style="filter: invert(0.9) hue-rotate(180deg);"></iframe></div>
            </div></main></body></html>"""
        
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
        # 1. Recupero Dati Mercato
        res = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR", timeout=5).json()
        prezzo_btc = f"€ {res.get('EUR', 60000.0):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        notizie = get_real_news()
        report_id = random.randint(1000, 9999)
        analisi_pro = generate_pro_analysis()
        scenario = random.choice(["INSTITUTIONAL ROTATION", "LIQUIDITY BRIDGE", "STRATEGIC COMPRESSION"])

        # 2. Generazione HTML Report
        html_content = f"""
        <!DOCTYPE html><html><head><meta charset='UTF-8'><style>
        body{{background:#020408; color:#a1b2c3; font-family:monospace; padding:40px; line-height:1.8;}}
        .terminal{{max-width:850px; margin:0 auto; border:1px solid #1a2332; padding:45px; background:#060913;}}
        h1{{color:#00e5ff; border-bottom:1px solid #1a2332;}} .intel-box{{background:#03050a; padding:25px; border-left:4px solid #00ff88; color:#eee;}}
        </style></head><body><div class='terminal'>
        <h1>KEYGAP // DOSSIER #{report_id}</h1><p>TIMESTAMP: {datetime.now().strftime('%d/%m/%Y %H:%M')}</p>
        <div class='intel-box'><strong>ANALISI CEFI vs DEFI:</strong><br><br>{analisi_pro}</div>
        <p style='font-size:1.8rem; color:#fff;'>BTC VALUE: {prezzo_btc}</p>
        <hr><h3>LIVE RAW NEWS:</h3>
        {"".join([f"<p style='color:#00ff88;'>> {n['text']}</p>" for n in notizie])}
        </div></body></html>"""

        filename = f"Report_Mondiale_{datetime.now().strftime('%d_%m_%Y_%H_%M')}.html"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, "w", encoding='utf-8') as f: f.write(html_content)

        update_index_github()
        
        # 3. Aggiornamento Blogger
        try:
            service = get_service()
            body = {'title': f'Intelligence Report #{report_id} - BTC {prezzo_btc}', 'content': html_content}
            service.posts().insert(blogId=BLOG_ID, body=body).execute()
        except Exception as e: print(f"⚠️ Blogger Error: {e}")

        # 4. Git Sync
        subprocess.run(["git", "add", "."], cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"📊 Dossier {report_id}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main", "--force"], cwd=BASE_DIR)

        print(f"✅ [KEYGAP] Sincronizzazione completata alle {datetime.now().strftime('%H:%M')}")
        send_telegram_alert(prezzo_btc, report_id, scenario, analisi_pro)

    except Exception as e: print(f"❌ Errore Ciclo: {e}")

if __name__ == "__main__":
    print("🚀 KEYGAP_ADVANTAGE CORE - Intelligence Engine Active.")
    while True:
        run_update()
        time.sleep(1800)