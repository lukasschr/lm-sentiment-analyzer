from fastapi import FastAPI
from pydantic import BaseModel

from .sentiment_analyzer import SentimentAnalyzer

sentiment_analyzer = SentimentAnalyzer()
app = FastAPI()

class Text(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Willkommen"}

@app.put("/analyze")
def analyze(text: Text):
    result = sentiment_analyzer.analyze(text.text)
    return {"result": result}