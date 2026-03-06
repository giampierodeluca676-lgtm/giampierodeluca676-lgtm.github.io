import os
import json
import time
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# CONFIGURAZIONE
BLOG_ID = '8423232148419688536' # Sostituisci con il tuo ID Blogger se diverso
SCOPES = ['https://www.googleapis.com/auth/blogger']
LOCAL_REPORT_DIR = os.path.expanduser("~/Desktop/Keygap_AdVantage/Report_Finanziari")

if not os.path.exists(LOCAL_REPORT_DIR):
    os.makedirs(LOCAL_REPORT_DIR)

def get_blogger_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('blogger', 'v3', credentials=creds)

def crea_report():
    ora = datetime.now().strftime("%H:%M")
    data = datetime.now().strftime("%Y-%m-%d")
    
    titolo = f"Keygap Insights - Report {data} ({ora})"
    contenuto = f"""
    <h2>Analisi di Mercato delle {ora}</h2>
    <p>Il sistema Keygap ha rilevato nuovi movimenti sui mercati crypto.</p>
    <ul>
        <li><b>BTC/EUR:</b> Analisi in corso...</li>
        <li><b>Sentiment:</b> Alta Volatilità</li>
    </ul>
    <p>Consulta il terminale live qui: <a href="https://giampierodeluca676-lgtm.github.io/">Keygap Advantage</a></p>
    """
    return titolo, contenuto, data, ora

def pubblica():
    titolo, contenuto, data, ora = crea_report()
    
    # Salva in locale
    file_path = os.path.join(LOCAL_REPORT_DIR, f"report_{data}_{ora.replace(':','-')}.html")
    with open(file_path, "w") as f:
        f.write(f"<h1>{titolo}</h1>{contenuto}")
    
    # Pubblica su Blogger
    try:
        service = get_blogger_service()
        body = {
            "kind": "blogger#post",
            "title": titolo,
            "content": contenuto
        }
        service.posts().insert(blogId=BLOG_ID, body=body).execute()
        print(f"[{ora}] Report pubblicato e salvato in locale.")
    except Exception as e:
        print(f"Errore pubblicazione: {e}")

# LOOP AUTONOMO
print("Bot Blogger Avviato. In attesa degli orari programmati...")
while True:
    ora_attuale = datetime.now().strftime("%H:%M")
    
    # Orari: Mattina 08:30 e Sera 20:30
    if ora_attuale in ["08:30", "20:30"]:
        pubblica()
        time.sleep(61) # Evita doppie pubblicazioni nello stesso minuto
    
    time.sleep(30)