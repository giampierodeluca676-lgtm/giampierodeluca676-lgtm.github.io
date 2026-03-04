import os, subprocess, datetime, requests

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
    return "QUANTUM ENGINE: Analisi dei flussi istituzionali in corso. Rilevata bassa volatilità."

# --- GESTIONE DATI DINAMICI ---
ora_attuale = datetime.datetime.now() + datetime.timedelta(hours=1) 
ora_esatta = ora_attuale.strftime("%H:%M")
id_versione = ora_attuale.strftime("%Y%m%d%H%M%S")
testo_notizia = ottieni_contenuto()

# --- LAYOUT "QUANTUM DASHBOARD" ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KEYGAP | QUANTUM ADVANTAGE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Inter:wght@400;900&display=swap" rel="stylesheet">
    <style>
        html {{ scroll-behavior: smooth; }}
        body {{ background-color: #050505; color: #e0e0e0; font-family: 'Inter', sans-serif; overflow-x: hidden; }}
        .mono {{ font-family: 'JetBrains Mono', monospace; }}
        .glass {{ background: rgba(255, 255, 255, 0.03); backdrop-filter: blur(10px); border: 1px solid rgba(255,255,255,0.05); }}
        .neon-text {{ color: #00ff41; text-shadow: 0 0 10px rgba(0,255,65,0.5); }}
        .neon-border {{ border: 1px solid #00ff41; box-shadow: 0 0 15px rgba(0,255,65,0.2); }}
        .grid-bg {{ background-image: radial-gradient(rgba(0, 255, 65, 0.1) 1px, transparent 1px); background-size: 30px 30px; }}
        .scanline {{ width: 100%; height: 100px; background: linear-gradient(0deg, rgba(0,0,0,0) 0%, rgba(0,255,65,0.02) 50%, rgba(0,0,0,0) 100%); position: fixed; top: 0; animation: scan 8s linear infinite; pointer-events: none; z-index: 999; }}
        @keyframes scan {{ 0% {{ top: -100px; }} 100% {{ top: 100%; }} }}
        .pulse {{ animation: pulse 2s infinite; }}
        @keyframes pulse {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.4; }} 100% {{ opacity: 1; }} }}
    </style>
</head>
<body class="grid-bg">
    <div class="scanline"></div>

    <nav class="w-full border-b border-white/10 glass sticky top-0 z-50 px-4 py-2 flex justify-between items-center">
        <div class="flex items-center gap-6">
            <span class="mono text-[10px] uppercase tracking-tighter text-white/40">Terminal: <span class="text-white">KG-PRO</span></span>
            <span class="mono text-[10px] uppercase neon-text pulse hidden md:inline">Connected_Live</span>
        </div>
        <div class="mono text-[11px] font-bold">
            <span id="clock" class="neon-text">--:--:--</span>
        </div>
    </nav>

    <div class="max-w-[1600px] mx-auto p-4 md:p-6 grid grid-cols-1 lg:grid-cols-12 gap-6">
        <aside class="lg:col-span-3 space-y-4">
            <div class="glass p-4 rounded-sm border-l-2 border-green-500">
                <h3 class="mono text-[9px] text-white/50 mb-3 uppercase tracking-widest">Market_Scanner</h3>
                <iframe src="https://s.tradingview.com/embed-widget/screener/?market=crypto&theme=dark" width="100%" height="350" frameborder="0"></iframe>
            </div>
        </aside>

        <main class="lg:col-span-6 space-y-6">
            <div class="glass p-6 border border-white/10">
                <div class="flex justify-between items-start mb-6">
                    <span class="bg-white/10 text-white px-2 py-1 text-[9px] font-bold uppercase tracking-widest">Intelligence_Report</span>
                    <span class="mono text-[9px] text-white/20">v4.2</span>
                </div>
                <h2 class="text-3xl md:text-5xl font-black italic tracking-tighter text-white leading-none uppercase mb-8">
                    "{testo_notizia}"
                </h2>
                <div class="h-[500px] neon-border bg-black mb-6">
                    <iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&v={id_versione}" width="100%" height="100%" frameborder="0"></iframe>
                </div>
            </div>
        </main>

        <aside class="lg:col-span-3 space-y-6">
            <div class="glass p-4">
                <h3 class="mono text-[9px] text-white/50 mb-4 uppercase tracking-widest">Global_Events</h3>
                <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=dark&width=100%25&height=400" width="100%" height="400" frameborder="0"></iframe>
            </div>
        </aside>
    </div>

    <footer class="mt-12 border-t border-white/5 p-8 text-center mono">
        <p class="text-[9px] text-white/30 uppercase tracking-widest leading-loose">
            Keygap Advantage System // Build_ID: {id_versione}
        </p>
    </footer>

    <script>
        function updateClock() {{
            const now = new Date();
            document.getElementById('clock').textContent = now.toLocaleTimeString('it-IT', {{ hour12: false }});
        }}
        setInterval(updateClock, 1000);
        updateClock();
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
        subprocess.run(["git", "commit", "-m", f"QUANTUM-CORE {ora_esatta}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR)
except Exception as e:
    print(f"ERROR: {{e}}")
