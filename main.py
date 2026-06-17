from supabase import create_client
from dotenv import load_dotenv
import requests
import os

load_dotenv()

supabase = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

instance_id = os.getenv("ZAPI_INSTANCE_ID")
token = os.getenv("ZAPI_TOKEN")

resposta= supabase.table("contatos").select("*").limit(3).execute()

contatos = resposta.data

for contato in contatos:
    try: 
        mensagem = f"Olá, {contato['nome']} tudo bem com você?"

        url = f"https://api.z-api.io/instances/{instance_id}/token/{token}/send-text"

        dados_mensagem = {
        "phone": contato["telefone"],
        "message": mensagem
         }

        envio = requests.post(url,json=dados_mensagem)

        if envio.status_code != 200:
            print(f"Erro ao enviar para {contato['nome']}: {envio.text}")
        else: 
            print( f"Mensagem enviada para {contato['nome']} - Status: {envio.status_code}")
    
    except Exception as e: 
        print(f"Erro inesperado para {contato['nome']}: {e}")