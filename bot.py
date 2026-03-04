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
    return "QUANTUM_LINK: Analisi dei flussi istituzionali in corso..."

# --- DATI ---
ora_attuale = datetime.datetime.now() + datetime.timedelta(hours=1) 
ora_esatta = ora_attuale.strftime("%H:%M")
id_v = ora_attuale.strftime("%Y%m%d%H%M%S")
testo = ottieni_contenuto()

# --- LAYOUT "THE GALAXY" 3D ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KEYGAP | QUANTUM TERMINAL</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --neon: #00f2ff; --bg: #030406; }}
        body {{ 
            background: var(--bg); color: #e0e6ed; font-family: 'Rajdhani', sans-serif;
            perspective: 2000px; margin: 0; overflow-x: hidden;
        }}
        
        /* CARD PROFESSIONALI CON PROFONDITÀ */
        .module-card {{
            background: rgba(255, 255, 255, 0.01);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 25px;
            box-shadow: 0 30px 60px rgba(0,0,0,0.8);
            transition: all 0.5s ease;
            height: 100%;
            display: flex;
            flex-direction: column;
        }}
        .module-card:hover {{
            transform: translateY(-10px) translateZ(20px);
            border-color: var(--neon);
            box-shadow: 0 0 40px rgba(0, 242, 255, 0.1);
        }}

        .neon-title {{
            font-family: 'Orbitron', sans-serif;
            font-size: 10px;
            letter-spacing: 4px;
            color: var(--neon);
            text-transform: uppercase;
            border-bottom: 1px solid rgba(0, 242, 255, 0.2);
            padding-bottom: 15px;
            margin-bottom: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}

        .btn-tech {{
            background: rgba(255, 255, 255, 0.03);
            border: 1px solid rgba(0, 242, 255, 0.2);
            padding: 8px 15px;
            border-radius: 10px;
            font-size: 10px;
            color: white;
            transition: 0.3s;
        }}
        .btn-tech:hover {{ background: var(--neon); color: black; box-shadow: 0 0 15px var(--neon); }}

        iframe {{ border-radius: 15px; flex-grow: 1; }}
        
        /* ANIMAZIONI */
        .dot {{ width: 6px; height: 6px; background: var(--neon); border-radius: 50%; animation: pulse 1.5s infinite; }}
        @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.3; }} 100% {{ opacity: 1; }} }}
    </style>
</head>
<body class="p-4 md:p-8">

    <header class="max-w-[1800px] mx-auto mb-12 flex justify-between items-end border-b border-white/5 pb-6">
        <div>
            <h1 class="font-black text-4xl tracking-[15px] uppercase italic text-white">Keygap <span class="text-cyan-400">Advantage</span></h1>
            <p class="text-[9px] tracking-[6px] uppercase opacity-40 mt-2">Professional Trading Intelligence System v.11.0</p>
        </div>
        <div class="text-right">
            <div id="clock" class="text-3xl font-bold tracking-widest text-white/80">00:00:00</div>
            <div class="text-[9px] text-cyan-400 uppercase tracking-widest mt-1">Status: Operational</div>
        </div>
    </header>

    <div class="max-w-[1800px] mx-auto grid grid-cols-1 lg:grid-cols-12 gap-8">
        
        <aside class="lg:col-span-3 space-y-8">
            <div class="module-card p-6">
                <div class="neon-title"><div class="dot"></div> Market Heatmap</div>
                <iframe src="https://s.tradingview.com/embed-widget/crypto-mcap/?locale=it&theme=dark" width="100%" height="300" frameborder="0"></iframe>
            </div>
            <div class="module-card p-6">
                <div class="neon-title"><div class="dot"></div> Top Assets Flow</div>
                <iframe src="https://s.tradingview.com/embed-widget/screener/?market=crypto&theme=dark" width="100%" height="400" frameborder="0"></iframe>
            </div>
        </aside>

        <main class="lg:col-span-6 space-y-8">
            <div class="module-card p-8 border-t-2 border-cyan-500/50">
                <div class="flex justify-center gap-3 mb-10">
                    <button onclick="change('BINANCE:BTCUSDT')" class="btn-tech italic font-bold">BITCOIN</button>
                    <button onclick="change('TVC:GOLD')" class="btn-tech italic font-bold">GOLD</button>
                    <button onclick="change('INDEX:SPX')" class="btn-tech italic font-bold">S&P 500</button>
                    <button onclick="change('FX:EURUSD')" class="btn-tech italic font-bold">EUR/USD</button>
                </div>
                
                <div class="text-center mb-10">
                    <h2 class="text-4xl md:text-6xl font-black uppercase tracking-tighter leading-none italic text-white mb-6">
                        "{testo}"
                    </h2>
                    <div class="h-[2px] w-24 bg-cyan-500 mx-auto opacity-50"></div>
                </div>

                <div class="h-[600px] rounded-3xl overflow-hidden border border-white/10 shadow-2xl bg-black">
                    <iframe id="mainChart" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&style=3" width="100%" height="100%" frameborder="0"></iframe>
                </div>
            </div>
        </main>

        <aside class="lg:col-span-3 space-y-8">
            <div class="module-card p-6">
                <div class="neon-title" style="color:#ff0055; border-color:rgba(255,0,85,0.2);"><div class="dot" style="background:#ff0055;"></div> Technical Gauge</div>
                <iframe src="https://s.tradingview.com/embed-widget/technical-analysis/?symbol=BINANCE:BTCUSDT&theme=dark" width="100%" height="350" frameborder="0"></iframe>
            </div>
            <div class="module-card p-6">
                <div class="neon-title"><div class="dot"></div> Economic Pulse</div>
                <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=dark&isTransparent=true" width="100%" height="350" frameborder="0"></iframe>
            </div>
        </aside>

    </div>

    <footer class="mt-20 p-12 text-center opacity-20 border-t border-white/5">
        <div class="tracking-[20px] text-[10px] uppercase text-white">Keygap Advantage Intelligence // {id_v}</div>
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
        subprocess.run(["git", "commit", "-m", f"V11-DASHBOARD-PRO {ora_esatta}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR)
except Exception as e:
    print(f"ERROR: {{e}}")
