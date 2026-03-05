import os, subprocess, datetime, smtplib, time
from email.mime.text import MIMEText

# --- CONFIGURAZIONE ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTICOLI_PATH = os.path.join(BASE_DIR, "articoli_pronti")

# Credenziali Fornite
EMAIL_MITTENTE = "giampierodeluca676@gmail.com"
EMAIL_PASSWORD = "nrznrbyfannkxdtb" # La tua Password per le App (senza spazi)
EMAIL_BLOGGER = "giampierodeluca676.keygap_insights@blogger.com"
ID_PROFILO_FB = "61587728495758"

def ottieni_contenuto():
    ora = datetime.datetime.now().hour
    file_target = "mattina.txt" if 5 <= ora < 15 else "sera.txt"
    path_file = os.path.join(ARTICOLI_PATH, file_target)
    if os.path.exists(path_file):
        with open(path_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "QUANTUM_LINK: Accesso ai nodi di borsa completato..."

# --- FUNZIONI AUTOMAZIONE SOCIAL ---

def pubblica_su_blogger(contenuto):
    print("Inviando post a Blogger...")
    titolo = f"Keygap Insights Update - {datetime.datetime.now().strftime('%d/%m/%Y')}"
    msg = MIMEText(contenuto)
    msg['Subject'] = titolo
    msg['From'] = EMAIL_MITTENTE
    msg['To'] = EMAIL_BLOGGER

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_MITTENTE, EMAIL_PASSWORD)
            server.sendmail(EMAIL_MITTENTE, EMAIL_BLOGGER, msg.as_string())
        print("✅ Blogger: Post inviato con successo.")
    except Exception as e:
        print(f"❌ Errore Blogger: {e}")

def pubblica_su_facebook(contenuto):
    try:
        import pyautogui
        print("Avvio automazione Facebook (Brave)...")
        # 1. Navigazione
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(1)
        pyautogui.write(f"https://www.facebook.com/profile.php?id={ID_PROFILO_FB}")
        pyautogui.press('enter')
        time.sleep(10) # Tempo per caricamento profilo

        # 2. Apertura Box Post
        pyautogui.press('p')
        time.sleep(5)
        
        # 3. Scrittura Testo
        pyautogui.write(contenuto, interval=0.05)
        time.sleep(3)

        # 4. Navigazione 8 TAB verso 'Pubblica'
        print("Navigazione con 8 TAB...")
        for _ in range(8):
            pyautogui.press('tab')
            time.sleep(0.3)
        
        # 5. Invio
        pyautogui.press('enter')
        print("✅ Facebook: Post condiviso correttamente.")
    except ImportError:
        print("⚠️ PyAutoGUI non installato. Salto Facebook.")
    except Exception as e:
        print(f"❌ Errore Facebook: {e}")

# --- GENERAZIONE HTML ---
ora_attuale = datetime.datetime.now() + datetime.timedelta(hours=1) 
ora_esatta = ora_attuale.strftime("%H:%M")
id_v = ora_attuale.strftime("%Y%m%d%H%M%S")
testo = ottieni_contenuto()

HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KEYGAP | ELITE TERMINAL</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --neon: #00f2ff; --bg: #010204; }}
        body {{ background: var(--bg); color: #fff; font-family: 'Rajdhani', sans-serif; margin: 0; }}
        .neon-glow {{ color: var(--neon); text-shadow: 0 0 20px rgba(0, 242, 255, 1); font-family: 'Orbitron', sans-serif; }}
        .main-title {{ font-size: clamp(2rem, 6vw, 5.5rem); font-weight: 900; color: var(--neon); text-shadow: 0 0 40px rgba(0, 242, 255, 0.5); line-height: 0.9; margin: 50px 0; font-style: italic; }}
        .quant-panel {{ background: #0a0b0d; border: 1px solid rgba(255, 255, 255, 0.05); border-top: 2px solid var(--neon); border-radius: 10px; box-shadow: 0 50px 80px rgba(0,0,0,0.9); }}
        .btn-command {{ border: 1px solid var(--neon); color: var(--neon); padding: 20px 45px; border-radius: 4px; font-family: 'Orbitron', sans-serif; font-size: 15px; font-weight: 900; letter-spacing: 4px; transition: 0.3s; background: rgba(0, 242, 255, 0.02); }}
        .btn-command:hover {{ background: var(--neon); color: #000; box-shadow: 0 0 50px rgba(0, 242, 255, 0.3); transform: scale(1.05); }}
        .heatmap-box {{ height: 550px; width: 100%; background: #131722; padding: 5px; }}
        .panel-header {{ padding: 15px 25px; background: rgba(255,255,255,0.02); border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; justify-content: space-between; }}
    </style>
</head>
<body class="p-6 md:p-12">
    <nav class="flex justify-between items-center max-w-[1700px] mx-auto mb-16 border-b border-white/5 pb-8">
        <div><h1 class="neon-glow text-4xl tracking-[15px]">Keygap</h1><p class="text-[10px] tracking-[8px] opacity-40 uppercase">Institutional Trading Desk</p></div>
        <div class="text-right"><div id="clock" class="neon-glow text-2xl">00:00:00</div></div>
    </nav>
    <div class="max-w-[1700px] mx-auto text-center">
        <h2 class="main-title uppercase italic">"{testo}"</h2>
        <div class="flex flex-wrap justify-center gap-8 mb-20">
            <button onclick="change('BINANCE:BTCUSDT')" class="btn-command">Bitcoin</button>
            <button onclick="change('TVC:GOLD')" class="btn-command">Gold</button>
            <button onclick="change('INDEX:SPX')" class="btn-command">S&P 500</button>
            <button onclick="change('FX:EURUSD')" class="btn-command">EUR / USD</button>
        </div>
        <div class="quant-panel mb-16">
            <div class="panel-header"><span class="text-[10px] uppercase font-bold text-white/50">Market_Core_Visualizer</span></div>
            <div class="h-[750px]"><iframe id="mainChart" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&style=3" width="100%" height="100%" frameborder="0"></iframe></div>
        </div>
        <div class="quant-panel mb-20">
            <div class="panel-header"><span class="neon-glow text-[11px] tracking-[5px]">Global Asset Distribution Heatmap</span></div>
            <div class="heatmap-box">
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-crypto-coins-heatmap.js" async>
                {{ "symbolGroups": [ {{ "name": "Market Leaders", "symbols": [ {{ "name": "BINANCE:BTCUSDT" }}, {{ "name": "BINANCE:ETHUSDT" }}, {{ "name": "BINANCE:SOLUSDT" }}, {{ "name": "BINANCE:BNBUSDT" }}, {{ "name": "BINANCE:XRPUSDT" }}, {{ "name": "BINANCE:ADAUSDT" }}, {{ "name": "BINANCE:DOTUSDT" }}, {{ "name": "BINANCE:LINKUSDT" }} ] }} ], "colorTheme": "dark", "isTransparent": false, "hasSymbolTooltip": true, "locale": "it", "displayMode": "regular", "width": "100%", "height": "100%" }}
                </script>
            </div>
        </div>
    </div>
    <footer class="text-center py-20 border-t border-white/5 opacity-20"><div class="neon-glow text-[10px] tracking-[20px]">Keygap Terminal // {id_v}</div></footer>
    <script>
        function updateClock() {{ document.getElementById('clock').textContent = new Date().toLocaleTimeString('it-IT', {{ hour12: false }}); }}
        setInterval(updateClock, 1000); updateClock();
        function change(s) {{ document.getElementById('mainChart').src = `https://s.tradingview.com/widgetembed/?symbol=${{s}}&theme=dark&style=3&v=${{Date.now()}}`; }}
    </script>
</body>
</html>
'''

try:
    # 1. Scrittura file HTML locale
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML_MASTER)
    
    # 2. Sincronizzazione GitHub (se non in Actions)
    if "GITHUB_ACTIONS" not in os.environ:
        subprocess.run(["git", "add", "."], cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"V16-ELITE-FULL-AUTO {ora_esatta}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR)
        
        # 3. Post Social
        pubblica_su_blogger(testo)
        pubblica_su_facebook(testo)

except Exception as e:
    print(f"❌ ERROR: {e}")
