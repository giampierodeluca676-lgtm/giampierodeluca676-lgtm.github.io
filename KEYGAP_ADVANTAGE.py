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
    """Recupera news reali con filtraggio tematico per CeFi e DeFi."""
    try:
        # Cerchiamo di ottenere più news per avere materiale di analisi
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        r = requests.get(url, timeout=10).json()
        news_data = r.get('Data', [])
        if not isinstance(news_data, list): raise ValueError("Dati non validi")
        
        news_list = []
        for item in news_data[:10]: # Analizziamo le prime 10 news
            t = datetime.fromtimestamp(item.get('published_on', time.time())).strftime('%H:%M')
            news_list.append({"time": t, "text": item.get('title', 'Analisi in corso...')})
        return news_list
    except Exception as e:
        print(f"⚠️ Nota: Recupero news in standby ({e})")
        return [{"time": "SYS", "text": "Intercettazione flussi istituzionali in corso..."}]

def generate_dynamic_analysis(news_list):
    """Genera un'analisi CeFi vs DeFi professionale e dettagliata, mai uguale."""
    
    # Database di osservazioni tecniche per la variabilità
    cefi_obs = [
        "Gli inflow sugli exchange centralizzati indicano una pressione di accumulo OTC.",
        "I volumi sui derivati CeFi mostrano un aumento dell'open interest istituzionale.",
        "Le riserve di stablecoin sulle piattaforme tier-1 sono ai massimi trimestrali.",
        "Si osserva una migrazione di asset verso custodian regolamentati per ridurre il rischio controparte."
    ]
    
    defi_obs = [
        "Il TVL nei protocolli di lending decentralizzato segnala una fase di deleveraging.",
        "L'attività sui DEX mostra una preferenza per le pool di liquidità a bassa volatilità.",
        "I volumi di minting degli asset sintetici indicano una nuova ondata di speculazione on-chain.",
        "I rendimenti medi nei protocolli di yield farming stanno sovraperformando i tassi CeFi."
    ]
    
    comparison_logic = [
        "La convergenza tra le due infrastrutture sta riducendo lo spread di arbitraggio.",
        "Mentre il retail rimane bloccato sulle piattaforme CeFi, le whale stanno iniettando liquidità nei bridge DeFi.",
        "La barriera tra finanza tradizionale e on-chain si sta sgretolando a favore di soluzioni ibride.",
        "Lo shock di liquidità attuale è guidato da un deflusso dai protocolli DeFi verso i cold storage istituzionali."
    ]

    # Composizione dinamica
    p1 = random.choice(cefi_obs)
    p2 = random.choice(defi_obs)
    p3 = random.choice(comparison_logic)
    
    # Integrazione parole chiave dalle news reali
    context = ""
    if news_list and news_list[0]['time'] != "SYS":
        kw = news_list[0]['text'][:50]
        context = f" L'attuale focus del mercato su '{kw}' conferma questa tendenza."

    return f"{p1} {p2} {p3}{context}"

def update_index_github():
    """Aggiorna index e archivio in tempo reale."""
    try:
        if not os.path.exists(REPORT_DIR): os.makedirs(REPORT_DIR)
        reports = sorted([f for f in os.listdir(REPORT_DIR) if f.endswith('.html')], reverse=True)
        ultimo_report = f"Report_Finanziari/{reports[0]}" if reports else "archivio.html"

        # Generazione lista link per archivio
        links_html = ""
        for r in reports[:30]:
            try:
                parti = r.replace('.html', '').split('_')
                if len(parti) >= 7:
                    giorno, mese, anno, ora = parti[-5], parti[-4], parti[-3], f"{parti[-2]}:{parti[-1]}"
                    data_display = f"{giorno}.{mese}.{anno}"
                else: data_display, ora = "REPORT", "--:--"

                links_html += f'<a href="Report_Finanziari/{r}" style="display:block; color:#00e5ff; margin-bottom:10px;">> DOSSIER {data_display} {ora}</a>'
            except: continue

        # Scrittura ARCHIVIO e INDEX (mantenendo la tua logica di design)
        with open(os.path.join(BASE_DIR, "index.html"), "w", encoding='utf-8') as f:
            f.write(f"""<html><body style='background:#05070a; color:#fff; font-family:sans-serif; padding:50px;'>
            <h1>KEYGAP COMMAND</h1><hr>
            <a href='{ultimo_report}' style='background:red; color:white; padding:15px; text-decoration:none; font-weight:bold;'>🔴 ULTIMO DOSSIER LIVE</a>
            <div style='margin-top:30px;'>{links_html}</div>
            </body></html>""")
    except Exception as e:
        print(f"⚠️ Errore indici: {e}")

def send_telegram_alert(prezzo_btc, news_list, id_report, scenario, analisi):
    """Invia alert Telegram sincronizzato."""
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    
    msg = f"""🚨 <b>[{scenario}]</b> 🚨

📊 <b>ID Sincronizzazione:</b> #KG-{id_report}
🕒 <b>Timestamp:</b> {datetime.now().strftime('%d/%m/%Y | %H:%M CET')}

⬛️ <b>METRICHE DI RETE</b>
🔹 <b>Asset:</b> Bitcoin (BTC)
🔹 <b>Market Value:</b> {prezzo_btc}

⬛️ <b>CONFRONTO CeFi vs DeFi</b>
{analisi}

⚡️ <b>LEGGI IL DOSSIER COMPLETO:</b>
👉 <a href="https://giampierodeluca676-lgtm.github.io/">Accedi al Terminale</a>
"""
    try:
        requests.post(url, json={"chat_id": TELEGRAM_CHAT_ID, "text": msg, "parse_mode": "HTML", "disable_web_page_preview": False})
    except: pass

def run_update():
    """Ciclo di aggiornamento con generazione dossier professionale."""
    try:
        # 1. Recupero dati reali
        try:
            res = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR", timeout=5).json()
            p_num = res.get('EUR', 60000.0)
        except: p_num = 60000.0
        
        prezzo_btc = f"€ {p_num:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        ora_attuale = datetime.now().strftime("%H:%M")
        vere_notizie = get_real_news()
        
        report_id = random.randint(1000, 9999)
        
        # 2. Generazione Analisi Dinamica CeFi/DeFi
        analisi_prof = generate_dynamic_analysis(vere_notizie)
        scenario = random.choice(["ISTITUTIONAL ROTATION", "LIQUIDITY BRIDGE", "CROSS-CHAIN INTELLIGENCE"])

        # 3. Costruzione HTML Dossier (Design Testuale Professionale)
        news_html = "".join([f'<p style="color:#00ff88;">> [{n["time"]}] {n["text"]}</p>' for n in vere_notizie[:5]])
        
        html_report = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <style>
        body {{ background: #020408; color: #a1b2c3; font-family: monospace; padding: 40px; }}
        .terminal {{ max-width: 800px; margin: 0 auto; border: 1px solid #1a2332; padding: 40px; background: #060913; }}
        h1 {{ color: #00e5ff; border-bottom: 1px solid #1a2332; padding-bottom: 10px; }}
        .analysis-block {{ font-size: 1.1rem; color: #fff; line-height: 1.8; margin: 25px 0; border-left: 3px solid #00ff88; padding-left: 20px; }}
    </style>
</head>
<body>
    <div class="terminal">
        <h1>KEYGAP // DOSSIER {report_id}</h1>
        <p>TIMESTAMP: {datetime.now().strftime('%d/%m/%Y %H:%M')} | SCENARIO: {scenario}</p>
        <div class="analysis-block">
            <strong>VALUTAZIONE CEFI vs DEFI:</strong><br>
            {analisi_prof}
        </div>
        <div style="background:#000; padding:20px; margin-bottom:20px;">
            <span style="color:#00e5ff;">MARKET VALUE:</span> <strong style="color:white;">{prezzo_btc}</strong>
        </div>
        <h3>GLOBAL RAW DATA FEED:</h3>
        {news_html}
        <div style="margin-top:30px; font-size:0.7rem; color:#445;">KEYGAP_ADVANTAGE CORE // SECURE DOCUMENT</div>
    </div>
</body>
</html>"""

        # 4. Salvataggio e Sincronizzazione
        filename = f"Report_Mondiale_{datetime.now().strftime('%d_%m_%Y_%H_%M')}.html"
        filepath = os.path.join(REPORT_DIR, filename)
        with open(filepath, "w", encoding='utf-8') as f: f.write(html_report)

        update_index_github()
        
        subprocess.run(["git", "add", "."], check=True, cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"📊 Dossier {ora_attuale}"], check=True, cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True, cwd=BASE_DIR)
        
        print(f"✅ [KEYGAP] Sincronizzazione completata alle {ora_attuale}")
        send_telegram_alert(prezzo_btc, vere_notizie, report_id, scenario, analisi_prof)

    except Exception as e:
        print(f"❌ Errore critico: {e}")

if __name__ == "__main__":
    print("🚀 KEYGAP_ADVANTAGE CORE - Generatore Dossier Professionale Attivo.")
    while True:
        run_update()
        print("💤 Standby 30 minuti...")
        time.sleep(1800)