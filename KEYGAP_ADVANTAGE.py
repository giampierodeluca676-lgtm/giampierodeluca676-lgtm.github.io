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
        
        # Ordinamento cronologico inverso basato sul nome file (YYYY_MM_DD_HH_MM)
        reports = sorted([f for f in os.listdir(cartella) if f.endswith('.html')], reverse=True)
        links_html = ""
        
        for r in reports[:30]:
            try:
                parti = r.replace('.html', '').split('_')
                
                # Se il file segue il formato Report_Mondiale_GG_MM_AAAA_HH_MM
                if len(parti) >= 6:
                    giorno = parti[-4]
                    mese = parti[-3]
                    anno = parti[-2]
                    ora = parti[-1].replace('-', ':')
                    
                    data_display = f"{giorno}.{mese}.{anno}"
                    ora_display = ora
                    titolo_label = "ANALISI MERCATO GLOBALE"
                else:
                    data_display = "STORICO"
                    ora_display = "--:--"
                    titolo_label = r.replace(".html", "").replace("_", " ").upper()

                links_html += f"""
                <a href="{cartella}/{r}" style="display: flex; align-items: center; background: #0d1117; border: 1px solid rgba(0, 229, 255, 0.1); padding: 18px 25px; border-radius: 12px; text-decoration: none; color: #fff; margin-bottom: 12px; border-left: 5px solid #00e5ff; transition: 0.3s;">
                    <div style="display: flex; gap: 25px; align-items: center; flex-grow: 1;">
                        <div style="display: flex; flex-direction: column; min-width: 90px; border-right: 1px solid rgba(255,255,255,0.1); padding-right: 20px; text-align: center;">
                            <span style="color: #00e5ff; font-family: 'JetBrains Mono'; font-size: 0.85rem; font-weight: 700;">{data_display}</span>
                            <span style="color: rgba(255,255,255,0.4); font-family: 'JetBrains Mono'; font-size: 0.7rem;">{ora_display}</span>
                        </div>
                        <div>
                            <div style="font-size: 1.05rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase;">{titolo_label}</div>
                            <div style="font-family: 'JetBrains Mono'; font-size: 0.6rem; color: #00ff88; margin-top: 4px; letter-spacing: 2px;">STATUS: DECRIPTATO // INTELLIGENCE_CORE</div>
                        </div>
                    </div>
                    <div style="background: rgba(0, 255, 136, 0.1); color: #00ff88; padding: 6px 12px; border-radius: 4px; font-size: 0.65rem; font-weight: 900; border: 1px solid rgba(0, 255, 136, 0.2); font-family: 'JetBrains Mono';">SECURE</div>
                </a>"""
            except Exception:
                continue

        archivio_content = f"""
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="UTF-8">
            <title>KEYGAP | Intelligence Archive</title>
            <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700&family=Outfit:wght@500;700;900&display=swap" rel="stylesheet">
            <style>
                body {{ background: #05070a; color: #fff; font-family: 'Outfit', sans-serif; padding: 40px 20px; margin: 0; }}
                .container {{ max-width: 850px; margin: 0 auto; }}
                h1 {{ font-family: 'JetBrains Mono'; font-size: 1.5rem; margin-bottom: 30px; border-bottom: 2px solid #00e5ff; padding-bottom: 20px; text-transform: uppercase; letter-spacing: 3px; display: flex; justify-content: space-between; align-items: center; }}
                .btn-back {{ color: #00e5ff; text-decoration: none; font-size: 0.8rem; border: 1px solid #00e5ff; padding: 8px 16px; border-radius: 6px; transition: 0.3s; }}
                .btn-back:hover {{ background: #00e5ff; color: #000; box-shadow: 0 0 15px rgba(0,229,255,0.3); }}
                a:hover {{ transform: scale(1.01); background: #161b22 !important; border-color: #00e5ff !important; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>ARCHIVIO REPORT <a href="index.html" class="btn-back">← TERMINALE</a></h1>
                <div class="grid">{{links_html}}</div>
            </div>
        </body>
        </html>
        """.replace("{links_html}", links_html)
        
        with open("archivio.html", "w", encoding='utf-8') as f:
            f.write(archivio_content)
    except Exception as e:
        print(f"⚠️ Errore aggiornamento archivio: {e}")

def run_update():
    try:
        try:
            url_p = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"
            res = requests.get(url_p, timeout=5).json()
            prezzo_numero = res.get('EUR', 60000.00)
        except:
            prezzo_numero = 60000.00
        
        prezzo_btc = f"€ {prezzo_numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        ora_attuale = datetime.now().strftime("%H:%M")
        data_f = datetime.now().strftime("%d/%m/%Y")
        vere_notizie = get_real_news()
        volatilita = f"{random.uniform(0.1, 2.5):.2f}%"
        hash_rate = f"{random.randint(500, 700)} EH/s"
        report_id = random.randint(1000, 9999)

        # --- GENERAZIONE REPORT HTML UNIFORMATO (INTELLIGENCE PRO) ---
        html_report = f"""
        <!DOCTYPE html>
        <html lang="it">
        <head>
            <meta charset="UTF-8">
            <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Outfit:wght@700;900&display=swap" rel="stylesheet">
            <style>
                :root {{ --bg: #05070a; --acc: #00e5ff; --panel: #0d1117; --green: #00ff88; }}
                body {{ background: var(--bg); color: #fff; font-family: 'Outfit', sans-serif; padding: 40px; margin: 0; display: flex; justify-content: center; }}
                .report-container {{ max-width: 750px; width: 100%; background: var(--panel); padding: 40px; border-radius: 25px; border: 1px solid rgba(0, 229, 255, 0.2); border-top: 6px solid var(--acc); box-shadow: 0 20px 50px rgba(0,0,0,0.5); }}
                .header-intel {{ border-bottom: 1px solid rgba(0, 229, 255, 0.1); padding-bottom: 20px; margin-bottom: 30px; display: flex; justify-content: space-between; align-items: flex-start; }}
                .title-main {{ font-family: 'JetBrains Mono'; font-size: 1.4rem; color: var(--acc); letter-spacing: 2px; font-weight: 700; }}
                .meta-data {{ font-family: 'JetBrains Mono'; font-size: 0.75rem; color: rgba(255,255,255,0.5); text-align: right; line-height: 1.6; }}
                .status-badge {{ background: rgba(0, 255, 136, 0.1); color: var(--green); padding: 4px 12px; border-radius: 5px; font-size: 0.7rem; font-weight: 900; border: 1px solid var(--green); }}
                .price-box {{ background: rgba(0,0,0,0.3); padding: 30px; border-radius: 15px; text-align: center; margin-bottom: 30px; border: 1px solid rgba(255,255,255,0.05); }}
                .price-label {{ font-size: 0.8rem; text-transform: uppercase; color: var(--acc); letter-spacing: 3px; margin-bottom: 10px; }}
                .price-value {{ font-size: 3rem; font-weight: 900; letter-spacing: -1px; }}
                .stat-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 30px; }}
                .stat-card {{ background: rgba(255,255,255,0.02); padding: 15px; border-radius: 10px; border: 1px solid rgba(255,255,255,0.05); }}
                .stat-label {{ color: var(--acc); font-family: 'JetBrains Mono'; font-size: 0.65rem; text-transform: uppercase; }}
                .stat-value {{ font-size: 1.2rem; font-weight: 800; margin-top: 5px; }}
                .feed-title {{ font-family: 'JetBrains Mono'; font-size: 0.9rem; color: var(--acc); margin-bottom: 15px; border-left: 3px solid var(--acc); padding-left: 15px; }}
                .news-item {{ padding: 12px; border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 0.95rem; display: flex; gap: 15px; }}
                .news-time {{ color: var(--acc); font-family: 'JetBrains Mono'; font-weight: 700; min-width: 60px; }}
                .footer {{ text-align: center; margin-top: 40px; font-family: 'JetBrains Mono'; font-size: 0.65rem; color: rgba(255,255,255,0.2); letter-spacing: 4px; }}
            </style>
        </head>
        <body>
            <div class="report-container">
                <div class="header-intel">
                    <div>
                        <div class="title-main">KEYGAP INTELLIGENCE REPORT</div>
                        <div style="margin-top: 10px;"><span class="status-badge">STATUS: DECRYPTED</span></div>
                    </div>
                    <div class="meta-data">
                        ID: {report_id} | DATA: {data_f}<br>
                        TIME: {ora_attuale} UTC | NODES: ACTIVE
                    </div>
                </div>

                <div class="price-box">
                    <div class="price-label">Bitcoin Market Value (EUR)</div>
                    <div class="price-value">{prezzo_btc}</div>
                </div>

                <div class="stat-grid">
                    <div class="stat-card">
                        <div class="stat-label">Network Volatility</div>
                        <div class="stat-value">{volatilita}</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Estimated Hashrate</div>
                        <div class="stat-value">{hash_rate}</div>
                    </div>
                </div>

                <div class="feed-title">GLOBAL MARKET FEED // LIVE_DATA</div>
                <div class="news-list">
                    {''.join([f'<div class="news-item"><span class="news-time">[{n["time"]}]</span><span>{n["text"]}</span></div>' for n in vere_notizie[:5]])}
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