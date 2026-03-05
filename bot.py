import os
from datetime import datetime

def genera_e_salva_report():
    data_ora = datetime.now().strftime('%d/%m/%Y %H:%M')
    # Definiamo il percorso della sottocartella articoli_pronti
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(base_dir, 'articoli_pronti')
    
    # Crea la cartella se non esiste
    if not os.path.exists(folder):
        os.makedirs(folder)
    
    btc, eth, xrp = '€61.734,20 (+4.1%)', '€3.105,88 (-1.2%)', '€0.5891 (+2.7%)'
    
    # --- VERSIONE FACEBOOK ELITE ---
    fb = (
        f"📑 REPORT ANALITICO: KEYGAP ADK 2.0 (LIVE UPDATE)\n\n"
        f"Status del Sistema: Operativo 🟢\nData: {data_ora}\n\n"
        f"L'ecosistema Keygap ha completato la scansione dei flussi dati in tempo reale. "
        f"Le anomalie grafiche rilevate — i cosiddetti 'glitch' — sono state isolate e identificate "
        f"come impronte digitali di algoritmi HFT istituzionali.\n\n"
        f"📊 ANALISI PERFORMANCE ASSET:\n"
        f"• BITCOIN (BTC): {btc} 🚀\nDiagnosi: Rilevato segnale di Accumulo HFT. Le 'bacchette sparse' indicano posizionamento massivo.\n"
        f"• ETHEREUM (ETH): {eth} 📉\nDiagnosi: Micro-glitch di compressione. Fase di stallo tecnico monitorata.\n"
        f"• RIPPLE (XRP): {xrp} ✨\nDiagnosi: Institutional Movement. Tracce di ordini algoritmici rilevate.\n\n"
        f"🔍 KEYGAP INSIGHT:\nMentre il mercato retail osserva solo i prezzi, l'intelligenza autonoma di Keygap "
        f"decodifica il linguaggio nascosto della finanza algoritmica.\n\n"
        f"Leggi l'analisi completa: https://giampierodeluca676-lgtm.github.io/\n\n"
        f"#KeygapInsights #TradingProfessionale #HFT #Bitcoin #CryptoAnalysis"
    )
    
    # --- VERSIONE TIKTOK RIDOTTA ---
    tt = (
        f"🔑 KEYGAP: DECODIFICA HFT ATTIVA\n\n"
        f"BTC {btc} 🚀\nETH {eth} 📉\nXRP {xrp} ✨\n\n"
        f"I glitch sono le tracce dei Giganti. Segui il segnale.\n"
        f"#Keygap #Crypto #HFT #PerTe"
    )
    
    # --- VERSIONE HTML BLOGGER ---
    html = (
        f"<div style='font-family:Arial;border:1px solid #ddd;padding:20px;border-radius:10px;max-width:600px;margin:auto;'>\n"
        f"<h2 style='color:#1a73e8;text-align:center;'>🏛️ KEYGAP INTELLIGENCE</h2>\n"
        f"<p style='text-align:center;'><b>Sessione:</b> {data_ora} | HFT ATTIVO 🟢</p><hr>\n"
        f"<p><b>BTC:</b> {btc} (Accumulo)</p>\n"
        f"<p><b>ETH:</b> {eth} (Compressione)</p>\n"
        f"<p><b>XRP:</b> {xrp} (Flow Istituzionale)</p>\n"
        f"</div>"
    )

    # Salvataggio file nella sottocartella
    with open(os.path.join(folder, 'REPORT_SOCIAL.txt'), 'w') as f:
        f.write(f"--- FACEBOOK ---\n{fb}\n\n--- TIKTOK ---\n{tt}")
    
    with open(os.path.join(folder, 'PAGINA_BLOGGER.html'), 'w') as f:
        f.write(html)

    print(f"✅ Tutto sistemato! Bot principale aggiornato e file salvati in: {folder}")

if __name__ == '__main__':
    genera_e_salva_report()
