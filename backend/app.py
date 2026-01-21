from fastapi import FastAPI
from pydantic import BaseModel
from llm import generate_reply
from vector_store import index_texts, search_similar

app = FastAPI(title="Simple Assistant API")


class IngestRequest(BaseModel):
    text: str
    doc_id: str | None = None


class ChatRequest(BaseModel):
    message: str


@app.post("/ingest")
def ingest(req: IngestRequest):
    """Save a single text snippet into Pinecone."""
    doc_id = req.doc_id or "doc-" + str(abs(hash(req.text)))[:10]
    index_texts([(doc_id, req.text)])
    return {"status": "ok", "stored": doc_id}


@app.post("/chat")
def chat(req: ChatRequest):
    """Answer a question using nearby snippets and the local LLM."""
    matches = search_similar(req.message, top_k=3)
    context = " ".join([m.get("text", "") for m in matches])
    prompt = (
        "You are a short, helpful assistant for a SaaS product.\n"
        f"Context: {context}\n"
        f"Question: {req.message}\n"
        "Answer in 2-3 sentences."
    )
    answer = generate_reply(prompt)
    return {"reply": answer, "sources": matches}
