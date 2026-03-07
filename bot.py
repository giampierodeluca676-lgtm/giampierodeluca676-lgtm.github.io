import os, pickle, json, subprocess, time, requests
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/blogger']
BLOG_ID = '2744764892823107807'
# Il sito dove le persone devono atterrare per farti monetizzare con Adsterra
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
        # Prende le ultime 6 notizie reali
        for item in r['Data'][:6]:
            t = datetime.fromtimestamp(item['published_on']).strftime('%H:%M')
            news_list.append({"time": t, "text": item['title']})
        return news_list
    except Exception as e:
        print(f"⚠️ Errore recupero news: {e}")
        return [{"time": "SYS", "text": "Sincronizzazione flussi globali in corso..."}]

def pubblica():
    """Crea un post SEO-friendly per spingere gli utenti sul sito con Adsterra"""
    try:
        service = get_service()
        ora = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        titolo = f"Keygap AdVantage - Report Mercato {ora}"
        
        contenuto_html = f"""
        <h2>Aggiornamento di Mercato Keygap</h2>
        <p>L'algoritmo ha appena completato l'analisi della chain BTC/EUR alle {ora}.</p>
        <p>I livelli di supporto e i segnali direzionali sono stati aggiornati.</p>
        <br>
        <div style="text-align: center; background-color: #f1f1f1; padding: 15px; border-radius: 5px;">
            <h3>👉 <a href="{SITO_MONETIZZATO}" target="_blank" style="color: #d93025; text-decoration: none;"><b>CLICCA QUI PER VEDERE IL SEGNALE IN TEMPO REALE</b></a> 👈</h3>
        </div>
        <br>
        <p><i>Sistema operativo al 100%. Generato in automatico da Keygap.</i></p>
        """
        
        body = {
            'kind': 'blogger#post',
            'title': titolo,
            'content': contenuto_html,
            'labels': ['Trading', 'Bitcoin', 'Keygap', 'Analisi Tecnica', 'Segnali']
        }
        
        service.posts().insert(blogId=BLOG_ID, body=body, isDraft=False).execute()
        print(f"✅ REPORT INVIATO A BLOGGER: {ora} - Traffico indirizzato verso Adsterra.")
        
    except Exception as e:
        print(f"❌ Errore durante la pubblicazione su Blogger: {e}")

def run_update():
    """Aggiorna il sito con dati reali e notizie fresche"""
    try:
        # --- MODIFICA PER TABELLA A SINISTRA ---
        try:
            # Scarica il prezzo reale da CryptoCompare
            url_p = "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR"
            res = requests.get(url_p).json()
            prezzo_numero = res.get('EUR', 87420.10)
            # Formatta con i puntini e la virgola corretta
            prezzo_btc = f"€ {prezzo_numero:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except:
            prezzo_btc = "€ 87.420,10" # Backup se internet fallisce

        # Affidabilità dinamica (cambia leggermente per far vedere che il bot lavora)
        import random
        percentuale = f"{random.randint(97, 99)}%" 
        # ---------------------------------------

        ora_attuale = datetime.now().strftime("%H:%M:%S")
        
        # Recupera le notizie vere dal mercato
        vere_notizie = get_real_news()
        
        status_web = {
            "status": "OPERATIVO",
            "price": prezzo_btc,         # Ora questo cambierà!
            "signal": "BULLISH",
            "reliability": percentuale,  # Ora questo cambierà!
            "last_update": ora_attuale,
            "ticker": f"BTC/EUR: {prezzo_btc} • KEYGAP SIGNAL: BULLISH • STATUS: ONLINE • UPDATE: {ora_attuale} • ",
            "news": vere_notizie
        }
        
        # Scrive il file JSON per il sito
        with open("market_status.json", "w") as j:
            json.dump(status_web, j, indent=4)
        
        # Esegue il push su GitHub
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"🚀 Keygap System Update {ora_attuale}"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        print(f"✅ SITO AGGIORNATO: Prezzo {prezzo_btc} e News alle: {ora_attuale}")
        
    except Exception as e:
        print(f"❌ Errore aggiornamento sito GitHub: {e}")

if __name__ == "__main__":
    print("🤖 Keygap AdVantage - Bot Avviato. Operatività in background attiva.")
    while True:
        ora_ora = datetime.now().hour
        minuto_ora = datetime.now().minute
        
        if (ora_ora == 8 and minuto_ora == 30) or (ora_ora == 20 and minuto_ora == 30):
            pubblica()
            time.sleep(65)
        
        run_update()
        time.sleep(300)