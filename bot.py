import os, subprocess, datetime

# --- CONFIGURAZIONE ---
REPO_PATH = os.path.expanduser("~") + "/Desktop/Keygap_AdVantage"
ARTICOLI_PATH = os.path.join(REPO_PATH, "articoli_pronti")

def ottieni_contenuto():
    ora = datetime.datetime.now().hour
    file_target = "mattina.txt" if 5 <= ora < 15 else "sera.txt"
    path_file = os.path.join(ARTICOLI_PATH, file_target)
    if os.path.exists(path_file):
        with open(path_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "ANALISI DI MERCATO: In attesa di nuovi dati algoritmici..."

testo_notizia = ottieni_contenuto()
ora_esatta = datetime.datetime.now().strftime("%H:%M")

# --- LAYOUT PROFESSIONAL DASHBOARD ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KEYGAP ADVANTAGE | Terminal</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background-color: #0a0a0a; color: #e5e5e5; font-family: 'Inter', sans-serif; overflow-x: hidden; }}
        .glass {{ background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.1); }}
        .neon-border {{ border-left: 4px solid #3b82f6; }}
        @keyframes pulse-red {{ 0%, 100% {{ opacity: 1; }} 50% {{ opacity: 0.5; }} }}
        .live-dot {{ height: 8px; width: 8px; background-color: #ef4444; border-radius: 50%; display: inline-block; animation: pulse-red 1s infinite; }}
    </style>
</head>
<body class="p-2 md:p-4">

    <header class="glass mb-4 p-4 rounded-lg border-l-4 border-red-600">
        <div class="flex items-center justify-between mb-2">
            <span class="text-xs font-bold tracking-widest uppercase text-red-500">
                <span class="live-dot mr-2"></span>LIVE MARKET ULTIMATUM
            </span>
            <span class="text-xs text-gray-500 font-mono">{ora_esatta} - SERVER: OPERATIONAL</span>
        </div>
        <h1 class="text-2xl md:text-3xl font-black italic tracking-tighter text-white uppercase">
            {testo_notizia}
        </h1>
    </header>

    <div class="glass mb-4 rounded-lg overflow-hidden">
        <iframe src="https://s.tradingview.com/embed-widget/ticker-tape/?symbols=BINANCE:BTCUSDT,BINANCE:ETHUSDT,NASDAQ:AAPL,NASDAQ:TSLA,FX:EURUSD,TVC:GOLD&theme=dark" width="100%" height="46" frameborder="0"></iframe>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-4">
        
        <div class="lg:col-span-2 glass rounded-lg p-2 h-[500px] md:h-[600px]">
            <iframe src="https://s.tradingview.com/widgetembed/?symbol=NASDAQ:AAPL&theme=dark&interval=D" width="100%" height="100%" frameborder="0"></iframe>
        </div>

        <div class="flex flex-col gap-4">
            <div class="glass rounded-lg p-4 flex-1">
                <h3 class="text-sm font-bold text-blue-400 mb-3 uppercase tracking-wider">Analisi Tecnica</h3>
                <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=NASDAQ:AAPL&theme=dark&interval=1D" width="100%" height="100%" frameborder="0"></iframe>
            </div>
            
            <div class="glass rounded-lg p-4 h-48">
                <h3 class="text-sm font-bold text-green-400 mb-2 uppercase tracking-wider">Stato Sistema</h3>
                <div class="space-y-2 text-xs font-mono">
                    <div class="flex justify-between border-b border-gray-800 pb-1"><span>BOT STATUS:</span> <span class="text-green-500">ACTIVE</span></div>
                    <div class="flex justify-between border-b border-gray-800 pb-1"><span>CAPITAL:</span> <span>€ 500,00</span></div>
                    <div class="flex justify-between border-b border-gray-800 pb-1"><span>MODE:</span> <span class="text-yellow-500">PAPER TRADING</span></div>
                    <div class="flex justify-between"><span>BRANCH:</span> <span class="text-blue-500">MAIN</span></div>
                </div>
            </div>
        </div>
    </div>

    <footer class="mt-4 text-center text-[10px] text-gray-600 uppercase tracking-[0.2em]">
        Keygap AdVantage © 2026 - Proprietary Algorithmic Terminal
    </footer>

</body>
</html>
'''

try:
    os.chdir(REPO_PATH)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_MASTER)
    
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Dashboard Pro Update {ora_esatta}"])
    result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ DASHBOARD AGGIORNATA: Il sito è ora in modalità professionale!")
    else:
        print(f"❌ ERRORE: {result.stderr}")

except Exception as e:
    print(f"❌ ERRORE CRITICO: {e}")