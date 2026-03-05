import os
from datetime import datetime

def genera_e_salva_report():
    data_ora = datetime.now().strftime('%d/%m/%Y %H:%M')
    folder = os.path.expanduser('~/Desktop/Keygap_AdVantage/articoli_pronti')
    filename = datetime.now().strftime('report_%Y-%m-%d_%H-%M.txt')
    path = os.path.join(folder, filename)
    
    # Prezzi Simulati/Reali per il report
    btc, eth, xrp = '€61.734,20 (+4.1%)', '€3.105,88 (-1.2%)', '€0.5891 (+2.7%)'
    
    contenuto = f'''--- REPORT ANALITICO KEYGAP ADK 2.0 ---
Data: {data_ora}

[VERSIONE FACEBOOK]
Status: Operativo 🟢
BTC: {btc} -> Accumulo HFT
ETH: {eth} -> Compressione
XRP: {xrp} -> Segnale Istituzionale

[VERSIONE TIKTOK]
BTC {btc} 🚀
ETH {eth} 📉
XRP {xrp} ✨
Glitch rilevati: SI. Segui il segnale. #Keygap
---
'''
    
    with open(path, 'w') as f:
        f.write(contenuto)
    print(f'✅ Report salvato in: {path}')

genera_e_salva_report()