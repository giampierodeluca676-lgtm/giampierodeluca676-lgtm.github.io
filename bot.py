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

# --- LAYOUT V14 MASTER ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KEYGAP | QUANTUM COMMAND</title>
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
            background: rgba(15, 20, 30, 0.85);
            border: 1px solid rgba(0, 242, 255, 0.3);
            border-radius: 35px;
            overflow: hidden;
            box-shadow: 0 0 60px rgba(0,0,0,0.9);
        }}

        /* PULSANTI GIGANTI E PROFESSIONALI */
        .btn-command {{
            border: 2px solid var(--neon);
            color: var(--neon);
            padding: 18px 40px;
            border-radius: 20px;
            font-family: 'Orbitron', sans-serif;
            font-size: 14px;
            font-weight: 900;
            letter-spacing: 3px;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
            background: rgba(0, 242, 255, 0.03);
            text-transform: uppercase;
            cursor: pointer;
        }}
        .btn-command:hover {{ 
            background: var(--neon); 
            color: #000; 
            box-shadow: 0 0 40px var(--neon); 
            transform: translateY(-8px) scale(1.05);
        }}
        .btn-command:active {{ transform: scale(0.95); }}
        
        .heatmap-container {{ height: 450px; width: 100%; }}
    </style>
</head>
<body class="p-4 md:p-10">

    <nav class="flex justify-between items-center max-w-[1700px] mx-auto mb-16">
        <div>
            <h1 class="neon-glow text-4xl tracking-[12px]">Keygap</h1>
            <p class="text-[10px] tracking-[6px] opacity-60">Intelligence & Quantum Trading</p>
        </div>
        <div id="clock" class="neon-glow text-2xl">00:00:00</div>
    </nav>

    <div class="max-w-[1700px] mx-auto text-center">
        <h2 class="main-title uppercase italic">"{testo}"</h2>
        
        <div class="flex flex-wrap justify-center gap-6 mb-16">
            <button onclick="change('BINANCE:BTCUSDT')" class="btn-command">Bitcoin</button>
            <button onclick="change('TVC:GOLD')" class="btn-command">Gold</button>
            <button onclick="change('INDEX:SPX')" class="btn-command">S&P 500</button>
            <button onclick="change('FX:EURUSD')" class="btn-command">EUR / USD</button>
        </div>

        <div class="glass-panel h-[700px] mb-16">
            <iframe id="mainChart" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&style=3" width="100%" height="100%" frameborder="0"></iframe>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-2 gap-10 mb-20">
            
            <div class="glass-panel p-8">
                <h3 class="neon-glow text-[12px] mb-6 text-left tracking-[5px]">Global Crypto Heatmap</h3>
                <div class="heatmap-container">
                    <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-crypto-coins-heatmap.js" async>
                    {{
                      "symbolGroups": [
                        {{ "name": "Main Assets", "symbols": [
                          {{ "name": "BINANCE:BTCUSDT" }}, {{ "name": "BINANCE:ETHUSDT" }},
                          {{ "name": "BINANCE:SOLUSDT" }}, {{ "name": "BINANCE:BNBUSDT" }},
                          {{ "name": "BINANCE:XRPUSDT" }}, {{ "name": "BINANCE:ADAUSDT" }},
                          {{ "name": "BINANCE:DOTUSDT" }}, {{ "name": "BINANCE:LINKUSDT" }}
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

            <div class="glass-panel p-8">
                <h3 class="neon-glow text-[12px] mb-6 text-left tracking-[5px]">Macro Economic Events</h3>
                <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=dark&isTransparent=false&locale=it" width="100%" height="450" frameborder="0"></iframe>
            </div>

        </div>
    </div>

    <footer class="text-center py-16 opacity-30 border-t border-white/5">
        <div class="neon-glow text-[11px] tracking-[20px]">Keygap Terminal // {id_v}</div>
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
            setTimeout(() => f.style.opacity = '1', 400);
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
        subprocess.run(["git", "commit", "-m", f"V14-BIG-BUTTONS {ora_esatta}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR)
except Exception as e:
    print(f"ERROR: {{e}}")
