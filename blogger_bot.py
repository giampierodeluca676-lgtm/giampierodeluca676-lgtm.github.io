import os
import time
import pickle
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# CONFIGURAZIONE CORE
BLOG_ID = '2744764892823107807'
SCOPES = ['https://www.googleapis.com/auth/blogger']
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

def pubblica():
    now = datetime.now()
    ora = now.strftime("%H:%M")
    data = now.strftime("%d/%m/%Y")
    nome_file = now.strftime("%Y-%m-%d_%H-%M")
    
    titolo = f"Keygap Advantage: Analisi Strategica CeFi/DeFi - {data} ({ora})"
    
    # ARTICOLO PROFESSIONALE NARRATIVO
    contenuto = f"""
    <div style="font-family: 'Helvetica', Arial, sans-serif; line-height: 1.6; color: #e1e1e1; background-color: #121212; max-width: 800px; margin: auto; padding: 30px; border-radius: 10px;">
        <h1 style="color: #4dadff; border-bottom: 1px solid #333; padding-bottom: 10px;">Market Intelligence Report</h1>
        <p style="font-style: italic; color: #888;">Sessione operativa Keygap Advantage - {data} {ora}</p>
        
        <p>L'attuale configurazione degli asset <b>BTC/EUR</b> mostra una fase di consolidamento strutturale. Il monitoraggio Keygap sta analizzando i flussi di liquidità tra gli exchange centralizzati (CeFi) e i principali protocolli di prestito decentralizzati (DeFi).</p>
        
        <h2 style="color: #4dadff;">Monitoraggio CeFi & Risk Management</h2>
        <p>L'operatività tramite BingX rimane stabile. Il sistema mantiene rigorosamente un <b>capital floor di 500 unità</b> in modalità virtual trading, garantendo la sicurezza del setup prima di ogni transizione verso il trading reale. Gli algoritmi di protezione sono attivi per prevenire drawdown eccessivi.</p>
        
        <h2 style="color: #4dadff;">Integrazione DeFi & On-Chain Data</h2>
        <p>Sul fronte DeFi, stiamo mappando i cluster di liquidità che definiscono i nuovi supporti dinamici. La convergenza tra i dati centralizzati e quelli on-chain permette al bot di identificare aree di inefficienza sfruttabili dal protocollo Keygap.</p>
        
        <div style="background-color: #1e1e1e; border-left: 4px solid #4dadff; padding: 15px; margin: 20px 0;">
            <b>Stato del Sistema:</b> Battleground Mode Attiva. Nessuna restrizione rilevata.
        </div>
        
        <p>Consulta i dati in tempo reale qui: <a href="https://giampierodeluca676-lgtm.github.io/" style="color: #4dadff;">Dashboard Ufficiale</a></p>
    </div>
    """
    
    # SALVATAGGIO LOCALE
    file_path = os.path.join(LOCAL_REPORT_DIR, f"report_{nome_file}.html")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"<html><body style='background-color:#000;'>{contenuto}</body></html>")
    
    # INVIO BLOGGER
    try:
        service = get_blogger_service()
        body = {"kind": "blogger#post", "title": titolo, "content": contenuto}
        service.posts().insert(blogId=BLOG_ID, body=body).execute()
        print(f"✅ [{ora}] Post professionale pubblicato e salvato in locale.")
    except Exception as e:
        print(f"❌ [{ora}] Errore critico: {e}")

if __name__ == "__main__":
    print("🔥 KEYGAP ADVANTAGE BOT: Monitoraggio orari 08:30 e 20:30 attivo.")
    while True:
        ora_attuale = datetime.now().strftime("%H:%M")
        if ora_attuale in ["08:30", "20:30"]:
            pubblica()
            time.sleep(61)  # Evita invii multipli nello stesso minuto
        time.sleep(30)
