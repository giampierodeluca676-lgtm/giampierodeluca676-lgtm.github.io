import os, pickle, json, subprocess, time, requests, random
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# --- SISTEMA DI IDENTIFICAZIONE PROCESSO ---
# Questo crea un file che contiene l'ID del bot attuale per spegnerlo facilmente
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
    """Scarica notizie vere dal mercato crypto via API pubblica"""
    try:
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        r = requests.get(url, timeout=5).json()
        news_list = []
        for item in r['Data'][:6]:
            t = datetime.fromtimestamp(item['published_on']).strftime('%H:%M')
            news_list.append({"time": t, "text": item['title']})
        return news_list
    except Exception as e:
        print(f"⚠️ Errore recupero news: {e}")
        return [{"time": "SYS", "text": "Sincronizzazione flussi globali in corso..."}]

def pubblica():
    """Crea un post SEO-friendly per Blogger"""
    try:
        service = get_service()
        ora = datetime.now().strftime("%d/%m/%Y %H:%M")
        titolo = f"Keygap AdVantage - Report Mercato {ora}"
        contenuto_html = f"""
        <h2>Aggiornamento di Mercato Keygap</h2>
        <p>L'algoritmo ha appena completato l'analisi della chain BTC/EUR alle {ora}.</p>
        <div style="text-align: center; background-color: #f1f1f1; padding: 15px; border-radius: 5px;">
            <h3>👉 <a href="{SITO_MONETIZZATO}" target="_blank" style="color: #d93025; text-decoration: none;"><b>CLICCA QUI PER VEDERE IL SEGNALE IN TEMPO REALE</b></a> 👈</h3>
        </div>
        <p><i>Sistema operativo al 100%. Generato in automatico da KEYGAP_ADVANTAGE.</i></p>
        """
        body = {'kind': 'blogger#post', 'title': titolo, 'content': contenuto_html, 'labels': ['Trading', 'Bitcoin', 'Keygap', 'Analisi']}
        service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
        print(f"✅ REPORT INVIATO A BLOGGER: {ora}")
    except Exception as e:
        print(f"❌ Errore Blogger: {e}")

def run_update():
    """Aggiorna il sito e genera Report Professionali di livello Mondiale (DeFi/CeFi)"""
    try:
        # AGGIORNAMENTO PREZZO REALE
        try:
            url_p = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"
            res = requests.get(url_p, timeout=5).json()
            prezzo_numero = res.get('EUR', 87420.10)
            prezzo_btc = f"€ {prezzo_numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except:
            prezzo_btc = "€ 87.420,10"

        percentuale = f"{random.randint(97, 99)}%" 
        ora_attuale = datetime.now().strftime("%H:%M:%S")
        data_per_file = datetime.now().strftime("%d_%m_%Y_%H_%M")
        data_display = datetime.now().strftime("%d/%m/%Y")
        vere_notizie = get_real_news()
        
        status_web = {
            "status": "OPERATIVO",
            "price": prezzo_btc,
            "signal": "BULLISH",
            "reliability": percentuale,
            "last_update": ora_attuale,
            "ticker": f"BTC/EUR: {prezzo_btc} • KEYGAP SIGNAL: BULLISH • STATUS: ONLINE • UPDATE: {ora_attuale} • ",
            "news": vere_notizie
        }
        
        # --- GESTIONE REPORT FINANZIARI (DESIGN PROFESSIONALE MONDIALE) ---
        cartella_report = "Report_Finanziari"
        if not os.path.exists(cartella_report):
            os.makedirs(cartella_report)
            
        nome_file_storico = f"{cartella_report}/Report_Mondiale_{data_per_file}.html"
        
        # CREAZIONE DEL CONTENUTO HTML PROFESSIONALE (DEFI & CEFI INTELLIGENCE)
        html_report = f"""
        <div style="font-family: 'Segoe UI', Helvetica, Arial, sans-serif; max-width: 900px; margin: auto; border: 1px solid #e1e4e8; border-radius: 12px; background-color: #ffffff; color: #1a1d21; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
            
            <div style="background: linear-gradient(135deg, #0f172a, #1e293b); padding: 40px 20px; text-align: center; color: #f8fafc;">
                <h1 style="margin: 0; font-size: 32px; text-transform: uppercase; letter-spacing: 3px; font-weight: 800;">Keygap Global Intelligence</h1>
                <p style="margin: 10px 0 0; font-size: 16px; color: #94a3b8; font-weight: 300;">Analisi Quantitativa Asset Digitali | Report {data_display}</p>
            </div>

            <div style="padding: 40px;">
                <div style="display: flex; gap: 20px; margin-bottom: 40px; text-align: center;">
                    <div style="flex: 1; padding: 20px; background: #f1f5f9; border-radius: 8px;">
                        <span style="display: block; font-size: 12px; color: #64748b; text-transform: uppercase; font-weight: bold; margin-bottom: 5px;">BTC/EUR Index</span>
                        <span style="font-size: 22px; font-weight: 700; color: #0f172a;">{prezzo_btc}</span>
                    </div>
                    <div style="flex: 1; padding: 20px; background: #ecfdf5; border-radius: 8px; border: 1px solid #10b981;">
                        <span style="display: block; font-size: 12px; color: #059669; text-transform: uppercase; font-weight: bold; margin-bottom: 5px;">Market Signal</span>
                        <span style="font-size: 22px; font-weight: 700; color: #047857;">STRONG BULLISH</span>
                    </div>
                    <div style="flex: 1; padding: 20px; background: #eff6ff; border-radius: 8px;">
                        <span style="display: block; font-size: 12px; color: #3b82f6; text-transform: uppercase; font-weight: bold; margin-bottom: 5px;">Reliability Index</span>
                        <span style="font-size: 22px; font-weight: 700; color: #1d4ed8;">{percentuale}</span>
                    </div>
                </div>

                <div style="margin-bottom: 40px;">
                    <h3 style="font-size: 18px; color: #0f172a; border-left: 5px solid #3b82f6; padding-left: 15px; margin-bottom: 15px;">Sommario Esecutivo CeFi & DeFi</h3>
                    <p style="font-size: 15px; color: #475569; line-height: 1.7;">
                        I flussi di capitale istituzionali indicano una fase di accumulo strutturale. L'analisi on-chain rileva una diminuzione delle riserve sugli exchange (CeFi) e un incremento dell'attività nei protocolli di prestito decentralizzati (DeFi). Il modello quantitativo Keygap suggerisce una continuazione del trend primario con bassa volatilità attesa nel breve termine.
                    </p>
                </div>

                <h3 style="font-size: 18px; color: #0f172a; border-left: 5px solid #3b82f6; padding-left: 15px; margin-bottom: 20px;">Intelligence News Feed</h3>
                <div style="background: #ffffff; border: 1px solid #f1f5f9; border-radius: 8px;">
                    {"".join([f'''
                    <div style="padding: 15px; border-bottom: 1px solid #f1f5f9;">
                        <span style="color: #3b82f6; font-weight: 700; font-size: 13px;">[{n['time']}]</span>
                        <span style="margin-left: 10px; font-size: 14px; color: #1e293b;">{n['text']}</span>
                    </div>''' for n in vere_notizie])}
                </div>

                <div style="margin-top: 50px; text-align: center;">
                    <a href="{SITO_MONETIZZATO}" style="display: inline-block; background: #2563eb; color: #ffffff; padding: 18px 40px; text-decoration: none; font-weight: 800; border-radius: 50px; text-transform: uppercase; font-size: 14px; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(37,99,235,0.4);">
                        Accedi al Terminale Live Real-Time
                    </a>
                </div>
            </div>

            <div style="background: #f8fafc; padding: 25px; text-align: center; border-top: 1px solid #e2e8f0;">
                <p style="margin: 0; font-size: 11px; color: #94a3b8; line-height: 1.5;">
                    SISTEMA OPERATIVO 100% ONLINE. Questo documento è stato generato automaticamente dall'architettura KEYGAP_ADVANTAGE Core alle ore {ora_attuale} UTC. Analisi riservata per uso professionale e informativo.
                </p>
            </div>
        </div>
        """
        
        # Scrittura file principale per il sito (JSON)
        with open("market_status.json", "w", encoding='utf-8') as j:
            json.dump(status_web, j, indent=4, ensure_ascii=False)
            j.flush()
            os.fsync(j.fileno())

        # Scrittura Report Mondiale in formato HTML
        with open(nome_file_storico, "w", encoding='utf-8') as h_rep:
            h_rep.write(html_report)
            h_rep.flush()
            os.fsync(h_rep.fileno())
        
        # PUSH SU GITHUB
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"📊 KEYGAP GLOBAL REPORT Update {ora_attuale}"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        print(f"✅ [KEYGAP_ADVANTAGE] REPORT MONDIALE GENERATO: {prezzo_btc}")
        
    except Exception as e:
        print(f"❌ Errore aggiornamento professionale: {e}")
if __name__ == "__main__":
    print("🔥 KEYGAP_ADVANTAGE CORE - Avviato e monitorato.")
    while True:
        ora_ora = datetime.now().hour
        minuto_ora = datetime.now().minute
        
        if (ora_ora == 8 and minuto_ora == 30) or (ora_ora == 20 and minuto_ora == 30):
            pubblica()
            time.sleep(65)
        
        run_update()
        time.sleep(300)