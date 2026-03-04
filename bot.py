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
    return "QUANTUM_ENGINE: Sincronizzazione flussi in corso..."

# --- DATI ---
ora_attuale = datetime.datetime.now() + datetime.timedelta(hours=1) 
ora_esatta = ora_attuale.strftime("%H:%M")
id_v = ora_attuale.strftime("%Y%m%d%H%M%S")
testo = ottieni_contenuto()

# --- LAYOUT MASTER 3.0 ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KEYGAP | QUANTUM ADVANTAGE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --neon: #00f2ff; --bg: #010204; }}
        body {{ background: var(--bg); color: #fff; font-family: 'Rajdhani', sans-serif; margin: 0; }}
        
        .neon-glow {{
            color: var(--neon);
            text-shadow: 0 0 15px rgba(0, 242, 255, 1);
            font-family: 'Orbitron', sans-serif;
            text-transform: uppercase;
        }}

        .main-title {{
            font-size: clamp(2rem, 6vw, 5rem);
            font-weight: 900;
            color: var(--neon);
            text-shadow: 0 0 30px rgba(0, 242, 255, 0.4);
            line-height: 0.9;
            margin: 40px 0;
            font-style: italic;
        }}

        .glass-panel {{
            background: rgba(15, 20, 30, 0.8);
            border: 1px solid rgba(0, 242, 255, 0.3);
            border-radius: 30px;
            overflow: hidden;
            box-shadow: 0 0 50px rgba(0,0,0,0.8);
        }}

        .neon-btn {{
            border: 1px solid var(--neon);
            color: var(--neon);
            padding: 10px 20px;
            border-radius: 12px;
            font-family: 'Orbitron', sans-serif;
            font-size: 10px;
            transition: 0.3s;
            background: transparent;
        }}
        .neon-btn:hover {{ background: var(--neon); color: #000; box-shadow: 0 0 20px var(--neon); }}
        
        /* Container specifico per forzare la Heatmap */
        .heatmap-container {{ height: 400px; width: 100%; }}
    </style>
</head>
<body class="p-4 md:p-8">

    <nav class="flex justify-between items-center max-w-[1600px] mx-auto mb-12">
        <div>
            <h1 class="neon-glow text-3xl tracking-[10px]">Keygap</h1>
            <p class="text-[9px] tracking-[4px] opacity-50">High-Frequency Intelligence</p>
        </div>
        <div id="clock" class="neon-glow text-xl">00:00:00</div>
    </nav>

    <div class="max-w-[1600px] mx-auto text-center">
        <h2 class="main-title uppercase italic">"{testo}"</h2>
        
        <div class="flex flex-wrap justify-center gap-4 mb-12">
            <button onclick="change('BINANCE:BTCUSDT')" class="neon-btn">Bitcoin</button>
            <button onclick="change('TVC:GOLD')" class="neon-btn">Gold</button>
            <button onclick="change('INDEX:SPX')" class="neon-btn">S&P 500</button>
            <button onclick="change('FX:EURUSD')" class="neon-btn">EUR/USD</button>
        </div>

        <div class="glass-panel h-[650px] mb-12">
            <iframe id="mainChart" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&style=3" width="100%" height="100%" frameborder="0"></iframe>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-20">
            
            <div class="glass-panel p-6">
                <h3 class="neon-glow text-[11px] mb-4 text-left tracking-widest">Market Heatmap</h3>
                <div class="heatmap-container">
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-crypto-coins-heatmap.js" async>
                    {{
                      "symbolGroups": [
                        {{ "name": "Coins", "symbols": [
                          {{ "name": "BINANCE:BTCUSDT" }}, {{ "name": "BINANCE:ETHUSDT" }},
                          {{ "name": "BINANCE:SOLUSDT" }}, {{ "name": "BINANCE:BNBUSDT" }},
                          {{ "name": "BINANCE:XRPUSDT" }}, {{ "name": "BINANCE:ADAUSDT" }}
                        ] }}
                      ],
                      "colorTheme": "dark",
                      "isTransparent": false,
                      "hasSymbolTooltip": true,
                      "locale": "it",
                      "displayMode": "regular",
                      "width": "100%",
                      "height": "100%"
                    }}
                    </script>
                </div>
            </div>

            <div class="glass-panel p-6">
                <h3 class="neon-glow text-[11px] mb-4 text-left tracking-widest">Economic Pulse</h3>
                <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=dark&isTransparent=false&locale=it" width="100%" height="400" frameborder="0"></iframe>
            </div>

        </div>
    </div>

    <footer class="text-center py-12 opacity-20 border-t border-white/5">
        <div class="neon-glow text-[10px] tracking-[15px]">Keygap Terminal // {id_v}</div>
    </footer>

    <script>
        function updateClock() {{
            document.getElementById('clock').textContent = new Date().toLocaleTimeString('it-IT', {{ hour12: false }});
        }}
        setInterval(updateClock, 1000);
        updateClock();

        function change(s) {{
            const f = document.getElementById('mainChart');
            f.src = `https://s.tradingview.com/widgetembed/?symbol=${{s}}&theme=dark&style=3&v=${{Date.now()}}`;
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
        subprocess.run(["git", "commit", "-m", f"V13-HEATMAP-FIX {ora_esatta}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR)
except Exception as e:
    print(f"ERROR: {{e}}")
