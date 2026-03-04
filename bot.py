import os, subprocess, datetime, requests

# --- CONFIGURAZIONE UNIVERSALE ---
# Usiamo il percorso relativo per far sì che funzioni ovunque (PC o GitHub)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTICOLI_PATH = os.path.join(BASE_DIR, "articoli_pronti")
# Sicurezza: il token viene letto dall'ambiente, non è più scritto nel codice
ADSTERRA_API_TOKEN = os.environ.get("ADSTERRA_TOKEN", "") 

def ottieni_contenuto():
    ora = datetime.datetime.now().hour
    # Il bot sceglie il file in base all'orario
    file_target = "mattina.txt" if 5 <= ora < 15 else "sera.txt"
    path_file = os.path.join(ARTICOLI_PATH, file_target)
    
    if os.path.exists(path_file):
        with open(path_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "ANALISI DI MERCATO: I nostri algoritmi stanno elaborando i dati in tempo reale..."

testo_notizia = ottieni_contenuto()
ora_esatta = datetime.datetime.now().strftime("%H:%M")

# --- LAYOUT STYLE ARANZULLA / FINANCIAL TIMES ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Keygap Advantage | Il Punto sulla Finanza</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@400;600;700&display=swap" rel="stylesheet">
    <style>
        body {{ background-color: #fcfcfc; color: #1a1a1a; font-family: 'Inter', sans-serif; }}
        .header-logo {{ font-family: 'Playfair Display', serif; font-size: 2.5rem; border-bottom: 3px solid #1a1a1a; }}
        .top-nav {{ border-bottom: 1px solid #eee; background: white; }}
        .main-card {{ background: white; border: 1px solid #e5e7eb; transition: all 0.3s ease; }}
        .breaking-tag {{ background: #c00; color: white; padding: 2px 8px; font-size: 0.7rem; font-weight: bold; text-transform: uppercase; }}
        .article-title {{ font-family: 'Playfair Display', serif; line-height: 1.2; }}
    </style>
</head>
<body>

    <nav class="top-nav p-3 mb-6">
        <div class="max-w-6xl mx-auto flex justify-between items-center text-xs font-bold uppercase tracking-widest text-gray-500">
            <span>Finanza & Mercati • {ora_esatta}</span>
            <div class="space-x-4">
                <a href="#" class="hover:text-red-600">Home</a>
                <a href="#" class="hover:text-red-600">Analisi</a>
                <a href="#" class="hover:text-red-600">Guide</a>
            </div>
        </div>
    </nav>

    <div class="max-w-6xl mx-auto px-4">
        
        <header class="text-center mb-10">
            <h1 class="header-logo inline-block px-4">Keygap Advantage</h1>
            <p class="text-gray-500 mt-2 italic">Il portale di riferimento per l'analisi finanziaria professionale</p>
        </header>

        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8 mb-12">
            <div class="lg:col-span-2">
                <div class="mb-4"><span class="breaking-tag">In Primo Piano</span></div>
                <h2 class="article-title text-4xl md:text-5xl font-bold mb-6">{testo_notizia}</h2>
                <div class="h-[450px] main-card rounded-lg overflow-hidden shadow-sm">
                    <iframe src="https://s.tradingview.com/widgetembed/?symbol=TVC:DXY&theme=light&interval=D" width="100%" height="100%" frameborder="0"></iframe>
                </div>
            </div>

            <div class="space-y-6">
                <div class="main-card p-4 rounded-lg">
                    <h3 class="font-bold border-b pb-2 mb-4 uppercase text-xs">Prezzi Live</h3>
                    <iframe src="https://s.tradingview.com/embed-widget/tickers/?symbols=FX:EURUSD,TVC:GOLD,INDEX:SPX,BINANCE:BTCUSDT&theme=light" width="100%" height="220" frameborder="0"></iframe>
                </div>
                
                <div class="main-card p-4 rounded-lg bg-gray-50">
                    <h3 class="font-bold border-b pb-2 mb-4 uppercase text-xs text-red-700">Calendario Economico</h3>
                    <iframe src="https://s.tradingview.com/embed-widget/events/?colorTheme=light&width=100%25&height=300" width="100%" height="300" frameborder="0"></iframe>
                </div>
            </div>
        </div>

        <div class="border-t pt-8 mb-12">
            <h3 class="text-2xl font-bold mb-6">Archivio Analisi</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div class="main-card p-4 hover:shadow-md transition cursor-pointer">
                    <h4 class="font-bold text-lg mb-2 text-red-700">Strategia S&P500</h4>
                    <p class="text-sm text-gray-600">Livelli chiave per la settimana. Supporti e resistenze basate su volumi.</p>
                </div>
                <div class="main-card p-4 hover:shadow-md transition cursor-pointer">
                    <h4 class="font-bold text-lg mb-2 text-red-700">Focus Criptovalute</h4>
                    <p class="text-sm text-gray-600">Bitcoin mantiene il floor psicologico. Analisi del sentiment retail.</p>
                </div>
                <div class="main-card p-4 hover:shadow-md transition cursor-pointer">
                    <h4 class="font-bold text-lg mb-2 text-red-700">Commodities: Oro</h4>
                    <p class="text-sm text-gray-600">Il bene rifugio brilla. Proiezioni per il Q2 2026 basate sui tassi.</p>
                </div>
            </div>
        </div>
    </div>

    <footer class="bg-gray-900 text-white py-12 mt-12 text-center">
        <div class="max-w-6xl mx-auto px-4">
            <p class="text-2xl font-serif mb-4">Keygap Advantage</p>
            <p class="text-gray-500 text-xs uppercase tracking-widest">© 2026 - Analisi Indipendente • Proprietà di Giampiero De Luca</p>
        </div>
    </footer>

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
        subprocess.run(["git", "commit", "-m", f"Update {ora_esatta}"], cwd=BASE_DIR)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR)
    else:
        print(f"🤖 ESECUZIONE AUTOMATICA GITHUB ACTIONS COMPLETATA ({ora_esatta})")

except Exception as e:
    print(f"❌ ERRORE CRITICO: {e}")