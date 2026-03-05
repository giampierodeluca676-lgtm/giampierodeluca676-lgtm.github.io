import os
from datetime import datetime

def genera_e_salva_report():
    data_ora = datetime.now().strftime('%d/%m/%Y %H:%M')
    folder = os.path.expanduser('~/Desktop/Keygap_AdVantage/articoli_pronti')
    
    btc, eth, xrp = '€61.734,20 (+4.1%)', '€3.105,88 (-1.2%)', '€0.5891 (+2.7%)'
    
    # 1. VERSIONE HTML PER BLOGGER
    html_content = f'''<div style="font-family: Arial; color: #333; max-width: 800px; margin: auto; border: 1px solid #ddd; padding: 20px; border-radius: 8px;">
    <h2 style="color: #1a73e8; text-align: center;">🏛️ KEYGAP INTELLIGENCE: ANALISI ISTITUZIONALE</h2>
    <p style="text-align: center; font-weight: bold;">Sessione: {data_ora} | HFT ATTIVO 🟢</p>
    <div style="background: #f8f9fa; padding: 15px; margin: 10px 0;"><h3>BTC: {btc}</h3><p>Segnale Accumulo HFT: Assorbimento pressione vendita.</p></div>
    <div style="background: #f8f9fa; padding: 15px; margin: 10px 0;"><h3>ETH: {eth}</h3><p>Spoofing Algoritmico: Test liquidita livelli inferiori.</p></div>
    <div style="background: #f8f9fa; padding: 15px; margin: 10px 0;"><h3>XRP: {xrp}</h3><p>Low Latency Flow: Interazione smart contracts istituzionali.</p></div>
</div>'''
    
    # 2. VERSIONE SOCIAL (FB/TT)
    social_content = f'''📑 REPORT ELITE KEYGAP

[FACEBOOK PROFESSONALE]
Analisi Micro-struttura: BTC ({btc}) mostra assorbimento volumi istituzionali. ETH ({eth}) in fase di compressione tecnica.

[TIKTOK RIDOTTO]
Glitch = Segnali. Segui i giganti. #Keygap #HFT'''

    with open(os.path.join(folder, 'POST_SOCIAL.txt'), 'w') as f: f.write(social_content)
    with open(os.path.join(folder, 'PAGINA_BLOGGER.html'), 'w') as f: f.write(html_content)
    
    print(f'✅ Creati POST_SOCIAL.txt e PAGINA_BLOGGER.html in {folder}')

genera_e_salva_report()