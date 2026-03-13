import os, pickle, json, subprocess, time, requests, random
from datetime import datetime

# --- CONFIGURAZIONE PERCORSI ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
REPORT_DIR = os.path.join(BASE_DIR, "Report_Finanziari")

# Assicuriamoci che la cartella esista all'avvio
if not os.path.exists(REPORT_DIR):
    os.makedirs(REPORT_DIR)

def get_real_news():
    """Recupera le news con gestione robusta degli errori di slicing."""
    try:
        url = "https://min-api.cryptocompare.com/data/v2/news/?lang=EN"
        r = requests.get(url, timeout=10).json()
        
        # Verifichiamo che la chiave 'Data' esista e sia una lista
        news_data = r.get('Data', [])
        if not isinstance(news_data, list):
            raise ValueError("Formato dati news non valido")

        news_list = []
        # Prendiamo le prime 6 news in modo sicuro
        for item in news_data[:6]:
            t = datetime.fromtimestamp(item.get('published_on', time.time())).strftime('%H:%M')
            news_list.append({
                "time": t, 
                "text": item.get('title', 'Analisi in corso...'),
                "link": item.get('url', '#') 
            })
        return news_list
    except Exception as e:
        print(f"⚠️ Nota: Recupero news in standby ({e})")
        return [{"time": "SYS", "text": "Sincronizzazione flussi globali in corso...", "link": "#"}]

def update_index_github():
    """Rigenera l'archivio HTML con indici corretti per la data."""
    try:
        if not os.path.exists(REPORT_DIR): os.makedirs(REPORT_DIR)
        
        reports = sorted([f for f in os.listdir(REPORT_DIR) if f.endswith('.html')], reverse=True)
        links_html = ""
        
        for r in reports[:30]:
            try:
                # Esempio file: Report_Mondiale_13_03_2026_12_41.html
                parti = r.replace('.html', '').split('_')
                
                if len(parti) >= 7:
                    # Indici corretti per il formato Mondiale_GG_MM_AAAA_HH_MM
                    giorno = parti[-5]
                    mese = parti[-4]
                    anno = parti[-3]
                    ora = f"{parti[-2]}:{parti[-1]}"
                    
                    data_display = f"{giorno}.{mese}.{anno}"
                    ora_display = ora
                else:
                    data_display = "REPORT"
                    ora_display = "--:--"

                links_html += f"""
                <a href="Report_Finanziari/{r}" style="display: flex; align-items: center; background: #0d1117; border: 1px solid rgba(0, 229, 255, 0.1); padding: 18px 25px; border-radius: 12px; text-decoration: none; color: #fff; margin-bottom: 12px; border-left: 5px solid #00e5ff; transition: 0.3s;">
                    <div style="display: flex; gap: 25px; align-items: center; flex-grow: 1;">
                        <div style="display: flex; flex-direction: column; min-width: 90px; border-right: 1px solid rgba(255,255,255,0.1); padding-right: 20px; text-align: center;">
                            <span style="color: #00e5ff; font-family: 'JetBrains Mono'; font-size: 0.85rem; font-weight: 700;">{data_display}</span>
                            <span style="color: rgba(255,255,255,0.4); font-family: 'JetBrains Mono'; font-size: 0.7rem;">{ora_display}</span>
                        </div>
                        <div>
                            <div style="font-size: 1.05rem; font-weight: 800; letter-spacing: 1px; text-transform: uppercase;">ANALISI MERCATO GLOBALE</div>
                            <div style="font-family: 'JetBrains Mono'; font-size: 0.6rem; color: #00ff88; margin-top: 4px; letter-spacing: 2px;">STATUS: DECRIPTATO // INTELLIGENCE_CORE</div>
                        </div>
                    </div>
                    <div style="background: rgba(0, 255, 136, 0.1); color: #00ff88; padding: 6px 12px; border-radius: 4px; font-size: 0.65rem; font-weight: 900; border: 1px solid rgba(0, 255, 136, 0.2); font-family: 'JetBrains Mono';">SECURE</div>
                </a>"""
            except: continue

        # Scrittura archivio
        with open(os.path.join(BASE_DIR, "archivio.html"), "w", encoding='utf-8') as f:
            f.write(f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>KEYGAP | Archive</title>
            <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@700&family=Outfit:wght@700&display=swap" rel="stylesheet">
            <style>body{{background:#05070a;color:#fff;font-family:'Outfit',sans-serif;padding:40px;}} .container{{max-width:850px;margin:0 auto;}}
            h1{{font-family:'JetBrains Mono';border-bottom:2px solid #00e5ff;padding-bottom:20px;letter-spacing:3px;display:flex;justify-content:space-between;}}
            .btn-back{{color:#00e5ff;text-decoration:none;font-size:0.8rem;border:1px solid #00e5ff;padding:8px 16px;border-radius:6px;}}</style>
            </head><body><div class="container"><h1>ARCHIVIO <a href="index.html" class="btn-back">← TERMINALE</a></h1>{links_html}</div></body></html>""")
    except Exception as e:
        print(f"⚠️ Errore Archivio: {e}")

def run_update():
    """Esegue il ciclo di intelligence e push su GitHub."""
    try:
        # Prezzo BTC
        try:
            res = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=EUR", timeout=5).json()
            p_num = res.get('EUR', 60000.0)
        except: p_num = 60000.0
        
        prezzo_btc = f"€ {p_num:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        ora_attuale = datetime.now().strftime("%H:%M")
        vere_notizie = get_real_news()
        
        # Template HTML (Versione compatta per velocità)
        html_report = f"""<!DOCTYPE html><html lang="it"><head><meta charset="UTF-8">
        <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Outfit:wght@700;900&display=swap" rel="stylesheet">
        <style>:root{{--bg:#05070a;--acc:#00e5ff;--panel:#0d1117;}} body{{background:var(--bg);color:#fff;font-family:'Outfit',sans-serif;padding:40px;display:flex;justify-content:center;}}
        .report-container{{max-width:750px;width:100%;background:var(--panel);padding:40px;border-radius:25px;border:1px solid rgba(0,229,255,0.2);border-top:6px solid var(--acc);}}
        .title-main{{font-family:'JetBrains Mono';font-size:1.4rem;color:var(--acc);}} .price-value{{font-size:3rem;font-weight:900;}}
        .news-item{{padding:12px;border-bottom:1px solid rgba(255,255,255,0.05);}}</style></head>
        <body><div class="report-container"><div class="title-main">KEYGAP INTELLIGENCE REPORT</div>
        <div style="text-align:right; font-family:'JetBrains Mono'; font-size:0.7rem; color:gray;">ID: {random.randint(1000,9999)} | {datetime.now().strftime('%d/%m/%Y')}</div>
        <div style="background:rgba(0,0,0,0.3);padding:30px;margin:20px 0;border-radius:15px;text-align:center;">
        <div style="color:var(--acc);font-size:0.8rem;letter-spacing:2px;">BITCOIN MARKET VALUE</div><div class="price-value">{prezzo_btc}</div></div>
        <div style="color:var(--acc);font-family:'JetBrains Mono';font-size:0.9rem;margin-bottom:10px;">GLOBAL FEED</div>
        {''.join([f'<div class="news-item"><span style="color:var(--acc);font-family:monospace;">[{n["time"]}]</span> {n["text"]}</div>' for n in vere_notizie[:5]])}
        <div style="text-align:center;margin-top:30px;font-size:0.6rem;color:rgba(255,255,255,0.2);">KEYGAP_ADVANTAGE CORE - SECURE DOCUMENT</div></div></body></html>"""

        # Salvataggio sicuro
        if not os.path.exists(REPORT_DIR): os.makedirs(REPORT_DIR)
        filename = f"Report_Mondiale_{datetime.now().strftime('%d_%m_%Y_%H_%M')}.html"
        filepath = os.path.join(REPORT_DIR, filename)
        
        with open(filepath, "w", encoding='utf-8') as f:
            f.write(html_report)

        update_index_github()
        
        # Git Push
        subprocess.run(["git", "add", "."], check=True, cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"📊 Update {ora_attuale}"], check=True, cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main", "--force"], check=True, cwd=BASE_DIR)
        
        print(f"✅ [KEYGAP] Sincronizzazione completata alle {ora_attuale}")

    except Exception as e:
        print(f"❌ Errore critico: {e}")

if __name__ == "__main__":
    print("🚀 KEYGAP_ADVANTAGE CORE - Online.")
    while True:
        run_update()
        print("💤 Standby 30 minuti...")
        time.sleep(1800)