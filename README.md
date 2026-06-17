# Desafio B2BFlow

Projeto desenvolvido em Python para leitura de contatos armazenados no Supabase e envio automático de mensagens via WhatsApp utilizando a API da Z-API.

## Tecnologias

- Python
- Supabase
- Z-API
- python-dotenv

## Estrutura da tabela

Tabela: `contatos`

| Campo    | Tipo    |
| -------- | ------- |
| id       | integer |
| nome     | text    |
| telefone | text    |

## Variáveis de ambiente

```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```
