import os
import pickle
import json
import subprocess
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

def publish_post():
    try:
        service = get_service()
        # Dati dinamici
        prezzo_btc = "€ 87.420,10"
        ora_attuale = datetime.now().strftime("%H:%M:%S")
        
        # 1. Blogger
        content = f"<p>Update Keygap: {prezzo_btc} alle {ora_attuale}</p>"
        body = {'kind': 'blogger#post', 'title': f'Keygap Advantage - {ora_attuale}', 'content': content}
        posts = service.posts().insert(blogId=BLOG_ID, body=body).execute()
        post_url = posts.get('url', 'https://giampierodeluca676.blogspot.com/')

        # 2. PONTE WEB (Il cuore del sito)
        status_web = {
            "status": "OPERATIVO",
            "price": prezzo_btc,
            "signal": "BULLISH",
            "reliability": "98%",
            "last_update": ora_attuale,
            "last_post_title": f"⚠️ ANALISI: BTC {prezzo_btc}",
            "last_post_url": post_url,
            "ticker": f"BTC/EUR: {prezzo_btc} • STATUS: OK • UPDATE: {ora_attuale} • "
        }
        
        with open("market_status.json", "w") as j:
            json.dump(status_web, j, indent=4)
        
        # 3. Sincronizzazione GitHub
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", f"🚀 Sincronizzazione Totale {ora_attuale}"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        
        print(f"\n✅ CAPOLAVORO! Sito aggiornato alle {ora_attuale}")
        print("👉 Controlla ora: https://giampierodeluca676-lgtm.github.io/")

    except Exception as e:
        print(f"❌ Errore: {e}")

if __name__ == "__main__":
    publish_post()
