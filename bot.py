import os
import pickle
import json
import subprocess
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
    service = get_service()
    prezzo_btc = "€87.420,10"
    data_label = "06/03"
    
    content = f"<p>BTC Update: {prezzo_btc}</p>"
    body = {'kind': 'blogger#post', 'title': f'Keygap - {data_label}', 'content': content}
    
    print("🚀 Pubblicazione...")
    posts = service.posts().insert(blogId=BLOG_ID, body=body).execute()
    
    # Salvataggio Desktop
    path_desktop = os.path.join(os.path.expanduser("~"), "Desktop", "REPORT_SOCIAL_OGGI.txt")
    report_text = f"KEYGAP UPDATE\nBTC: {prezzo_btc}\nStatus: OPERATIVO"
    with open(path_desktop, "w") as f:
        f.write(report_text)
    
    # Ponte Web
    status_web = {"price": prezzo_btc, "status": "OPERATIVO", "signal": "BULLISH"}
    with open("market_status.json", "w") as j:
        json.dump(status_web, j)
    
    # Push automatico
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "⚡ AutoSync"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        print("✅ Ponte stabilizzato e sito aggiornato!")
    except:
        print("⚠️ Errore Git (ma il post è uscito)")

if __name__ == '__main__':
    publish_post()
