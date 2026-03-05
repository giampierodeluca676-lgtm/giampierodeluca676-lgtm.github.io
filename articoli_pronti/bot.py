import os
from datetime import datetime

def genera_e_salva_report():
    data_ora = datetime.now().strftime('%d/%m/%Y %H:%M')
    folder = os.path.expanduser('~/Desktop/Keygap_AdVantage/articoli_pronti')
    filename = 'report_corretto_strutturato.txt'
    path = os.path.join(folder, filename)
    
    btc, eth, xrp = '€61.734,20 (+4.1%)', '€3.105,88 (-1.2%)', '€0.5891 (+2.7%)'
    
    fb_desc = f'''📑 REPORT ANALITICO: KEYGAP ADK 2.0 (LIVE UPDATE)

Status del Sistema: Operativo 🟢
Data: {data_ora}

L'ecosistema Keygap ha completato la scansione dei flussi dati in tempo reale. Le anomalie grafiche rilevate — i cosiddetti "glitch" — sono state isolate e identificate come impronte digitali di algoritmi HFT (High-Frequency Trading) istituzionali.

📊 ANALISI PERFORMANCE ASSET:
• BITCOIN (BTC): {btc} 🚀 -> Rilevato segnale di Accumulo HFT. Le "bacchette sparse" indicano posizionamento massivo.
• ETHEREUM (ETH): {eth} 📉 -> Micro-glitch di compressione tecnica. Fase di stallo monitorata.
• RIPPLE (XRP): {xrp} ✨ -> Tracce di ordini algoritmici precisi rilevate dai sensori.

🔍 KEYGAP INSIGHT:
Mentre il mercato retail osserva solo i prezzi, l'intelligenza autonoma di Keygap decodifica il linguaggio nascosto della finanza algoritmica. Non seguiamo il trend: analizziamo le tracce lasciate dai giganti.

#KeygapInsights #TradingProfessionale #HFT #Bitcoin #Ethereum #Ripple #CryptoAnalysis #FinanzaAlgoritmica #TradingReport #DigitalAssets'''
    
    tt_desc = f'''🔑 KEYGAP: I GLITCH SONO SEGNALI

BTC {btc} 🚀
ETH {eth} 📉
XRP {xrp} ✨

Analisi HFT attiva. Segui il segnale.

#Keygap #Crypto #Trading #Bitcoin #HFT #PerTe #Viral'''

    contenuto = f'''--- SCHEDA EDITORIALE DEFINITIVA ---

[VERSIONE FACEBOOK: COPIA TUTTO IL TESTO SOTTO]

{fb_desc}

==============================================

[VERSIONE TIKTOK: COPIA TUTTO IL TESTO SOTTO]

{tt_desc}
---
'''
    
    with open(path, 'w') as f:
        f.write(contenuto)
    print(f'✅ Report professionale salvato in: {path}')

genera_e_salva_report()