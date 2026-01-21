import requests


def generate_reply(prompt: str) -> str:
    """Call a local Ollama model and return the text."""
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "llama3", "prompt": prompt},
        timeout=30,
    )
    data = response.json()
    return data.get("response", "").strip()
