from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

    
class SequenceClassificationModel:

    def __init__(self, model_id):
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSequenceClassification.from_pretrained(model_id)

        self.pipe = pipeline(
            "text-classification",
            model=model,
            tokenizer=tokenizer,
            top_k=None
        )
    
    def compute_sentiment(self, text:str):
        return self.pipe(str(text))


class CardiffnlpXlmRobertaBaseSentimentLM(SequenceClassificationModel):

    def __init__(self):
        super().__init__("cardiffnlp/twitter-xlm-roberta-base-sentiment")


class TabularisaiDistilbertMultilingualSentimentLM(SequenceClassificationModel):

    def __init__(self):
        super().__init__("tabularisai/multilingual-sentiment-analysis")


# https://huggingface.co/ProsusAI/finbert