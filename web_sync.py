import os
import time
import json
import random

def sync():
    # Qui il bot legge il prezzo (simulato o dal tuo log.txt)
    # Per ora mettiamo un valore di test che puoi collegare al tuo bot.py
    price = random.uniform(67000, 68500) 
    data = {
        "status": "OPERATIVO",
        "price": f"$ {price:,.2f}",
        "signal": "MONITORING"
    }
    
    with open('market_status.json', 'w') as f:
        json.dump(data, f)
    
    os.system("git add market_status.json && git commit -m 'Auto-Sync' && git push --force")
    print("Dati inviati al sito con successo.")

while True:
    sync()
    time.sleep(60) # Aggiorna ogni minuto
