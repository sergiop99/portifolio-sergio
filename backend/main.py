from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import resend
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

resend.api_key = os.getenv("RESEND_API_KEY")

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    project_type: str
    message: str

@app.post("/api/contact")
async def send_contact_email(form: ContactForm):
    try:
        subject = f"Novo contato do portfólio: {form.name}"
        html_content = f"""
        <h2>Nova mensagem do portfólio</h2>
        <p><strong>Nome:</strong> {form.name}</p>
        <p><strong>Email:</strong> {form.email}</p>
        <p><strong>Tipo de Projeto:</strong> {form.project_type}</p>
        <p><strong>Mensagem:</strong></p>
        <p>{form.message}</p>
        """

        params = {
            "from": "onboarding@resend.dev",
            "to": [os.getenv("RECIPIENT_EMAIL")],
            "subject": subject,
            "html": html_content,
        }

        email = resend.Emails.send(params)
        return {"success": True, "message": "Email enviado com sucesso!", "id": email["id"]}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar email: {str(e)}")

@app.get("/")
async def root():
    return {"message": "API do portfólio está funcionando!"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
