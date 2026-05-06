# Sergio Pereyra — Portfolio

Personal portfolio for Sergio Pereyra, a full-stack developer focused on early-stage startups. Dark-themed, fast, and fully static frontend with a Python backend for the contact form.

## Structure

```
├── index.html          # Main portfolio page
├── styles.css          # All styles
└── backend/            # Contact form API
    ├── main.py         # FastAPI app
    ├── requirements.txt
    ├── render.yaml     # Render deploy config
    └── README.md       # Backend-specific docs
```

## Frontend

Built with plain HTML, CSS, and vanilla JavaScript — no build step required.

**Sections:**
- Hero with CTA
- What I Build (service cards)
- Case Studies (problem → solution → result)
- Tech Stack
- Experience
- Contact form

**Run locally:** open `index.html` directly in the browser.

**Deploy:** any static host works — Vercel, Netlify, GitHub Pages.

## Backend

FastAPI server that handles the contact form and sends emails via Resend.

**Stack:** Python · FastAPI · Resend · Uvicorn

**Run locally:**
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

API available at `http://localhost:8000`.

**Environment variables required:**
| Variable | Description |
|---|---|
| `RESEND_API_KEY` | API key from resend.com |
| `RESEND_FROM_EMAIL` | Sender address (default: `onboarding@resend.dev`) |
| `RECIPIENT_EMAIL` | Where contact emails are delivered |

**Deploy:** hosted on [Render](https://render.com) via `backend/render.yaml`. Add the env vars in the Render dashboard after connecting the repository.

## Links

- Live site: [sergiopereyra-dev.vercel.app](https://sergiopereyra-dev.vercel.app)
- Book a call: [calendly.com/sergiopereyra](https://calendly.com/sergiopereyra)
