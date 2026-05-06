from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
import resend
import os
from html import escape
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

class ContactForm(BaseModel):
    name: str
    email: EmailStr
    project_type: str
    message: str


def get_email_settings() -> tuple[str, str, str]:
    api_key = os.getenv("RESEND_API_KEY")
    from_email = os.getenv("RESEND_FROM_EMAIL", "onboarding@resend.dev")
    recipient_email = os.getenv("RECIPIENT_EMAIL", "sperey@gcgiglobal.com")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="RESEND_API_KEY is not configured on the server.",
        )

    resend.api_key = api_key
    return api_key, from_email, recipient_email

@app.post("/api/contact")
async def send_contact_email(form: ContactForm):
    try:
        _, from_email, recipient_email = get_email_settings()
        sender_email = str(form.email)
        subject = f"Novo contato do portfólio: {form.name}"
        html_content = f"""
        <h2>Nova mensagem do portfólio</h2>
        <p><strong>Nome:</strong> {escape(form.name)}</p>
        <p><strong>Email:</strong> {escape(sender_email)}</p>
        <p><strong>Tipo de Projeto:</strong> {escape(form.project_type)}</p>
        <p><strong>Mensagem:</strong></p>
        <p>{escape(form.message)}</p>
        """
        internal_email = resend.Emails.send({
            "from": from_email,
            "to": [recipient_email],
            "subject": subject,
            "html": html_content,
            "reply_to": sender_email,
        })

        return {
            "success": True,
            "message": "Emails enviados com sucesso!",
            "id": internal_email["id"],
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao enviar email: {str(e)}")

@app.get("/")
async def root():
    return {"message": "API do portfólio está funcionando!"}

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
