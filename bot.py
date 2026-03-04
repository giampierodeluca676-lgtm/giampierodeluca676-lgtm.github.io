import os, subprocess, datetime, requests

# --- CONFIGURAZIONE UNIVERSALE ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTICOLI_PATH = os.path.join(BASE_DIR, "articoli_pronti")
ADSTERRA_API_TOKEN = os.environ.get("ADSTERRA_TOKEN", "") 

def ottieni_contenuto():
    ora = datetime.datetime.now().hour
    file_target = "mattina.txt" if 5 <= ora < 15 else "sera.txt"
    path_file = os.path.join(ARTICOLI_PATH, file_target)
    if os.path.exists(path_file):
        with open(path_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "MARKET WATCH: I mercati globali mostrano segnali di consolidamento in attesa dei dati macro."

# --- GESTIONE ORARIO E ANTI-CACHE ---
ora_attuale = datetime.datetime.now() + datetime.timedelta(hours=1) 
ora_esatta = ora_attuale.strftime("%H:%M")
id_versione = ora_attuale.strftime("%Y%m%d%H%M%S")
testo_notizia = ottieni_contenuto()

# --- LAYOUT PREMIUM NEWS PORTAL ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
    <title>Keygap Advantage | Professional Financial Hub</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,700;1,700&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        html {{ scroll-behavior: smooth; }}
        body {{ background-color: #f3f4f6; color: #111827; font-family: 'Inter', sans-serif; }}
        .news-header {{ font-family: 'Playfair Display', serif; border-bottom: 4px solid #000; }}
        .ticker-wrap {{ background: #000; color: #fff; overflow: hidden; padding: 5px 0; }}
        .main-container {{ max-width: 1200px; margin: 0 auto; background: white; box-shadow: 0 0 50px rgba(0,0,0,0.05); }}
        .sidebar-box {{ border-top: 3px solid #c00; background: #fafafa; }}
        .accent {{ color: #c00; }}
        .live-dot {{ height: 10px; width: 10px; background-color: #ff0000; border-radius: 50%; display: inline-block; animation: blink 1s infinite; }}
        @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.2; }} 100% {{ opacity: 1; }} }}
    </style>
</head>
<body class="py-0 md:py-8">

    <div class="main-container">
        <div class="ticker-wrap h-10">
            <iframe src="https://s.tradingview.com/embed-widget/ticker-tape/?symbols=FX:EURUSD,TVC:GOLD,INDEX:SPX,BINANCE:BTCUSDT,BINANCE:ETHUSDT&theme=dark" width="100%" height="100%" frameborder="0"></iframe>
        </div>

        <nav class="p-4 border-b flex justify-between items-center text-[10px] font-bold uppercase tracking-widest">
            <div class="flex items-center gap-4">
                <span><span class="live-dot mr-1"></span> LIVE: <span id="clock">--:--:--</span></span>
                <span class="hidden md:inline text-gray-400">|</span>
                <span class="hidden md:inline">Status: Market Open</span>
            </div>
            <div class="flex gap-6">
                <a href="index.html" class="hover:accent">Home</a>
                <a href="#analisi" class="hover:accent">Analisi Tecnica</a>
                <a href="#market" class="hover:accent">Market Data</a>
            </div>
        </nav>

        <header class="p-8 text-center news-header">
            <h1 class="text-5xl md:text-7xl font-bold uppercase tracking-tighter">Keygap <span class="accent">Advantage</span></h1>
            <p class="text-gray-500 italic mt-3 text-lg font-serif">"L'informazione finanziaria che precede il mercato"</p>
        </header>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-0">
            
            <div class="lg:col-span-3 border-r p-6 hidden lg:block bg-gray-50">
                <h3 class="font-black border-b-2 border-black pb-2 mb-4 uppercase text-xs">Trending Now</h3>
                <div class="space-y-6">
                    <div>
                        <span class="text-[10px] font-bold text-red-600 uppercase">Forex</span>
                        <h4 class="font-bold text-sm leading-tight hover:underline cursor-pointer">Resistenza chiave EUR/USD a 1.0850</h4>
                    </div>
                    <div>
                        <span class="text-[10px] font-bold text-red-600 uppercase">Commodities</span>
                        <h4 class="font-bold text-sm leading-tight hover:underline cursor-pointer">L'Oro testa i massimi storici</h4>
                    </div>
                    <div class="pt-4 border-t">
                        <iframe src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?symbol=FX:EURUSD&theme=light" width="100%" height="150" frameborder="0"></iframe>
                    </div>
                </div>
            </div>

            <div id="analisi" class="lg:col-span-6 p-6 md:p-10">
                <div class="mb-4 text-center">
                    <span class="bg-black text-white px-3 py-1 text-[10px] font-black uppercase tracking-widest">Analisi del Giorno</span>
                </div>
                <h2 class="text-4xl md:text-5xl font-bold font-serif italic text-center leading-tight mb-8 uppercase tracking-tighter">
                    "{testo_notizia}"
                </h2>
                <div class="h-[450px] border shadow-inner mb-8 bg-black">
                    <iframe src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=light&v={id_versione}" width="100%" height="100%" frameborder="0"></iframe>
                </div>
                <p class="text-gray-600 leading-relaxed first-letter:text-5xl first-letter:font-bold first-letter:float-left first-letter:mr-3">
                    Le attuali condizioni di mercato suggeriscono una fase di riaccumulazione. I nostri modelli quantitativi indicano una probabilità dell'85% di volatilità espansa nelle prossime 48 ore. Gli investitori istituzionali stanno monitorando attentamente i livelli di liquidità sotto i minimi settimanali.
                </p>
            </div>

            <div id="market" class="lg:col-span-3 p-6 bg-gray-50 border-l">
                <div class="sidebar-box p-4 mb-6 shadow-sm">
                    <h3 class="font-bold text-xs mb-4 uppercase">Market Screener</h3>
                    <iframe src="https://s.tradingview.com/embed-widget/screener/?itemsCount=5&market=crypto&theme=light" width="100%" height="400" frameborder="0"></iframe>
                </div>
                <div class="sidebar-box p-4 shadow-sm">
                    <h3 class="font-bold text-xs mb-4 uppercase">Economic Calendar</h3>
                    <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=light&isTransparent=false&width=100%25&height=300" width="100%" height="300" frameborder="0"></iframe>
                </div>
            </div>
        </div>

        <footer class="bg-black text-white p-12 text-center">
            <h2 class="text-3xl font-serif italic mb-4">Keygap Advantage</h2>
            <div class="flex justify-center gap-8 text-[10px] uppercase tracking-widest text-gray-400 mb-8">
                <a href="#" class="hover:text-white">Privacy Policy</a>
                <a href="#" class="hover:text-white">Terms of Service</a>
                <a href="#" class="hover:text-white">Risk Disclosure</a>
            </div>
            <p class="text-[9px] text-gray-600 max-w-xl mx-auto leading-loose uppercase">
                Tutti i contenuti sono generati da algoritmi proprietari. Il trading comporta rischi. Build ID: {id_versione}
            </p>
        </footer>
    </div>

    <script>
        function updateClock() {{
            const now = new Date();
            const timeString = now.toLocaleTimeString('it-IT', {{ hour12: false }});
            document.getElementById('clock').textContent = timeString;
        }}
        setInterval(updateClock, 1000);
        updateClock();
    </script>
    <script src="https://pl28819682.effectivegatecpm.com/07/47/37/074737f2d1be0f3c0e9de0585a695fd7.js"></script>
</body>
</html>
'''

# --- ESECUZIONE ---
try:
    with open(os.path.join(BASE_DIR, "index.html"), "w", encoding="utf-8") as f:
        f.write(HTML_MASTER)
    if "GITHUB_ACTIONS" not in os.environ:
        subprocess.run(["git", "add", "."], cwd=BASE_DIR)
        subprocess.run(["git", "commit", "-m", f"UI-PREMIUM Update {ora_esatta}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR)
    else:
        print(f"🤖 AUTOMAZIONE COMPLETATA ({ora_esatta})")
except Exception as e:
    print(f"❌ ERRORE: {e}")