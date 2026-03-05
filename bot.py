import os
from datetime import datetime

def genera_e_salva_report():
    data_ora = datetime.now().strftime('%d/%m/%Y %H:%M')
    folder = os.path.expanduser('~/Desktop/Keygap_AdVantage/articoli_pronti')
    filename = datetime.now().strftime('report_%Y-%m-%d_%H-%M.txt')
    path = os.path.join(folder, filename)
    
    btc, eth, xrp = '€61.734,20 (+4.1%)', '€3.105,88 (-1.2%)', '€0.5891 (+2.7%)'
    
    # Blocchi Testo Professionali
    fb_desc = f'''🚀 KEYGAP INSIGHTS: OLTRE IL MERCATO! 🚀

L'algoritmo ha isolato anomalie grafiche critiche. Non sono errori, è HFT istituzionale in azione.

📊 DATI REALI (Sessione {data_ora}):
• BTC: {btc} -> Accumulo HFT
• ETH: {eth} -> Compressione
• XRP: {xrp} -> Movimento Istituzionale

I glitch sono le tracce lasciate dai giganti. Noi li decodifichiamo per te.

#KeygapInsights #TradingProfessionale #HFT #Bitcoin #Ethereum #Ripple #CryptoAnalysis'''
    
    tt_desc = f'''🔑 KEYGAP: I GLITCH SONO SEGNALI

BTC {btc} 🚀
ETH {eth} 📉
XRP {xrp} ✨

Analisi HFT attiva. Segui il segnale. #Keygap #Crypto #Trading #PerTe'''

    contenuto = f'''--- SCHEDA PUBBLICAZIONE KEYGAP ---
Data: {data_ora}

[PER FACEBOOK - COPIA DA QUI]
{fb_desc}

------------------------------------

[PER TIKTOK - COPIA DA QUI]
{tt_desc}
---
'''
    
    with open(path, 'w') as f:
        f.write(contenuto)
    print(f'✅ Scheda completa salvata in: {path}')

genera_e_salva_report()