from .config import CONFIG


class SentimentAnalyzer:

    def __init__(self):
        if CONFIG["sentiment-analyer"]["model"] == "CardiffnlpXlmRobertaBaseSentimentLM":
            from .models import CardiffnlpXlmRobertaBaseSentimentLM
            self.model = CardiffnlpXlmRobertaBaseSentimentLM()
        elif CONFIG["sentiment-analyer"]["model"] == "TabularisaiDistilbertMultilingualSentimentLM":
            from .models import TabularisaiDistilbertMultilingualSentimentLM
            self.model = TabularisaiDistilbertMultilingualSentimentLM()
        else:
            print("Error") # Todo

    def analyze(self, text: str):
        return self.model.compute_sentiment(text)