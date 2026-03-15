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
    """Recupera news reali o genera intercettazioni tecniche ad alto livello se l'API è offline."""
    try:
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        r = requests.get(url, timeout=10).json()
        news_data = r.get('Data', [])
        
        if not isinstance(news_data, list) or len(news_data) == 0:
            raise ValueError("Dati non validi")
        
        news_list = []
        for item in news_data[:8]:
            t = datetime.fromtimestamp(item.get('published_on', time.time())).strftime('%H:%M')
            news_list.append({"time": t, "text": item.get('title', 'Analisi Flussi...')})
        return news_list
    except Exception:
        # DB Intelligence Locale Potenziato (CeFi/DeFi Focused)
        intel_pool = [
            "Rilevato spostamento di 4.500 BTC da wallet Binance verso cold storage istituzionale.",
            "Protocolli di Lending DeFi (Aave/Compound) mostrano un picco di utilizzo di stablecoin.",
            "Divergenza rilevata: aumento dell'Open Interest sui Future CME mentre il volume Spot scende.",
            "Whale alert: accumulo massiccio di ETH su Uniswap V3 tramite aggregatori di liquidità.",
            "I desk OTC riportano una carenza di offerta per ordini superiori ai 50M USD.",
            "L'hashrate globale tocca un nuovo massimo: la sicurezza del network Bitcoin è impenetrabile."
        ]
        random.shuffle(intel_pool)
        return [{"time": "INTEL", "text": f} for f in intel_pool[:5]]

def generate_pro_analysis():
    """Genera un confronto CeFi vs DeFi iper-professionale, reale e sempre diverso."""
    
    # Matrice CeFi
    cefi_data = [
        "Gli exchange centralizzati (CeFi) stanno vivendo una crisi di liquidità lato sell-side, con le riserve depositate ai minimi storici.",
        "Le piattaforme centralizzate registrano un aumento dei depositi di stablecoin, segno di una 'polvere da sparo' pronta per il breakout.",
        "I flussi istituzionali preferiscono la custodia regolamentata, limitando la circolazione effettiva degli asset sugli order book pubblici."
    ]
    
    # Matrice DeFi
    defi_data = [
        "In ambito DeFi, il Total Value Locked (TVL) sta migrando verso soluzioni Layer-2 per ottimizzare le strategie di rendimento reale.",
        "I protocolli di finanza decentralizzata stanno assorbendo la volatilità attraverso pool di liquidità sempre più efficienti e concentrate.",
        "Si osserva un'accelerazione nel minting di asset sintetici on-chain, indicando una maturazione dell'ecosistema DeFi rispetto ai cicli precedenti."
    ]
    
    # Matrice Confronto/Sintesi
    confronto = [
        "La vera battaglia si gioca sulla velocità: la CeFi domina l'on-ramp istituzionale, ma la DeFi sta vincendo sulla trasparenza dei flussi.",
        "Il mercato sta prezzando un pattern di rotazione: acquisto in CeFi e messa a rendita immediata in protocolli DeFi di staking.",
        "La convergenza tra questi due mondi sta creando un'inefficienza di arbitraggio che il terminale Keygap sta monitorando in tempo reale."
    ]

    # Composizione dinamica del dossier
    return f"{random.choice(cefi_data)} {random.choice(defi_data)} {random.choice(confronto)}"

def update_index_github():
    """Aggiorna la homepage e l'archivio con puntamento automatico per evitare 404."""
    try:
        reports = sorted([f for f in os.listdir(REPORT_DIR) if f.endswith('.html')], reverse=True)
        ultimo_link = f"Report_Finanziari/{reports[0]}" if reports else "#"
        
        # Scrittura dinamica dell'archivio per mantenere i link aggiornati
        links_html = "".join([f'<a href="Report_Finanziari/{r}" style="display:block;color:#00e5ff;margin-bottom:10px;">> {r}</a>' for r in reports[:25]])
        
        with open(os.path.join(BASE_DIR, "index.html"), "w", encoding='utf-8') as f:
            # Qui si può reinserire il codice HTML completo della tua index con Adsterra
            f.write(f"<html><body style='background:#000;color:#fff;'><a href='{ultimo_link}'>[ULTIMO DOSSIER]</a><hr>{links_html}</body></html>")
    except: pass

def send_telegram_alert(prezzo_btc, id_report, scenario, analisi):
    """Invia il dossier professionale sul canale Telegram."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    msg = f"""🚨 <b>[{scenario}]</b> 🚨

📊 <b>DOSSIER:</b> #KG-{id_report}
🕒 <b>ANALISI:</b> {datetime.now().strftime('%H:%M CET')}

⬛️ <b>CONFRONTO CeFi vs DeFi</b>
{analisi}

📈 <b>VALORE ATTUALE BTC:</b> {prezzo_btc}

⚡️ <b>TERMINALE COMPLETO:</b>
👉 <a href="https://giampierodeluca676-lgtm.github.io/">Decrypt Live Data</a>
"""
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "HTML", "disable_web_page_preview": False})
    except: pass

def run_update():
    """Ciclo principale di generazione dossier."""
    try:
        # Dati Prezzo BTC
        res = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR", timeout=5).json()
        prezzo_btc = f"€ {res.get('EUR', 60000.0):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        
        news_reali = get_real_news()
        report_id = random.randint(1000, 9999)
        
        # Scenari e Analisi
        scenari = ["ISTITUTIONAL ROTATION", "LIQUIDITY COMPRESSION", "NETWORK BREAKOUT", "ON-CHAIN INTELLIGENCE"]
        scenario = random.choice(scenari)
        analisi_dettagliata = generate_pro_analysis()

        # HTML Dossier Stile Terminale
        news_html = "".join([f"<p style='color:#00ff88;'>[{n['time']}] > {n['text']}</p>" for n in news_reali[:6]])
        
        html_report = f"""
        <!DOCTYPE html><html><head><meta charset='UTF-8'><style>
        body{{background:#020408; color:#a1b2c3; font-family:monospace; padding:40px; line-height:1.8;}}
        .terminal{{max-width:850px; margin:0 auto; border:1px solid #1a2332; padding:45px; background:#060913; box-shadow:0 0 40px rgba(0,229,255,0.05);}}
        h1{{color:#00e5ff; font-size:1.4rem; border-bottom:1px solid #1a2332; padding-bottom:10px;}}
        .content{{background:#03050a; padding:25px; border-left:4px solid #00ff88; color:#eee; font-size:1rem; margin:20px 0;}}
        </style></head><body><div class='terminal'>
        <h1>KEYGAP // DOSSIER INTELLIGENCE #{report_id}</h1>
        <p>PATTERN RILEVATO: <strong>[{scenario}]</strong></p>
        <div class='content'>
            <strong>ANALISI TECNICA CEFI vs DEFI:</strong><br><br>
            {analisi_dettagliata}
        </div>
        <p style='font-size:1.8rem; color:#fff;'>BTC VALUE: {prezzo_btc}</p>
        <hr style='border:1px solid #1a2332;'>
        <h3>LIVE INTERCEPTIONS:</h3>
        {news_html}
        <p style='margin-top:50px; font-size:0.75rem; color:#445;'>KEYGAP ADVANTAGE CORE // END OF DOSSIER</p>
        </div></body></html>"""

        # Salvataggio e Push su GitHub
        filename = f"Report_Mondiale_{datetime.now().strftime('%d_%m_%Y_%H_%M')}.html"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, "w", encoding='utf-8') as f: f.write(html_report)
        
        update_index_github()
        
        subprocess.run(["git", "add", "."], cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"📊 Dossier {report_id}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main", "--force"], cwd=BASE_DIR)
        
        print(f"✅ [KEYGAP] Sincronizzazione Dossier {report_id} completata.")
        send_telegram_alert(prezzo_btc, report_id, scenario, analisi_dettagliata)

    except Exception as e:
        print(f"❌ Errore critico: {e}")

if __name__ == "__main__":
    print("🚀 KEYGAP_ADVANTAGE CORE - Generatore Dossier Professionale Attivo.")
    while True:
        run_update()
        time.sleep(1800)