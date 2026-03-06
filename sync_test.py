import json, subprocess
data = {
    "price": "€ 87.420,10",
    "status": "OPERATIVO",
    "signal": "BULLISH",
    "last_post_title": "⚠️ ANALISI QUANTISTICA: BTC Rompe i Massimi",
    "last_post_url": "https://giampierodeluca676.blogspot.com/",
    "ticker": "BTC/EUR: € 87.420 • ETH/EUR: € 3.450 • KEYGAP SIGNAL: BULLISH • "
}
with open("market_status.json", "w") as j:
    json.dump(data, j)

subprocess.run(["git", "add", "market_status.json"])
subprocess.run(["git", "commit", "-m", "⚡ Sync Test News"])
subprocess.run(["git", "push", "origin", "main", "--force"])
print("\n✅ TEST NEWS INVIATO! Controlla il sito tra 5 secondi.")
