import os
import pickle
import json
import subprocess  # <--- AGGIUNTO per il ponte GitHub
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Configurazione definitiva
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
    
    # Dati variabili
    prezzo_btc = "€87.420,10"
    data_label = "06/03"
    
    # 1. Contenuto per il Blog
    content = f"""
    <p>Dati di mercato aggiornati:</p>
    <ul>
        <li><b>Asset:</b> Bitcoin (BTC)</li>
        <li><b>Prezzo:</b> {prezzo_btc} (Price Discovery)</li>
        <li><b>Sito:</b> <a href="https://giampierodeluca676-lgtm.github.io/">Visita il sito ufficiale</a></li>
    </ul>
    """
    
    body = {
        'kind': 'blogger#post',
        'title': f'Keygap - Aggiornamento BTC {data_label}',
        'content': content
    }
    
    print("🚀 Invio post in corso...")
    posts = service.posts().insert(blogId=BLOG_ID, body=body).execute()
    print(f"✅ POST PUBBLICATO! Link: {posts['url']}")

    # --- REPORT SOCIAL ---
    path_desktop = os.path.join(os.path.expanduser("~"), "Desktop", "REPORT_SOCIAL_OGGI.txt")
    report_text = f"""⚡ KEYGAP QUANTUM UPDATE {data_label} ⚡\n🟢 STATUS: OPERATIVO\nLink Blog: {posts['url']}\n#Keygap #HFT #Bitcoin2026"""

    with open(path_desktop, "w") as f:
        f.write(report_text)

    # --- INIEZIONE PONTE GITHUB ---
    try:
        import subprocess
        market_status_data = {"last_update": data_label, "price": prezzo_btc, "status": "OPERATIVO", "signal": "BULLISH"}
        with open("market_status.json", "w") as j: json.dump(market_status_data, j)
        subprocess.run(["git", "add", "market_status.json"], check=True)
        subprocess.run(["git", "commit", "-m", "sync"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
    except Exception as e: print(f"Errore Sincronizzazione: {e}")
        f.write(report_text)
    
    # --- IMPLEMENTAZIONE PONTE STABILE ---
    market_status_data = {
        "last_update": data_label,
        "price": prezzo_btc,
        "status": "OPERATIVO",
        "signal": "BULLISH",
        "reliability": "98%"
    }
    
    with open('market_status.json', 'w') as json_file:
        json.dump(market_status_data, json_file, indent=4)
    
    # COMANDI PONTE: Spingono il JSON sul sito web automaticamente
    try:
        subprocess.run(["git", "add", "market_status.json"], check=True)
        subprocess.run(["git", "commit", "-m", "⚡ Web Update"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🌐 SITO AGGIORNATO: Il ponte è attivo.")
    except Exception as e:
        print(f"⚠️ Errore ponte: Assicurati di aver salvato le credenziali Git.")

if __name__ == '__main__':
    publish_post()