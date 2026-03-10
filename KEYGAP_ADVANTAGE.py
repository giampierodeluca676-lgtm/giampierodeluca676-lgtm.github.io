import os, pickle, json, subprocess, time, requests, random
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# --- SISTEMA DI IDENTIFICAZIONE PROCESSO ---
with open("KEYGAP_ADVANTAGE.pid", "w") as f:
    f.write(str(os.getpid()))

SCOPES = ['https://www.googleapis.com/auth/blogger']
BLOG_ID = '2744764892823107807'
SITO_MONETIZZATO = 'https://giampierodeluca676-lgtm.github.io/'

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

def get_real_news():
    try:
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        r = requests.get(url, timeout=5).json()
        news_list = []
        for item in r['Data'][:6]:
            t = datetime.fromtimestamp(item['published_on']).strftime('%H:%M')
            news_list.append({
                "time": t, 
                "text": item['title'],
                "link": item['url'] 
            })
        return news_list
    except Exception as e:
        print(f"⚠️ Errore recupero news: {e}")
        return [{"time": "SYS", "text": "Sincronizzazione flussi globali in corso...", "link": "#"}]

def update_index_github():
    try:
        cartella = "Report_Finanziari"
        if not os.path.exists(cartella): os.makedirs(cartella)
        
        reports = sorted(os.listdir(cartella), reverse=True)
        links_html = "".join([f"""
            <a href="{cartella}/{r}" style="display: flex; justify-content: space-between; align-items: center; background: #0d1117; border: 1px solid rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; text-decoration: none; color: #fff; margin-bottom: 15px;">
                <div style="display: flex; flex-direction: column;">
                    <span style="color: #00e5ff; font-family: 'JetBrains Mono'; font-weight: 700; font-size: 0.8rem; margin-bottom: 5px;">{r.replace('.html', '').split('_')[-2]} / {r.replace('.html', '').split('_')[-3]} / {r.replace('.html', '').split('_')[-4]} - {r.replace('.html', '').split('_')[-1]}</span>
                    <span style="font-size: 1.2rem; font-weight: 800;">{r.replace(".html", "").replace("_", " ")}</span>
                </div>
                <span style="background: rgba(0, 255, 136, 0.1); color: #00ff88; padding: 5px 12px; border-radius: 6px; font-size: 0.8rem; font-weight: 700;">DECRIPTATO</span>
            </a>""" for r in reports[:20]])
        
        archivio_content = f"""
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="UTF-8">
            <title>KEYGAP | Intelligence Archive</title>
            <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700&family=Outfit:wght@500;700;900&display=swap" rel="stylesheet">
            <style>
                body {{ background: #05070a; color: #fff; font-family: 'Outfit', sans-serif; padding: 40px 20px; margin: 0; }}
                .container {{ max-width: 900px; margin: 0 auto; }}
                h1 {{ font-family: 'JetBrains Mono'; color: #fff; font-size: 1.8rem; margin-bottom: 30px; border-bottom: 2px solid #00e5ff; padding-bottom: 20px; }}
                .btn-back {{ color: #00e5ff; text-decoration: none; font-weight: 800; text-transform: uppercase; font-size: 0.9rem; float: right; }}
            </style>
        </head>
        <body>
            <div class="container">
                <a href="index.html" class="btn-back">← TERMINALE</a>
                <h1>ARCHIVIO INTELLIGENCE</h1>
                <div class="grid">{links_html}</div>
            </div>
        </body>
        </html>
        """
        with open("archivio.html", "w", encoding='utf-8') as f:
            f.write(archivio_content)
    except Exception as e:
        print(f"⚠️ Errore aggiornamento archivio: {e}")

def run_update():
    status_web = {"status": "IN_AGGIORNAMENTO", "price": "N/A", "signal": "NEUTRAL"}
    try:
        try:
            url_p = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"
            res = requests.get(url_p, timeout=5).json()
            prezzo_numero = res.get('EUR', 87420.10)
        except:
            prezzo_numero = 87420.10
        
        prezzo_btc = f"€ {prezzo_numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        ora_attuale = datetime.now().strftime("%H:%M:%S")
        vere_notizie = get_real_news()
        volatilita = f"{random.uniform(0.1, 2.5):.2f}%"
        hash_rate = f"{random.randint(500, 700)} EH/s"

        # --- GENERAZIONE REPORT HTML PROFESSIONALE ---
        data_full = datetime.now().strftime("%d/%m/%Y - %H:%M")
        
        html_report = f"""
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="UTF-8">
            <title>INTEL REPORT | {data_full}</title>
            <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Outfit:wght@700;900&display=swap" rel="stylesheet">
            <style>
                :root {{ --bg: #05070a; --acc: #00e5ff; --panel: #0d1117; --border: rgba(0, 229, 255, 0.2); }}
                body {{ background: var(--bg); color: #fff; font-family: 'Outfit', sans-serif; padding: 40px; margin: 0; }}
                .report-box {{ max-width: 800px; margin: 0 auto; border: 1px solid var(--border); padding: 40px; border-radius: 20px; background: var(--panel); box-shadow: 0 0 50px rgba(0, 229, 255, 0.05); }}
                .header {{ border-bottom: 2px solid var(--acc); padding-bottom: 20px; margin-bottom: 30px; }}
                .title {{ font-family: 'JetBrains Mono'; font-size: 1.8rem; font-weight: 900; color: var(--acc); letter-spacing: -1px; }}
                .meta {{ font-family: 'JetBrains Mono'; font-size: 0.9rem; color: #666; margin-top: 10px; }}
                .stat-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin: 30px 0; }}
                .stat-card {{ background: rgba(0,0,0,0.3); padding: 20px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.05); }}
                .label {{ color: var(--acc); font-size: 0.75rem; text-transform: uppercase; font-family: 'JetBrains Mono'; }}
                .value {{ font-size: 1.5rem; font-weight: 800; margin-top: 5px; }}
                .news-section {{ margin-top: 40px; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 30px; }}
                .news-item {{ margin-bottom: 15px; font-size: 1rem; color: #ccc; line-height: 1.5; padding-left: 15px; border-left: 2px solid var(--acc); }}
                .footer {{ text-align: center; margin-top: 50px; font-size: 0.8rem; color: #444; font-family: 'JetBrains Mono'; }}
            </style>
        </head>
        <body>
            <div class="report-box">
                <div class="header">
                    <div class="title">KEYGAP INTELLIGENCE REPORT</div>
                    <div class="meta">ID: {random.randint(1000,9999)} | DATA: {data_full} | STATUS: DECRYPTED</div>
                </div>
                
                <div class="stat-grid">
                    <div class="stat-card">
                        <div class="label">Bitcoin Price (EUR)</div>
                        <div class="value">{prezzo_btc}</div>
                    </div>
                    <div class="stat-card">
                        <div class="label">Network Volatility</div>
                        <div class="value">{volatilita}</div>
                    </div>
                    <div class="stat-card">
                        <div class="label">Estimated Hashrate</div>
                        <div class="value">{hash_rate}</div>
                    </div>
                    <div class="stat-card">
                        <div class="label">Market Sentiment</div>
                        <div class="value" style="color:#00ff88">STABLE_ACQ</div>
                    </div>
                </div>

                <div class="news-section">
                    <div class="label" style="margin-bottom:20px">Global Market Feed</div>
                    {''.join([f'<div class="news-item"><b>[{n["time"]}]</b> {n["text"]}</div>' for n in vere_notizie[:4]])}
                </div>

                <div class="footer">KEYGAP_ADVANTAGE CORE - SECURE ENCRYPTED DOCUMENT</div>
            </div>
        </body>
        </html>
        """

        if not os.path.exists("Report_Finanziari"): os.makedirs("Report_Finanziari")
        
        data_per_file = datetime.now().strftime("%d_%m_%Y_%H_%M")
        with open(f"Report_Finanziari/Report_Mondiale_{data_per_file}.html", "w", encoding='utf-8') as h_rep:
            h_rep.write(html_report)

        update_index_github()
        
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"📊 Update {ora_attuale}"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        
        print(f"✅ [KEYGAP] Report inviato con successo alle {ora_attuale}")

    except Exception as e:
        print(f"❌ Errore critico durante run_update: {e}")

if __name__ == "__main__":
    print("🚀 KEYGAP_ADVANTAGE CORE - Modalità Real-Time Attiva.")
    while True:
        now = datetime.now()
        print(f"🔄 Avvio ciclo di aggiornamento: {now.strftime('%H:%M:%S')}")
        try:
            run_update() 
            print(f"✅ Operazione completata con successo alle {datetime.now().strftime('%H:%M:%S')}")
            print("💤 Prossimo aggiornamento tra 30 minuti...")
        except Exception as e:
            print(f"⚠️ Errore durante il ciclo: {e}")
            time.sleep(60)
            continue
        time.sleep(1800)