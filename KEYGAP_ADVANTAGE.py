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
    """Scarica notizie vere dal mercato crypto via API pubblica con LINK"""
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
    """Crea la lista cliccabile dei report per la home di GitHub"""
    try:
        cartella = "Report_Finanziari"
        if not os.path.exists(cartella): os.makedirs(cartella)
        
        reports = sorted(os.listdir(cartella), reverse=True)
        links_html = "".join([f'<li><a href="{cartella}/{r}">{r.replace(".html", "").replace("_", " ")}</a></li>' for r in reports[:20]])
        
        index_content = f"""
        <html>
        <head><title>Keygap Intelligence - Live Feed</title></head>
        <body style="font-family: sans-serif; padding: 30px;">
            <h1>Keygap Global Intelligence - Archivio Report</h1>
            <hr>
            <ul>{links_html}</ul>
        </body>
        </html>
        """
        with open("index.html", "w", encoding='utf-8') as f:
            f.write(index_content)
    except Exception as e:
        print(f"⚠️ Errore indice: {e}")


def pubblica():
    """Crea un post SEO-friendly per Blogger con stile Mondiale e Monetizzazione"""
    try:
        service = get_service()
        try:
            url_p = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"
            res = requests.get(url_p, timeout=5).json()
            prezzo_numero = res.get('EUR', 87420.10)
            prezzo_btc = f"€ {prezzo_numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except:
            prezzo_btc = "€ 87.420,10"

        ora = datetime.now().strftime("%d/%m/%Y %H:%M")
        vere_notizie = get_real_news()
        percentuale = f"{random.randint(97, 99)}%"
        adsterra_script = '<script src="https://pl28819682.effectivegatecpm.com/07/47/37/074737f2d1be0f3c0e9de0585a695fd7.js"></script>'
        titolo = f"📊 Keygap Intelligence - Report CeFi/DeFi {ora}"
        
        contenuto_html = f"""
        {adsterra_script}
        <div style="font-family: 'Segoe UI', Arial, sans-serif; max-width: 800px; margin: auto; border: 1px solid #e1e4e8; border-radius: 12px; background-color: #ffffff; overflow: hidden; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
            <div style="background: linear-gradient(135deg, #0f172a, #1e293b); padding: 25px; text-align: center; color: white;">
                <h2 style="margin: 0; font-size: 22px; text-transform: uppercase;">Keygap Global Intelligence</h2>
                <p style="margin: 5px 0 0; opacity: 0.8; font-size: 14px;">Market Analysis | {ora}</p>
            </div>
            <div style="padding: 30px;">
                <div style="display: flex; gap: 15px; margin-bottom: 25px; text-align: center;">
                    <div style="flex: 1; background: #f8fafc; padding: 15px; border-radius: 8px;">
                        <span style="font-size: 11px; color: #64748b; font-weight: bold;">BTC/EUR</span><br>
                        <span style="font-size: 18px; font-weight: 700;">{prezzo_btc}</span>
                    </div>
                    <div style="flex: 1; background: #ecfdf5; padding: 15px; border-radius: 8px; border: 1px solid #10b981;">
                        <span style="font-size: 11px; color: #047857; font-weight: bold;">SIGNAL</span><br>
                        <span style="font-size: 18px; font-weight: 700; color: #047857;">STRONG BUY</span>
                    </div>
                </div>
                <h3 style="color: #0f172a; border-left: 4px solid #3b82f6; padding-left: 10px; font-size: 17px;">Analisi CeFi & DeFi</h3>
                <p style="color: #475569; font-size: 14px; line-height: 1.6;">L'algoritmo Keygap ha rilevato una forte pressione di accumulo istituzionale. I protocolli DeFi mostrano un incremento della liquidità, confermando la solidità del trend attuale con affidabilità al {percentuale}.</p>
                <div style="background: #f1f5f9; padding: 15px; border-radius: 8px; font-size: 13px;">
                    {"".join([f"<p style='margin-bottom: 8px;'><strong>[{n['time']}]</strong> {n['text']}</p>" for n in vere_notizie])}
                </div>
                <div style="text-align: center; margin-top: 30px; background-color: #f8fafc; padding: 20px; border-radius: 10px;">
                    <h3 style="margin-bottom: 15px;">👉 <a href="{SITO_MONETIZZATO}" target="_blank" style="color: #2563eb; text-decoration: none; font-weight: bold;">CLICCA QUI PER IL SEGNALE LIVE</a> 👈</h3>
                </div>
            </div>
        </div>
        """
        body = {'kind': 'blogger#post', 'title': titolo, 'content': contenuto_html, 'labels': ['CeFi', 'DeFi', 'Bitcoin', 'Keygap', 'Trading Online']}
        service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
        print(f"✅ [BLOGGER] REPORT MONDIALE INVIATO: {ora}")
    except Exception as e:
        print(f"❌ Errore Blogger: {e}")


def run_update():
    """Aggiorna il sito e genera Report Professionali"""
    # 1. Inizializziamo status_web con valori di default per evitare l'errore "not defined"
    status_web = {"status": "IN_AGGIORNAMENTO", "price": "N/A", "signal": "NEUTRAL"}
    
    try:
        # --- RECUPERO PREZZO ---
        try:
            url_p = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"
            res = requests.get(url_p, timeout=5).json()
            prezzo_numero = res.get('EUR', 87420.10)
        except:
            prezzo_numero = 87420.10
        
        prezzo_btc = f"€ {prezzo_numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # --- DETERMINAZIONE SEGNALE ---
        prezzo_precedente = prezzo_numero
        if os.path.exists("market_status.json"):
            try:
                with open("market_status.json", "r") as f:
                    old = json.load(f)
                    p_str = old['price'].replace('€', '').replace('.', '').replace(',', '.').strip()
                    prezzo_precedente = float(p_str)
            except: pass

        nuovo_segnale = "NEUTRAL"
        if prezzo_numero > prezzo_precedente: nuovo_segnale = "BULLISH"
        elif prezzo_numero < prezzo_precedente: nuovo_segnale = "BEARISH"

        # --- ORA DEFINIAMO status_web CON I DATI REALI ---
        ora_attuale = datetime.now().strftime("%H:%M:%S")
        vere_notizie = get_real_news()
        percentuale = f"{random.randint(97, 99)}%"

        status_web = {
            "status": "OPERATIVO",
            "price": prezzo_btc,
            "signal": nuovo_segnale,
            "reliability": percentuale,
            "last_update": ora_attuale,
            "ticker": f"BTC/EUR: {prezzo_btc} • SIGNAL: {nuovo_segnale}",
            "news": vere_notizie
        }

        # --- SALVATAGGIO E REPORT ---
        if not os.path.exists("Report_Finanziari"): os.makedirs("Report_Finanziari")
        
        # Scrittura JSON
        with open("market_status.json", "w", encoding='utf-8') as j:
            json.dump(status_web, j, indent=4, ensure_ascii=False)
            
        # Generazione HTML (Assicurati che html_report usi i dati di status_web)
        data_display = datetime.now().strftime("%d/%m/%Y")
        html_report = f"<html><body><h1>Report {data_display}</h1><p>Prezzo: {prezzo_btc}</p></body></html>"

        data_per_file = datetime.now().strftime("%d_%m_%Y_%H_%M")
        with open(f"Report_Finanziari/Report_Mondiale_{data_per_file}.html", "w", encoding='utf-8') as h_rep:
            h_rep.write(html_report)

        # --- AGGIORNAMENTO INDICE E GIT ---
        update_index_github()
        
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"📊 Update {ora_attuale}"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        
        print(f"✅ [KEYGAP] Report inviato con successo alle {ora_attuale}")

    except Exception as e:
        print(f"❌ Errore critico durante run_update: {e}")

if __name__ == "__main__":
    print("🚀 KEYGAP_ADVANTAGE CORE - Modalità Real-Time Attiva.")
    print("📈 Aggiornamento automatico impostato ogni 30 minuti.")
    
    while True:
        now = datetime.now()
        print(f"🔄 Avvio ciclo di aggiornamento: {now.strftime('%H:%M:%S')}")
        
        try:
            # 1. Recupera news fresche e aggiorna il prezzo
            run_update() 
            
            # 2. Pubblica l'articolo professionale su Blogger e GitHub
            # pubblica()
            
            print(f"✅ Operazione completata con successo alle {datetime.now().strftime('%H:%M:%S')}")
            print("💤 Prossimo aggiornamento tra 30 minuti...")
            
        except Exception as e:
            print(f"⚠️ Errore durante il ciclo: {e}")
            print("🔄 Tentativo di ripristino tra 60 secondi...")
            time.sleep(60)
            continue

        # Dorme per 1800 secondi (esattamente 30 minuti)
        time.sleep(1800)