import os, pickle, json, subprocess, time
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/blogger']
BLOG_ID = '2744764892823107807'

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

def run_update():
    try:
        service = get_service()
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
        subprocess.run(["git", "commit", "-m", f"🚀 System Update {ora_attuale}"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        print(f"✅ SITO AGGIORNATO ALLE: {ora_attuale}")
    except Exception as e:
        print(f"❌ Errore: {e}")

if __name__ == "__main__":
    while True:
        run_update()
        print("In attesa del prossimo aggiornamento (60s)...")
        time.sleep(60)
