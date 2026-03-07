import json, subprocess
data = {
    "price": "€88.150,00", 
    "status": "TEST PONTE", 
    "signal": "ATTESA CHIAVI GOOGLE"
}
with open("market_status.json", "w") as j:
    json.dump(data, j)

subprocess.run(["git", "add", "market_status.json"])
subprocess.run(["git", "commit", "-m", "⚡ Test Sito"])
subprocess.run(["git", "push", "origin", "main", "--force"])
print("\n✅ DATI INVIATI! Controlla il cellulare tra 10 secondi.")
