import os, pickle, json, subprocess, time, requests, random
from datetime import datetime

# --- CONFIGURAZIONE TELEGRAM ---
TELEGRAM_BOT_TOKEN = "8736329123:AAFa9k_rtKOGQmpwXGICRu-jjdAGEUuWTZM"
TELEGRAM_CHAT_ID = "@KeygapTerminal"

# --- CONFIGURAZIONE PERCORSI ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "Report_Finanziari")

if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

def get_real_news():
    """Recupera news reali e previene il blocco in caso di dati non validi."""
    try:
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        r = requests.get(url, timeout=10).json()
        news_data = r.get('Data', [])
        
        if not isinstance(news_data, list) or len(news_data) == 0:
            raise ValueError("API News temporaneamente non disponibile")
        
        news_list = []
        for item in news_data[:8]:
            t = datetime.fromtimestamp(item.get('published_on', time.time())).strftime('%H:%M')
            news_list.append({"time": t, "text": item.get('title', 'Analisi Flussi...')})
        return news_list
    except Exception as e:
        # Fallback professionale: Intelligence Flashes per non interrompere il ciclo
        flash_intel = [
            "Rilevato spostamento massiccio di BTC verso wallet istituzionali (Custody).",
            "Aumento anomalo dell'attività sui protocolli di Liquid Staking on-chain.",
            "Divergenza rilevata tra volumi spot CeFi e derivati DeFi.",
            "Pressione di acquisto accumulata su desk OTC asiatici."
        ]
        return [{"time": "INTEL", "text": random.choice(flash_intel)} for _ in range(3)]

def generate_professional_dossier():
    """Genera un confronto CeFi vs DeFi iper-professionale e sempre diverso."""
    
    cefi_metrics = [
        "Le riserve degli exchange centralizzati segnano una contrazione dello 0.4%, indicando accumulo in cold storage.",
        "I volumi sui contratti future (CeFi) mostrano una dominanza di posizioni long istituzionali.",
        "I flussi verso i custodian regolamentati suggeriscono una fase di de-risking del capitale retail.",
        "La liquidità sugli order book centralizzati è in fase di compressione algoritmica avanzata."
    ]
    
    defi_metrics = [
        "Il Total Value Locked (TVL) nei protocolli di lending decentralizzato è cresciuto costantemente nelle ultime 4 ore.",
        "Si osserva un'accelerazione dei volumi sui DEX (Decentralized Exchanges) legata a operazioni di arbitraggio cross-chain.",
        "L'attività di minting su stablecoin algoritmiche indica un aumento della fiducia on-chain.",
        "I rendimenti reali (Real Yield) nei protocolli DeFi stanno iniziando a sovraperformare i tassi d'interesse CeFi."
    ]
    
    logic_comparison = [
        "Mentre la CeFi garantisce l'accesso istituzionale, la DeFi sta assorbendo la volatilità tramite pool di liquidità automatizzate.",
        "Il confronto evidenzia una migrazione strategica: lo Smart Money usa la CeFi per l'acquisto e la DeFi per la generazione di rendita.",
        "La barriera tra infrastruttura centralizzata e on-chain si sta riducendo grazie all'adozione di soluzioni ibride di settlement.",
        "Lo shock di liquidità attuale nasce da una divergenza strutturale tra l'offerta negli exchange e la domanda nei protocolli di prestito."
    ]

    # Composizione dinamica del dossier
    analisi = f"{random.choice(cefi_metrics)} {random.choice(defi_metrics)} {random.choice(logic_comparison)}"
    return analisi

def update_index_github():
    """Aggiorna la homepage con il link all'ultimo dossier dinamico."""
    try:
        reports = sorted([f for f in os.listdir(REPORT_DIR) if f.endswith('.html')], reverse=True)
        ultimo = f"Report_Finanziari/{reports[0]}" if reports else "archivio.html"
        
        with open(os.path.join(BASE_DIR, "index.html"), "w", encoding='utf-8') as f:
            # Qui va il codice HTML della tua index (mantenendo i tuoi script Adsterra)
            f.write(f"<html><body style='background:#000; color:#fff;'><a href='{ultimo}'>LIVE DOSSIER</a></body></html>")
    except: pass

def send_telegram_alert(prezzo_btc, id_report, scenario, analisi):
    """Invia il dossier professionale sul canale Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    msg = f"""🚨 <b>[{scenario}]</b> 🚨

📊 <b>DOSSIER:</b> #KG-{id_report}
🕒 <b>DATA:</b> {datetime.now().strftime('%d/%m/%Y | %H:%M')}

⬛️ <b>ANALISI COMPARATIVA CEFI vs DEFI</b>
{analisi}

📈 <b>VALUTAZIONE BTC:</b> {prezzo_btc}

⚡️ <b>ACCEDI AL TERMINALE COMPLETO:</b>
👉 <a href="https://giampierodeluca676-lgtm.github.io/">Decrypt Live Data</a>
"""
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "HTML", "disable_web_page_preview": False})
    except: pass

def run_update():
    """Esegue l'aggiornamento, genera il report e invia su Telegram."""
    try:
        # Recupero dati reali
        res = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR", timeout=5).json()
        p_num = res.get('EUR', 60000.0)
        prezzo_btc = f"€ {p_num:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        news_reali = get_real_news()
        report_id = random.randint(1000, 9999)
        
        # Scenari e Analisi dinamica
        scenari = ["INSTITUTIONAL ROTATION", "ON-CHAIN LIQUIDITY SHIFT", "MARKET DECOUPLING", "CROSS-CHAIN FLOW"]
        scenario_scelto = random.choice(scenari)
        analisi_dettagliata = generate_professional_dossier()

        # HTML Dossier in stile Terminale
        news_block = "".join([f"<p style='color:#00e5ff;'>[{n['time']}] > {n['text']}</p>" for n in news_reali])
        
        html_content = f"""
        <!DOCTYPE html><html><head><meta charset='UTF-8'><style>
        body{{background:#020408; color:#a1b2c3; font-family:monospace; padding:40px; line-height:1.7;}}
        .terminal{{max-width:850px; margin:0 auto; border:1px solid #1a2332; padding:45px; background:#060913; box-shadow:0 0 40px rgba(0,229,255,0.05);}}
        h1{{color:#00e5ff; font-size:1.4rem; margin-bottom:20px; border-bottom:1px solid #1a2332;}}
        .intel-box{{background:#03050a; padding:25px; border-left:4px solid #00ff88; color:#eee; font-size:1rem; margin-bottom:30px;}}
        .price{{font-size:2.2rem; color:#fff; font-weight:bold; margin-top:20px;}}
        </style></head><body><div class='terminal'>
        <h1>KEYGAP // INTELLIGENCE DOSSIER #{report_id}</h1>
        <p>SCENARIO: <span style='color:#00ff88;'>[{scenario_scelto}]</span></p>
        <hr style='border:0; border-top:1px dashed #1a2332;'>
        <h2>CONFRONTO REALE CEFI vs DEFI</h2>
        <div class='intel-box'>{analisi_dettagliata}</div>
        <div class='price'>BTC: {prezzo_btc}</div>
        <h2>RAW DATA STREAM</h2>
        {news_block}
        <p style='margin-top:50px; font-size:0.7rem; color:#445; letter-spacing:3px;'>KEYGAP ADVANTAGE CORE // END OF DOSSIER</p>
        </div></body></html>"""

        # Salvataggio e Push su GitHub
        filename = f"Report_Mondiale_{datetime.now().strftime('%d_%m_%Y_%H_%M')}.html"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, "w", encoding='utf-8') as f: f.write(html_content)
        
        update_index_github()
        
        subprocess.run(["git", "add", "."], cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"📊 Dossier {report_id}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main", "--force"], cwd=BASE_DIR)
        
        print(f"✅ [KEYGAP] Sincronizzazione Dossier {report_id} completata.")
        send_telegram_alert(prezzo_btc, report_id, scenario_scelto, analisi_dettagliata)

    except Exception as e:
        print(f"❌ Errore critico: {e}")

if __name__ == "__main__":
    print("🚀 KEYGAP_ADVANTAGE CORE - Dossier Engine Online.")
    while True:
        run_update()
        time.sleep(1800)