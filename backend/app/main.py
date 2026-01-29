from fastapi import FastAPI
from app.llm import analyze_text

app = FastAPI()

@app.get("/")
def root():
    return {"status": "AI Workflow Assistant running"}

@app.post("/analyze")
def analyze(payload: dict):
    result = analyze_text(payload["text"])
    return {"result": result}
