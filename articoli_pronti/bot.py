import os
from datetime import datetime

def genera_e_salva_report():
    data_ora = datetime.now().strftime('%d/%m/%Y %H:%M')
    folder = os.path.expanduser('~/Desktop/Keygap_AdVantage/articoli_pronti')
    os.makedirs(folder, exist_ok=True)
    
    btc, eth, xrp = '€61.734,20 (+4.1%)', '€3.105,88 (-1.2%)', '€0.5891 (+2.7%)'
    
    fb = (
        f"📑 REPORT ANALITICO: KEYGAP ADK 2.0 (LIVE UPDATE)\n\n"
        f"Status: Operativo 🟢\nData: {data_ora}\n\n"
        f"L'ecosistema Keygap ha isolato impronte digitali di algoritmi HFT istituzionali.\n\n"
        f"📊 ANALISI PERFORMANCE ASSET:\n"
        f"• BTC: {btc} 🚀\nDiagnosi: Accumulo HFT. Posizionamento massivo dei grandi player.\n"
        f"• ETH: {eth} 📉\nDiagnosi: Micro-glitch di compressione. Fase di stallo tecnico.\n"
        f"• XRP: {xrp} ✨\nDiagnosi: Institutional Movement. Ordini a bassa latenza rilevati.\n\n"
        f"🔍 KEYGAP INSIGHT:\nDecodifichiamo il linguaggio nascosto della finanza algoritmica.\n"
        f"🔗 https://giampierodeluca676-lgtm.github.io/\n\n"
        f"#KeygapInsights #HFT #Bitcoin #Ethereum #Ripple #CryptoAnalysis"
    )
    
    tt = (
        f"🔑 KEYGAP: DECODIFICA HFT ATTIVA\n\n"
        f"BTC {btc} 🚀\nETH {eth} 📉\nXRP {xrp} ✨\n\n"
        f"I glitch sono le tracce dei Giganti.\n"
        f"#Keygap #Crypto #HFT #PerTe"
    )
    
    html = (
        f"<div style='font-family:Arial;border:1px solid #ddd;padding:20px;border-radius:10px;max-width:600px;'>\n"
        f"<h2 style='color:#1a73e8;'>🏛️ KEYGAP INTELLIGENCE</h2>\n"
        f"<p><b>Sessione:</b> {data_ora}</p>\n"
        f"<hr><p><b>BTC:</b> {btc} (Accumulo HFT)</p>\n"
        f"<p><b>ETH:</b> {eth} (Compressione)</p>\n"
        f"<p><b>XRP:</b> {xrp} (Low Latency Flow)</p>\n"
        f"</div>"
    )

    with open(os.path.join(folder, 'REPORT_SOCIAL.txt'), 'w') as f:
        f.write(f"--- FACEBOOK ---\n{fb}\n\n--- TIKTOK ---\n{tt}")
    
    with open(os.path.join(folder, 'PAGINA_BLOGGER.html'), 'w') as f:
        f.write(html)

    print(f"✅ File generati con successo in: {folder}")

genera_e_salva_report()
