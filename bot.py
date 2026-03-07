import os, pickle, json, subprocess, time
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

def pubblica():
    """Crea un post SEO-friendly per spingere gli utenti sul sito con Adsterra"""
    try:
        service = get_service()
        ora = datetime.now().strftime("%d/%m/%Y %H:%M")
        
        # Titolo con nomenclatura Keygap
        titolo = f"Keygap AdVantage - Report Mercato {ora}"
        
        # Testo formattato in HTML per inserire il link cliccabile
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
    """Aggiorna il sito per simulare attività e mantenere l'indicizzazione"""
    try:
        prezzo_btc = "€ 87.420,10"
        ora_attuale = datetime.now().strftime("%H:%M:%S")
        status_web = {
            "status": "OPERATIVO",
            "price": prezzo_btc,
            "signal": "BULLISH",
            "reliability": "98%",
            "last_update": ora_attuale,
            "ticker": f"BTC/EUR: {prezzo_btc} • KEYGAP SIGNAL: BULLISH • STATUS: ONLINE • UPDATE: {ora_attuale} • "
        }
        with open("market_status.json", "w") as j:
            json.dump(status_web, j, indent=4)
        
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"🚀 Keygap System Update {ora_attuale}"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        print(f"✅ SITO GITHUB AGGIORNATO ALLE: {ora_attuale}")
    except Exception as e:
        print(f"❌ Errore aggiornamento sito GitHub: {e}")

if __name__ == "__main__":
    print("🤖 Keygap AdVantage - Bot Avviato. Operatività in background attiva.")
    while True:
        ora_ora = datetime.now().hour
        minuto_ora = datetime.now().minute
        
        # Pubblica su Blogger esattamente alle 08:30 e 20:30
        if (ora_ora == 8 and minuto_ora == 30) or (ora_ora == 20 and minuto_ora == 30):
            pubblica()
            time.sleep(65) # Dorme 65 secondi per evitare che pubblichi 2 volte nello stesso minuto
        
        # Aggiorna il sito GitHub ogni 5 minuti
        run_update()
        time.sleep(300)