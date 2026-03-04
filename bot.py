import os, subprocess, datetime

# --- CONFIGURAZIONE ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTICOLI_PATH = os.path.join(BASE_DIR, "articoli_pronti")

def ottieni_contenuto():
    ora = datetime.datetime.now().hour
    file_target = "mattina.txt" if 5 <= ora < 15 else "sera.txt"
    path_file = os.path.join(ARTICOLI_PATH, file_target)
    if os.path.exists(path_file):
        with open(path_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "SYSTEM_ACTIVE: Sincronizzazione flussi quantistici in corso..."

# --- DATI ---
ora_attuale = datetime.datetime.now() + datetime.timedelta(hours=1) 
ora_esatta = ora_attuale.strftime("%H:%M")
id_v = ora_attuale.strftime("%Y%m%d%H%M%S")
testo = ottieni_contenuto()

# --- LAYOUT NEON IMMERSIVO ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KEYGAP | NEON QUANTUM</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --neon: #00f2ff; --bg: #010204; }}
        body {{ 
            background: var(--bg); color: #fff; font-family: 'Rajdhani', sans-serif;
            margin: 0; overflow-x: hidden;
        }}
        
        .neon-glow {{
            color: var(--neon);
            text-shadow: 0 0 10px rgba(0, 242, 255, 0.8), 0 0 20px rgba(0, 242, 255, 0.4);
            font-family: 'Orbitron', sans-serif;
        }}

        .glass-panel {{
            background: rgba(10, 15, 25, 0.7);
            border: 1px solid rgba(0, 242, 255, 0.2);
            border-radius: 35px;
            box-shadow: 0 0 30px rgba(0,0,0,0.5);
        }}

        .neon-btn {{
            background: transparent;
            border: 1px solid var(--neon);
            color: var(--neon);
            padding: 10px 20px;
            border-radius: 12px;
            font-family: 'Orbitron', sans-serif;
            font-size: 11px;
            text-transform: uppercase;
            box-shadow: inset 0 0 10px rgba(0, 242, 255, 0.2);
            transition: 0.3s;
        }}
        .neon-btn:hover {{
            background: var(--neon);
            color: #000;
            box-shadow: 0 0 25px var(--neon);
        }}

        .main-title {{
            font-size: clamp(2.5rem, 7vw, 5.5rem);
            font-weight: 900;
            text-transform: uppercase;
            line-height: 0.9;
            color: var(--neon);
            text-shadow: 0 0 30px rgba(0, 242, 255, 0.5);
        }}

        /* Fix per i widget vuoti: forziamo altezza e visibilità */
        .widget-container {{
            min-height: 350px;
            width: 100%;
            background: #131722; /* Colore nativo TradingView per evitare lo sfarfallio */
            border-radius: 20px;
            overflow: hidden;
        }}
    </style>
</head>
<body class="min-h-screen">

    <nav class="p-8 flex justify-between items-center max-w-[1600px] mx-auto">
        <div class="flex flex-col">
            <span class="neon-glow text-2xl tracking-[8px]">Keygap</span>
            <span class="text-[9px] tracking-[4px] text-white opacity-50 uppercase">Advanced Intelligence</span>
        </div>
        <div id="clock" class="neon-glow text-xl tracking-widest">00:00:00</div>
    </nav>

    <main class="max-w-[1600px] mx-auto px-6 py-8">
        
        <div class="text-center mb-16">
            <span class="neon-glow text-[10px] uppercase tracking-[5px] mb-6 block animate-pulse">● System Live Report</span>
            <h2 class="main-title italic mb-10">
                "{testo}"
            </h2>
            
            <div class="flex flex-wrap justify-center gap-4 mb-12">
                <button onclick="change('BINANCE:BTCUSDT')" class="neon-btn">Bitcoin</button>
                <button onclick="change('TVC:GOLD')" class="neon-btn">Gold</button>
                <button onclick="change('INDEX:SPX')" class="neon-btn">S&P 500</button>
                <button onclick="change('FX:EURUSD')" class="neon-btn">EUR / USD</button>
            </div>
        </div>

        <div class="glass-panel p-1 mb-16 h-[700px]">
            <iframe id="mainChart" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&style=3" width="100%" height="100%" frameborder="0"></iframe>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-20">
            <div class="glass-panel p-6">
                <h4 class="neon-glow text-[11px] uppercase mb-4">Technical Sentiment</h4>
                <div class="widget-container">
                    <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE:BTCUSDT&theme=dark&locale=it" width="100%" height="320" frameborder="0"></iframe>
                </div>
            </div>
            <div class="glass-panel p-6">
                <h4 class="neon-glow text-[11px] uppercase mb-4">Economic Pulse</h4>
                <div class="widget-container">
                    <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=dark&isTransparent=false&locale=it" width="100%" height="320" frameborder="0"></iframe>
                </div>
            </div>
            <div class="glass-panel p-6">
                <h4 class="neon-glow text-[11px] uppercase mb-4">Market Heatmap</h4>
                <div class="widget-container">
                    <iframe src="https://s.tradingview.com/embed-widget/crypto-mcap/?locale=it&theme=dark" width="100%" height="320" frameborder="0"></iframe>
                </div>
            </div>
        </div>

    </main>

    <footer class="py-12 text-center border-t border-white/5">
        <div class="neon-glow text-[9px] tracking-[10px] opacity-50">KEYGAP TERMINAL // Giampiero De Luca</div>
    </footer>

    <script>
        function updateClock() {{
            document.getElementById('clock').textContent = new Date().toLocaleTimeString('it-IT', {{ hour12: false }});
        }}
        setInterval(updateClock, 1000);
        updateClock();

        function change(s) {{
            const f = document.getElementById('mainChart');
            f.style.opacity = '0.4';
            f.src = `https://s.tradingview.com/widgetembed/?symbol=${{s}}&theme=dark&style=3&v=${{Date.now()}}`;
            setTimeout(() => f.style.opacity = '1', 500);
        }}
    </script>
    <script src="https://pl28819682.effectivegatecpm.com/07/47/37/074737f2d1be0f3c0e9de0585a695fd7.js"></script>
</body>
</html>
'''

try:
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML_MASTER)
    if "GITHUB_ACTIONS" not in os.environ:
        subprocess.run(["git", "add", "."], cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"FIX-NEON-HEATMAP {ora_esatta}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR)
except Exception as e:
    print(f"ERROR: {{e}}")
