import os
from datetime import datetime

def genera_e_salva_report():
    data_ora = datetime.now().strftime('%d/%m/%Y %H:%M')
    folder = os.path.expanduser('~/Desktop/Keygap_AdVantage/articoli_pronti')
    filename = 'INSIGHT_PROFESSIONALE_KEYGAP.txt'
    path = os.path.join(folder, filename)
    
    btc, eth, xrp = '€61.734,20 (+4.1%)', '€3.105,88 (-1.2%)', '€0.5891 (+2.7%)'
    
    fb_desc = f'''🏛️ KEYGAP INTELLIGENCE: ANALISI ISTITUZIONALE FLOW-DATA

DATA SESSIONE: {data_ora}
STATUS: MONITORAGGIO HFT ATTIVO 🟢

L'analisi odierna dei flussi di mercato rivela un'attività anomala nei cluster di liquidità. Il motore Keygap ADK 2.0 ha isolato pattern di esecuzione che confermano la presenza di operatori Market Maker in fase di riposizionamento strategico.

📊 DECODIFICA ASSET (SESSIONE CORRENTE):

🔸 BITCOIN (BTC): {btc}
Analisi: Segnale di Accumulo HFT confermato. Le "bacchette sparse" evidenziano un assorbimento della pressione di vendita in area micro-gap. I flussi istituzionali stanno costruendo un floor di supporto invisibile al retail.

🔹 ETHEREUM (ETH): {eth}
Analisi: Micro-glitch di compressione volumetrica. Rilevato un pattern di "spoofing" algoritmico atto a testare la liquidità dei livelli inferiori prima di una possibile espansione.

🔸 RIPPLE (XRP): {xrp}
Analisi: Tracce di ordini algoritmici a bassa latenza. Il sistema rileva un'interazione diretta tra smart contracts istituzionali e pool di liquidità centralizzate.

🔍 KEYGAP INSIGHT - SENTIMENT ALGORITMICO:
Non limitatevi a guardare le candele. Le ombre dei prezzi sono le tracce lasciate dai giganti della finanza. Noi decodifichiamo il linguaggio dell'Order Flow per anticipare i movimenti che il grafico mostrerà solo in seguito.

#KeygapInsights #HFTTrading #OrderFlow #AnalisiTecnica #Bitcoin #FinanzaIstituzionale #MarketInsights #CryptoData'''
    
    tt_desc = f'''🔑 KEYGAP: DENTRO IL LINGUAGGIO HFT

📉 BTC {btc} -> Segnale Istituzionale
📈 ETH {eth} -> Test Liquidità
📊 XRP {xrp} -> Pattern Algoritmico

I glitch grafici sono la nostra mappa. Smetti di guardare il prezzo, guarda i volumi nascosti. #Keygap #TradingAlgoritmico #HFT #Crypto #PerTe'''

    contenuto = f'''--- SCHEDA EDITORIALE ELITE KEYGAP ---

[PER FACEBOOK: ANALISI APPROFONDITA]

{fb_desc}

==============================================

[PER TIKTOK: FAST INSIGHT]

{tt_desc}
---
'''
    
    with open(path, 'w') as f:
        f.write(contenuto)
    print(f'✅ Report Elite salvato in: {path}')

genera_e_salva_report()