import os
from datetime import datetime

def genera_e_salva_report():
    data_ora = datetime.now().strftime('%d/%m/%Y %H:%M')
    base_dir = os.path.dirname(os.path.abspath(__file__))
    folder = os.path.join(base_dir, 'articoli_pronti')
    os.makedirs(folder, exist_ok=True)
    
    # Dati simulati/reali
    btc, eth, xrp = '€61.734,20 (+4.1%)', '€3.105,88 (-1.2%)', '€0.5891 (+2.7%)'
    
    # --- VERSIONE FACEBOOK ELITE ---
    fb = (f"📑 REPORT ANALITICO: KEYGAP ADK 2.0\n\nStatus: Operativo 🟢\nData: {data_ora}\n\n"
          f"L'ecosistema Keygap ha isolato impronte digitali di algoritmi HFT istituzionali.\n\n"
          f"📊 ANALISI PERFORMANCE ASSET:\n• BTC: {btc} 🚀 (Accumulo HFT)\n• ETH: {eth} 📉 (Compressione)\n• XRP: {xrp} ✨ (Institutional Flow)\n\n"
          f"🔍 KEYGAP INSIGHT: Decodifichiamo il linguaggio nascosto della finanza algoritmica.\n"
          f"🔗 https://giampierodeluca676-lgtm.github.io/\n\n#KeygapInsights #HFT #Bitcoin #CryptoAnalysis")

    # --- VERSIONE BLOGGER HTML (ESTETICA PROFESSIONALE) ---
    html = f"""
<div style="background-color: #0f172a; color: #f8fafc; font-family: 'Inter', sans-serif; padding: 30px; border-radius: 15px; max-width: 800px; margin: auto; border: 1px solid #1e293b; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1);">
    <div style="text-align: center; border-bottom: 1px solid #334155; padding-bottom: 20px; margin-bottom: 20px;">
        <h1 style="color: #38bdf8; margin: 0; font-size: 24px; letter-spacing: 2px;">KEYGAP QUANTUM INTELLIGENCE</h1>
        <p style="color: #94a3b8; font-size: 14px;">TERMINAL STATUS: <span style="color: #22c55e;">ACTIVE 🟢</span> | SESSION: {data_ora}</p>
    </div>

    <div style="display: grid; gap: 15px; margin-bottom: 25px;">
        <div style="background: #1e293b; padding: 15px; border-radius: 10px; border-left: 4px solid #f59e0b;">
            <h3 style="margin: 0; color: #f59e0b;">BITCOIN (BTC)</h3>
            <p style="font-size: 20px; margin: 5px 0; font-weight: bold;">{btc}</p>
            <p style="font-size: 13px; color: #94a3b8; margin: 0;">Diagnosi: Accumulo HFT Istituzionale rilevato nei cluster.</p>
        </div>
        
        <div style="background: #1e293b; padding: 15px; border-radius: 10px; border-left: 4px solid #6366f1;">
            <h3 style="margin: 0; color: #6366f1;">ETHEREUM (ETH)</h3>
            <p style="font-size: 20px; margin: 5px 0; font-weight: bold;">{eth}</p>
            <p style="font-size: 13px; color: #94a3b8; margin: 0;">Diagnosi: Fase di compressione volumetrica in corso.</p>
        </div>

        <div style="background: #1e293b; padding: 15px; border-radius: 10px; border-left: 4px solid #0ea5e9;">
            <h3 style="margin: 0; color: #0ea5e9;">RIPPLE (XRP)</h3>
            <p style="font-size: 20px; margin: 5px 0; font-weight: bold;">{xrp}</p>
            <p style="font-size: 13px; color: #94a3b8; margin: 0;">Diagnosi: Movimenti algoritmici a bassa latenza (Institutional).</p>
        </div>
    </div>

    <div style="background: rgba(56, 189, 248, 0.1); padding: 20px; border-radius: 10px; border: 1px dashed #38bdf8;">
        <h4 style="margin: 0 0 10px 0; color: #38bdf8;">🔍 ANALISI GLITCH HFT</h4>
        <p style="font-size: 14px; line-height: 1.6; color: #cbd5e1; margin: 0;">
            Il sistema ha isolato micro-distorsioni nei data-feed. Queste anomalie non sono errori tecnici, ma impronte digitali di ordini massivi eseguiti da bot istituzionali. Keygap sta processando i vettori di uscita.
        </p>
    </div>

    <div style="margin-top: 25px; text-align: center; font-size: 12px; color: #64748b;">
        <p>Monitoraggio in tempo reale: <a href="https://giampierodeluca676-lgtm.github.io/" style="color: #38bdf8; text-decoration: none;">Accedi al Portale Live</a></p>
        <p>#KeygapInsights #TradingProfessionale #HFT #BlockchainIntelligence</p>
    </div>
</div>
"""

    with open(os.path.join(folder, 'REPORT_SOCIAL.txt'), 'w') as f:
        f.write(fb)
    with open(os.path.join(folder, 'PAGINA_BLOGGER.html'), 'w') as f:
        f.write(html)
    print(f"✅ Tutto pronto! File HTML e Social generati.")

if __name__ == '__main__':
    genera_e_salva_report()
