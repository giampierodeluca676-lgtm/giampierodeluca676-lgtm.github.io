import os
import pickle
import json  # Aggiunto per la tabella web
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
    
    # 1. Contenuto per il Blog (Aggiornato alla proiezione)
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

    # --- AGGIUNTA: SALVATAGGIO AUTOMATICO SUL DESKTOP ---
    path_desktop = os.path.join(os.path.expanduser("~"), "Desktop", "REPORT_SOCIAL_OGGI.txt")
    
    report_text = f"""⚡ KEYGAP QUANTUM UPDATE {data_label} ⚡
🟢 STATUS: OPERATIVO

Il sistema ha isolato nuove impronte digitali istituzionali.
PROIEZIONE BTC: {prezzo_btc} (Price Discovery) 🚀

Link Blog: {posts['url']}
Terminale Live: https://giampierodeluca676-lgtm.github.io/

#Keygap #HFT #Bitcoin2026 #Trading #PriceDiscovery"""

    with open(path_desktop, "w") as f:
        f.write(report_text)
    
    print(f"📂 Report salvato correttamente sul Desktop: {path_desktop}")

    # --- NUOVA IMPLEMENTAZIONE: DATI PER TABELLA MARKET STATUS ---
    # Questo file serve alla index.html per riempire la tabella web
    market_status_data = {
        "last_update": data_label,
        "price": prezzo_btc,
        "status": "OPERATIVO",
        "signal": "BULLISH",
        "reliability": "98%"
    }
    
    with open('market_status.json', 'w') as json_file:
        json.dump(market_status_data, json_file, indent=4)
    
    print("📊 Dati Market Status generati in market_status.json")
    # ---------------------------------------------------

if __name__ == '__main__':
    publish_post()
