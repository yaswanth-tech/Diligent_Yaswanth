import os
from typing import List, Tuple
from sentence_transformers import SentenceTransformer
import pinecone

PINECONE_INDEX = "assistant-index"
_pinecone_key = os.getenv("PINECONE_API_KEY", "")

# Keep everything lazy and simple for a student project.
pinecone.init(api_key=_pinecone_key, environment="gcp-starter")
if PINECONE_INDEX not in pinecone.list_indexes():
    # Minimal setup: 384 is the dimension for all-MiniLM-L6-v2.
    pinecone.create_index(PINECONE_INDEX, dimension=384)

index = pinecone.Index(PINECONE_INDEX)
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed_text(text: str) -> List[float]:
    return model.encode(text).tolist()


def index_texts(items: List[Tuple[str, str]]):
    """Upsert a list of (id, text) pairs."""
    payload = [
        (doc_id, embed_text(text), {"text": text})
        for doc_id, text in items
    ]
    index.upsert(payload)


def search_similar(query: str, top_k: int = 3):
    """Return small dicts with id and stored text for context building."""
    vector = embed_text(query)
    results = index.query(vector=vector, top_k=top_k, include_metadata=True)
    matches = []
    for match in results.get("matches", []):
        matches.append({
            "id": match.get("id"),
            "score": match.get("score"),
            "text": match.get("metadata", {}).get("text", ""),
        })
    return matches
