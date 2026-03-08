import os
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from datetime import datetime

BLOG_ID = '2744764892823107807'
SCOPES = ['https://www.googleapis.com/auth/blogger']

def get_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    return build('blogger', 'v3', credentials=creds)

try:
    print("🚀 Forzatura invio in corso...")
    service = get_service()
    now = datetime.now()
    titolo = f"Test Forzato Keygap - {now.strftime('%d/%m/%Y %H:%M')}"
    contenuto = "Test di pubblicazione immediata per verifica sistema."
    body = {"kind": "blogger#post", "title": titolo, "content": contenuto}
    service.posts().insert(blogId=BLOG_ID, body=body).execute()
    print("✅✅✅ POST INVIATO! CONTROLLA BLOGGER ORA!")
except Exception as e:
    print(f"❌ ERRORE: {e}")
