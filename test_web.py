import json, os, subprocess
data = {"price": "€87.420,10", "status": "TEST_PONTE", "signal": "ATTESA_CHIAVI"}
with open("market_status.json", "w") as j: json.dump(data, j)
subprocess.run(["git", "add", "market_status.json"])
subprocess.run(["git", "commit", "-m", "⚡ Test Ponte"])
subprocess.run(["git", "push", "origin", "main", "--force"])
print("🚀 Test inviato! Controlla il cellulare.")
