# Simple SaaS Assistant

A minimal “help” assistant for a SaaS app. Uses FastAPI, Pinecone for retrieval, and a local LLaMA (Ollama) for short answers.

## What it does
- `/ingest` — store small text snippets in Pinecone.
- `/chat` — retrieve nearby snippets, build a short prompt, call local LLaMA, return a concise reply plus the snippets used.
- Frontend — lightweight HTML/JS chat that calls the backend and shows context.

## Setup
1) Prereqs: Python 3.10+, pip, Ollama installed. Pull the model:
   - `ollama pull llama3`
2) Pinecone: create an index or let the code create `assistant-index`. Get your API key and note the environment (defaults to `gcp-starter`).
3) Backend deps:
   - `cd backend`
   - `pip install -r requirements.txt`
4) Env vars (PowerShell examples):
   - `$env:PINECONE_API_KEY="YOUR_KEY"`
   - If your env differs: `$env:PINECONE_ENVIRONMENT="your-env"`

## Run
1) Start the API (from `backend`):
   - `uvicorn app:app --reload --host 0.0.0.0 --port 8000`
2) (Optional) Seed sample docs:
   - `python ingest.py`
3) Open the UI:
   - Open `frontend/index.html` directly in a browser, or serve it (`cd frontend && python -m http.server 3000`).

## How to use
- Ask a question in the UI. The backend embeds it, fetches similar snippets, builds a short prompt, hits Ollama, and returns a 2–3 sentence answer with context.

## Notes
- Keep answers short; no agents or chains.
- Ensure Ollama is running locally with `llama3` pulled.
- Install deps in the same environment where you run `uvicorn` to avoid import errors.
