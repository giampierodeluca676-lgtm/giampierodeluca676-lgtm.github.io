import os
import json
import time
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle

# CONFIGURAZIONE
BLOG_ID = '8423232148419688536'
SCOPES = ['https://www.googleapis.com/auth/blogger']
# PERCORSO INTERNO ALLA CARTELLA DEL PROGETTO
LOCAL_REPORT_DIR = os.path.join(os.getcwd(), "Report_Finanziari")

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
    now = datetime.now()
    ora = now.strftime("%H:%M")
    data = now.strftime("%d/%m/%Y")
    nome_file = now.strftime("%Y-%m-%d_%H-%M")
    
    titolo = f"Keygap Insights - Report {data} ({ora})"
    contenuto = f"""
    <h2>Analisi di Mercato delle {ora}</h2>
    <p>Il sistema Keygap ha generato il report automatico programmato.</p>
    <ul>
        <li><b>Asset:</b> BTC/EUR</li>
        <li><b>Data:</b> {data}</li>
        <li><b>Status:</b> Live Terminal</li>
    </ul>
    <p>Guarda i grafici in tempo reale qui: <a href="https://giampierodeluca676-lgtm.github.io/">Keygap Advantage</a></p>
    """
    return titolo, contenuto, nome_file

def pubblica():
    titolo, contenuto, nome_file = crea_report()
    
    # Salvataggio nella cartella del progetto
    file_path = os.path.join(LOCAL_REPORT_DIR, f"report_{nome_file}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"<html><body><h1>{titolo}</h1>{contenuto}</body></html>")
    
    # Invio a Blogger
    try:
        service = get_blogger_service()
        body = {"kind": "blogger#post", "title": titolo, "content": contenuto}
        service.posts().insert(blogId=BLOG_ID, body=body).execute()
        print(f"[{datetime.now().strftime('%H:%M')}] Report salvato in 'Report_Finanziari' e inviato a Blogger.")
    except Exception as e:
        print(f"Errore: {e}")

print("Bot Blogger Attivo. Report programmati alle 08:30 e 20:30.")
print(f"I file verranno salvati in: {LOCAL_REPORT_DIR}")

if True:
    ora_attuale = datetime.now().strftime("%H:%M")
    if ora_attuale in ["08:30", "20:30"]:
        pubblica()
        time.sleep(61)
    time.sleep(30)
