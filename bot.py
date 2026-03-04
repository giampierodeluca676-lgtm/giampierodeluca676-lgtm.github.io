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
    return "QUANTUM_ENGINE: Sincronizzazione dati completata. Monitoraggio volatilità attivo."

# --- DATI DINAMICI ---
ora_attuale = datetime.datetime.now() + datetime.timedelta(hours=1) 
ora_esatta = ora_attuale.strftime("%H:%M")
id_v = ora_attuale.strftime("%Y%m%d%H%M%S")
testo = ottieni_contenuto()

# --- LAYOUT 3D ULTRA-PROFESSIONALE ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KEYGAP | 3D QUANTUM DESK</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;900&family=Rajdhani:wght@300;600;700&display=swap" rel="stylesheet">
    <style>
        :root {{ --neon: #00f2ff; --bg: #050608; }}
        body {{ 
            background: radial-gradient(circle at center, #10121a 0%, #050608 100%);
            color: #e0e6ed; font-family: 'Rajdhani', sans-serif;
            perspective: 2000px; overflow-x: hidden;
        }}
        .card-3d {{
            background: rgba(255, 255, 255, 0.02);
            backdrop-filter: blur(12px);
            border: 1px solid rgba(0, 242, 255, 0.1);
            border-radius: 24px;
            transform-style: preserve-3d;
            transform: rotateX(5deg) rotateY(-2deg);
            box-shadow: 0 25px 50px -12px rgba(0,0,0,0.7);
            transition: all 0.6s cubic-bezier(0.23, 1, 0.32, 1);
        }}
        .card-3d:hover {{
            transform: rotateX(0deg) rotateY(0deg) translateZ(30px);
            border-color: var(--neon);
            box-shadow: 0 0 40px rgba(0, 242, 255, 0.15);
        }}
        .neon-text {{ color: var(--neon); text-shadow: 0 0 12px rgba(0, 242, 255, 0.5); font-family: 'Orbitron', sans-serif; }}
        .glass-nav {{ background: rgba(5, 6, 8, 0.9); border-bottom: 1px solid rgba(0, 242, 255, 0.3); }}
    </style>
</head>
<body class="min-h-screen">

    <nav class="glass-nav sticky top-0 z-50 p-4 backdrop-blur-xl">
        <div class="max-w-[1500px] mx-auto flex justify-between items-center">
            <div class="flex items-center gap-4">
                <div class="w-2 h-2 bg-cyan-400 rounded-full animate-ping"></div>
                <h1 class="neon-text text-lg tracking-[6px] uppercase">Keygap <span class="text-white">Advantage</span></h1>
            </div>
            <div class="text-cyan-400 font-bold mono text-sm" id="clock">00:00:00</div>
        </div>
    </nav>

    <main class="max-w-[1500px] mx-auto p-6 grid grid-cols-1 lg:grid-cols-12 gap-8 mt-12">
        
        <aside class="lg:col-span-3">
            <div class="card-3d p-6 h-full">
                <h3 class="text-cyan-400 text-xs font-black uppercase mb-6 tracking-widest">Market Watch</h3>
                <div class="rounded-xl overflow-hidden border border-white/10 bg-[#131722]">
                    <iframe src="https://s.tradingview.com/embed-widget/screener/?market=crypto&theme=dark" width="100%" height="500" frameborder="0"></iframe>
                </div>
            </div>
        </aside>

        <section class="lg:col-span-6">
            <div class="card-3d p-8 border-t-4 border-t-cyan-500">
                <div class="flex justify-between mb-8">
                    <span class="text-[10px] bg-cyan-500/10 text-cyan-400 px-4 py-1 rounded-sm border border-cyan-500/20 uppercase font-black tracking-widest">Core_Active</span>
                    <span class="text-[10px] text-white/30 mono">V_9.1_STABLE</span>
                </div>
                <h2 class="text-3xl md:text-5xl font-bold mb-10 italic tracking-tighter uppercase leading-[0.9]">
                    "{testo}"
                </h2>
                <div class="rounded-2xl overflow-hidden shadow-2xl h-[550px] border border-white/5">
                    <iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&style=2&v={id_v}" width="100%" height="100%" frameborder="0"></iframe>
                </div>
            </div>
        </section>

        <aside class="lg:col-span-3">
            <div class="card-3d p-6 h-full">
                <h3 class="text-cyan-400 text-xs font-black uppercase mb-6 tracking-widest">Macro Events</h3>
                <div class="rounded-xl overflow-hidden border border-white/10">
                    <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=dark&isTransparent=true" width="100%" height="500" frameborder="0"></iframe>
                </div>
            </div>
        </aside>

    </main>

    <footer class="mt-24 p-12 text-center border-t border-white/5 opacity-30">
        <div class="text-[10px] uppercase tracking-[8px]">Keygap Terminal // {id_v}</div>
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
        subprocess.run(["git", "commit", "-m", f"UI-CORE-3D {ora_esatta}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR)
except Exception as e:
    print(f"ERROR: {{e}}")
