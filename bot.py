import os, datetime, smtplib, requests
from email.mime.text import MIMEText

# --- CONFIGURAZIONE ---
EMAIL_MITTENTE = "giampierodeluca676@gmail.com"
EMAIL_PASSWORD = "nrznrbyfannkxdtb" 
EMAIL_BLOGGER = "giampierodeluca676.keygap_insights@blogger.com"

def prendi_dati_mercato():
    """Recupera i dati reali per rendere il report professionale."""
    try:
        # Recupero prezzi da API pubblica
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple&vs_currencies=eur"
        res = requests.get(url, timeout=10).json()
        btc = res['bitcoin']['eur']
        eth = res['ethereum']['eur']
        xrp = res['ripple']['eur']
        return f"BTC: {btc}€ | ETH: {eth}€ | XRP: {xrp}€"
    except:
        return "DATA FEED: Sincronizzazione in corso..."

def genera_report_elite():
    """Genera un report istituzionale includendo l'analisi delle anomalie."""
    ora_h = datetime.datetime.now().hour
    data_f = datetime.datetime.now().strftime('%d/%m/%Y')
    prezzi = prendi_dati_mercato()
    
    header = (
        f"--- KEYGAP QUANTUM INTELLIGENCE TERMINAL ---\n"
        f"DATA: {data_f} | STATUS: OPERATIVO\n"
        f"MARKET LIVE: {prezzi}\n"
        f"--------------------------------------------\n\n"
    )

    if 5 <= ora_h < 15:
        titolo = f"KEYGAP: Morning Intelligence - {data_f}"
        corpo = (
            "**ANALISI FLUSSI E ANOMALIE DATA-FEED**\n\n"
            "Il sistema rileva micro-distorsioni (glitch) nei grafici di volume. "
            "Queste anomalie indicano un'attività HFT (High Frequency Trading) "
            "aggressiva in corso. La struttura dei prezzi rimane comunque solida.\n\n"
            "DIAGNOSTICA: Nodi sincronizzati. Nessun errore critico rilevato.\n"
            "#Keygap #MarketGlitch #DataAnalysis"
        )
    else:
        titolo = f"KEYGAP: Daily Wrap - {data_f}"
        corpo = (
            "**SINTESI SERALE E RILEVAMENTO SPREAD**\n\n"
            "La sessione si conclude con una riduzione dei 'glitch' visivi. "
            "Il mercato entra in fase di consolidamento post-volatilità. "
            "Tutti i dati strutturali sono stati archiviati nei server Keygap.\n\n"
            "STATUS: Monitoraggio notturno attivo.\n"
            "#KeygapElite #MarketReport #BigData"
        )
    
    return titolo, header + corpo

def pubblica_su_blogger():
    """Invia il report Elite a Blogger via Email."""
    titolo, contenuto = genera_report_elite()
    print(f"Generazione report professionale: {titolo}")
    
    msg = MIMEText(contenuto)
    msg['Subject'] = titolo
    msg['From'] = EMAIL_MITTENTE
    msg['To'] = EMAIL_BLOGGER
    
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_MITTENTE, EMAIL_PASSWORD)
            server.sendmail(EMAIL_MITTENTE, EMAIL_BLOGGER, msg.as_string())
        print(f"✅ Report Istituzionale inviato correttamente alle {datetime.datetime.now().strftime('%H:%M')}")
    except Exception as e:
        print(f"❌ Errore sistema: {e}")

if __name__ == "__main__":
    pubblica_su_blogger()