from fastapi import FastAPI
from pydantic import BaseModel

from .sentiment_analyzer import SentimentAnalyzer


sentiment_analyzer = SentimentAnalyzer()
app = FastAPI()


class Text(BaseModel):
    """Request model for text input."""
    text: str


@app.get("/", response_model=dict)
def read_root() -> dict:
    """Root endpoint returning a welcome message.

    Returns:
        dict: A welcome message.
    """
    return {"message": "Welcome"}


@app.put("/analyze", response_model=dict)
def analyze(text: Text) -> dict:
    """Analyzes the sentiment of the provided text.

    Args:
        text (Text): Input text wrapped in a Pydantic model.

    Returns:
        dict: A dictionary containing:
            - used_model (str): The name of the sentiment analysis model.
            - computation_time (float): The time taken for the sentiment analysis.
            - model_output (list): The output of the sentiment analysis model.
    """
    model_output, computation_time = sentiment_analyzer.analyze(text.text)
    return {
        "used_model": sentiment_analyzer.model.name,
        "computation_time": computation_time,
        "model_output": model_output
    }