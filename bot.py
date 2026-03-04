import os, subprocess, datetime

# --- CONFIGURAZIONE ---
REPO_PATH = os.path.expanduser("~") + "/Desktop/Keygap_AdVantage"
ARTICOLI_PATH = os.path.join(REPO_PATH, "articoli_pronti")

def ottieni_contenuto():
    ora = datetime.datetime.now().hour
    # Sceglie il file in base all'orario
    file_target = "mattina.txt" if 5 <= ora < 15 else "sera.txt"
    path_file = os.path.join(ARTICOLI_PATH, file_target)
    
    if os.path.exists(path_file):
        with open(path_file, "r", encoding="utf-8") as f:
            return f.read().strip()
    return "ATTENDERE: Aggiornamento segnali in corso..."

testo_notizia = ottieni_contenuto()
ora_esatta = datetime.datetime.now().strftime("%H:%M")

# --- NUOVO LAYOUT AD ALTO IMPATTO ---
HTML_MASTER = f'''
<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <title>KEYGAP ADVANTAGE</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{ background: #000; color: #fff; font-family: 'Inter', sans-serif; margin: 0; }}
        .news-banner {{ 
            background: #ff0000; 
            color: #fff; 
            padding: 25px; 
            text-align: center; 
            font-size: 35px; 
            font-weight: 900;
            border-bottom: 4px solid #fff;
            text-transform: uppercase;
            animation: blink 1.5s infinite;
        }}
        @keyframes blink {{ 0% {{ opacity: 1; }} 50% {{ opacity: 0.7; }} 100% {{ opacity: 1; }} }}
    </style>
</head>
<body>
    <div class="news-banner">
        ⚠️ NEWS FLASH {ora_esatta}: {testo_notizia}
    </div>
    <div style="padding: 10px; height: 80vh;">
        <iframe src="https://s.tradingview.com/widgetembed/?symbol=SPX&theme=dark" width="100%" height="100%" frameborder="0"></iframe>
    </div>
</body>
</html>
'''

try:
    os.chdir(REPO_PATH)
    # Scrive il file index.html locale
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(HTML_MASTER)
    
    # COMANDI GIT CORRETTI PER IL TUO RAMO 'MAIN'
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", f"Update News {ora_esatta}"])
    
    # CAMBIATO DA master A main PER RISOLVERE L'ERRORE
    result = subprocess.run(["git", "push", "origin", "main"], capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ SUCCESSO: La notizia è stata spedita correttamente su 'main'!")
    else:
        print(f"❌ ERRORE GIT: {result.stderr}")

except Exception as e:
    print(f"❌ ERRORE GENERALE: {e}")