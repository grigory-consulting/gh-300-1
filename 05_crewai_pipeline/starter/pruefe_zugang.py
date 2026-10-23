"""Prüft, ob der Schlüssel in .env funktioniert: eine kurze Anfrage an das Modell."""

import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv(Path(__file__).with_name(".env"), override=True)

basis = os.environ.get("LLM_BASE_URL") or "https://api.openai.com/v1"
schluessel = os.environ.get("LLM_API_KEY", "")
modell = os.environ.get("LLM_MODEL") or "gpt-4.1-mini"

if not schluessel or schluessel == "sk-...":
    raise SystemExit("In .env fehlt der Schlüssel (LLM_API_KEY). Vorlage: .env.example")

antwort = OpenAI(base_url=basis, api_key=schluessel).chat.completions.create(
    model=modell,
    messages=[{"role": "user", "content": "Antworte nur mit OK."}],
    max_tokens=5,
)
print(f"Zugang funktioniert: {modell} antwortet mit {antwort.choices[0].message.content!r}")
