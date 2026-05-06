# Portfolio Backend

Backend para o portfólio usando FastAPI + Resend para envio de emails.

## Como usar localmente

1. Crie uma conta no [Resend](https://resend.com/) e obtenha sua API Key
2. Copie `.env.example` para `.env` e preencha as variáveis:
   ```
   RESEND_API_KEY=seu_resend_api_key
   RECIPIENT_EMAIL=email_do_sergio@example.com
   ```
3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o servidor:
   ```bash
   python main.py
   ```
5. A API estará disponível em `http://localhost:8000`

## Deploy no Render

1. Conecte seu repositório GitHub ao Render
2. Crie um novo Web Service
3. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Adicione as variáveis de ambiente no painel do Render:
   - RESEND_API_KEY
   - RECIPIENT_EMAIL
5. Deploy!

## Atualizar o frontend

Depois do deploy no Render, atualize a URL no arquivo `index.html` do frontend, substituindo `https://your-render-backend-url.onrender.com/api/contact` pela URL real do seu backend no Render.
