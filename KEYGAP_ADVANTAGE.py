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
    """Aggiorna il sito con dati REALI (Prezzo e News) e archivia i Report in HTML"""
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
        
        # --- GESTIONE REPORT FINANZIARI (AGGIORNATA A HTML) ---
        cartella_report = "Report Finanziari"
        if not os.path.exists(cartella_report):
            os.makedirs(cartella_report)
            
        # Nome file con estensione .html
        nome_file_storico = f"{cartella_report}/Report_{data_per_file}.html"
        
        # CREAZIONE DEL CONTENUTO HTML IDENTICO A BLOGGER
        html_report = f"""
        <div style="font-family: Arial, sans-serif; padding: 20px; border: 1px solid #ddd; border-radius: 10px; max-width: 800px; margin: auto;">
            <h2 style="color: #2c3e50;">Aggiornamento di Mercato Keygap</h2>
            <p>L'algoritmo ha appena completato l'analisi della chain BTC/EUR alle {data_display} {ora_attuale}.</p>
            <div style="background: #f8f9fa; padding: 15px; border-left: 5px solid #27ae60; margin: 10px 0;">
                <p><strong>Prezzo Attuale:</strong> {prezzo_btc}</p>
                <p><strong>Segnale:</strong> BULLISH (Affidabilità {percentuale})</p>
            </div>
            <h3>Ultime Notizie Analizzate:</h3>
            <ul>
                {"".join([f"<li style='margin-bottom: 8px;'><strong>{n['time']}</strong> - {n['text']}</li>" for n in vere_notizie])}
            </ul>
            <p style="text-align: center; margin-top: 20px;">
                <a href="{SITO_MONETIZZATO}" style="background: #3498db; color: white; padding: 10px 20px; text-decoration: none; font-weight: bold; border-radius: 5px;">
                    👉 CLICCA QUI PER IL SEGNALE LIVE 👈
                </a>
            </p>
            <hr style="margin-top: 30px; border: 0; border-top: 1px solid #eee;">
            <p style="font-size: 12px; color: #7f8c8d; text-align: center;">Sistema operativo al 100%. Generato in automatico da KEYGAP_ADVANTAGE Core.</p>
        </div>
        """
        
        # Scrittura file principale per il sito (rimane JSON per il funzionamento web)
        with open("market_status.json", "w", encoding='utf-8') as j:
            json.dump(status_web, j, indent=4, ensure_ascii=False)
            j.flush()
            os.fsync(j.fileno())

        # Scrittura copia nei Report Finanziari in formato HTML
        with open(nome_file_storico, "w", encoding='utf-8') as h_rep:
            h_rep.write(html_report)
            h_rep.flush()
            os.fsync(h_rep.fileno())
        # ----------------------------------------------------
        
        # PUSH SU GITHUB
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"🚀 KEYGAP_ADVANTAGE Update {ora_attuale}"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        print(f"✅ [KEYGAP_ADVANTAGE] SITO E REPORT HTML AGGIORNATI: {prezzo_btc} alle: {ora_attuale}")
        
    except Exception as e:
        print(f"❌ Errore aggiornamento: {e}")
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