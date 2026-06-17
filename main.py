from supabase import create_client
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase = create_client(url, key)

resposta= supabase.table("contatos").select("*").limit(3).execute()

contatos = resposta.data

for contato in contatos:
    mensagem = f"Olá, {contato['nome']} tudo bem com você?"

    print("Telefone:", contato["telefone"])
    print("Mensagem", mensagem)
    print("-" * 30)