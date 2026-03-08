import os
import blogger_bot
from datetime import datetime

# Testo professionale CeFi/DeFi
t, c, n = blogger_bot.crea_report()
c = f"<h2>Analisi Strategica CeFi/DeFi</h2><p>Report Keygap Advantage generato per l'integrazione dei mercati centralizzati e decentralizzati.</p>{c}"

try:
    # Pubblica su Blogger
    s = blogger_bot.get_blogger_service()
    s.posts().insert(blogId=blogger_bot.BLOG_ID, body={'title': t, 'content': c}).execute()
    
    # Salva nella cartella
    path = os.path.join(blogger_bot.LOCAL_REPORT_DIR, f"report_{n}.html")
    with open(path, "w") as f:
        f.write(f"<html><body>{c}</body></html>")
    
    print("✅ CARTELLA E BLOGGER AGGIORNATI!")
except Exception as e:
    print(f"❌ ERRORE: {e}")
