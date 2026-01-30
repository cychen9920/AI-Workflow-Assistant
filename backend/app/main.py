from fastapi import FastAPI
from sqlalchemy.orm import Session
from .database import SessionLocal
from .llm import analyze_text
from .crud import create_analysis

app = FastAPI()

# get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#define sanity check endpoint
@app.get("/")
def root():
    return {"status": "AI Workflow Assistant running"}

#define endpoint for LLM result generation
@app.post("/analyze")
def analyze(payload: dict):
    result = analyze_text(payload["text"])
    return {"result": result}
