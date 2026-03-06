import os
import pickle
import json
import subprocess
from datetime import datetime
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# Configurazione Google Blogger
SCOPES = ['https://www.googleapis.com/auth/blogger']
BLOG_ID = '2744764892823107807' 

def get_service():
    creds = None
    # Il file token.json memorizza le credenziali dell'utente
    if os.path.exists('token.json'):
        with open('token.json', 'rb') as token:
            creds = pickle.load(token)
    
    # Se non ci sono credenziali valide, l'utente deve accedere
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            # Carica il file scaricato e rinominato precedentemente
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Salva le credenziali per il prossimo avvio
        with open('token.json', 'wb') as token:
            pickle.dump(creds, token)
            
    return build('blogger', 'v3', credentials=creds)

def publish_post():
    try:
        service = get_service()
        
        # Dati del segnale (Puoi automatizzare questi valori in futuro)
        prezzo_btc = "€ 87.420,10"
        ora_attuale = datetime.now().strftime("%H:%M:%S")
        data_label = datetime.now().strftime("%d/%m")
        
        # 1. Pubblicazione su Blogger
        content = f"<p>Keygap AdVantage Update: {prezzo_btc} alle ore {ora_attuale}</p>"
        body = {
            'kind': 'blogger#post', 
            'title': f'Keygap - {data_label} - {ora_attuale}', 
            'content': content
        }
        
        print("🚀 Pubblicazione su Blogger in corso...")
        posts = service.posts().insert(blogId=BLOG_ID, body=body).execute()
        post_url = posts.get('url', 'https://giampierodeluca676.blogspot.com/')
        
        # 2. Salvataggio Report su Desktop
        path_desktop = os.path.join(os.path.expanduser("~"), "Desktop", "REPORT_SOCIAL_OGGI.txt")
        report_text = f"KEYGAP UPDATE\nBTC: {prezzo_btc}\nOra: {ora_attuale}\nStatus: OPERATIVO"
        with open(path_desktop, "w") as f:
            f.write(report_text)
        
        # 3. Aggiornamento Ponte Web (JSON COMPLETO per il sito)
        status_web = {
            "status": "OPERATIVO",
            "price": prezzo_btc,
            "signal": "BULLISH",
            "reliability": "98%",
            "last_update": ora_attuale,
            "last_post_title": f"⚠️ UPDATE: BTC {prezzo_btc}",
            "last_post_url": post_url,
            "ticker": f"BTC/EUR: {prezzo_btc} • STATUS: OPERATIVO • SIGNAL: BULLISH • UPDATE: {ora_attuale} • "
        }
        
        with open("market_status.json", "w") as j:
            json.dump(status_web, j, indent=4)
        
        # 4. Push automatico su GitHub
        print("📤 Sincronizzazione con il sito web...")
        subprocess.run(["git", "add", "market_status.json"], check=True)
        subprocess.run(["git", "commit", "-m", f"⚡ Auto-Update {ora_attuale}"], check=True)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True)
        
        print(f"✅ Successo! Sito aggiornato alle {ora_attuale}")

    except Exception as e:
        print(f"❌ Errore durante l'esecuzione: {e}")

if __name__ == "__main__":
    publish_post()