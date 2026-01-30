import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3.1"

"""
    Given text, send to local Ollama model and return the model's
    analysis (classification, summary, actions)
"""
def analyze_text(text: str) -> dict:
    prompt = f"""
    You are an AI workflow assistant.

    Return ONLY valid JSON with:
    - classification: short label
    - summary: 1-2 sentences
    - actions: list of suggested next steps

    Text:
    {text}
    """

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    response.raise_for_status()
    raw = response.json()["response"] #convert to dict

    return raw

if __name__ == "__main__":
    print(analyze_text("Customer reports login error after update."))
