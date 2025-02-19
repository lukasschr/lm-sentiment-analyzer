from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import time


class SequenceClassificationModel:
    """Base class for sequence classification models using Hugging Face transformers."""

    def __init__(self, model_id: str):
        """Initializes the model with the given Hugging Face model ID.

        Args:
            model_id (str): The identifier of the pre-trained model from Hugging Face.
        """
        self._name = None

        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSequenceClassification.from_pretrained(model_id)

        self.pipe = pipeline(
            "text-classification",
            model=model,
            tokenizer=tokenizer,
            top_k=None
        )

    def compute_sentiment(self, text: str) -> tuple:
        """Computes the sentiment of the given text using the model.

        Args:
            text (str): The input text to analyze.

        Returns:
            tuple: A tuple containing the classification result (list of dicts)
                   and the computation time in seconds (float).
        """
        start_time = time.perf_counter()
        result = self.pipe(str(text))
        end_time = time.perf_counter()

        computation_time = end_time - start_time
        return result, computation_time

    # Getter & Setter
    def _get_name(self) -> str:
        return self._name

    def _set_name(self, value: str):
        self._name = value

    name = property(_get_name, _set_name)


class CardiffnlpXlmRobertaBaseSentimentLM(SequenceClassificationModel):
    """Sentiment analysis model using 'cardiffnlp/twitter-xlm-roberta-base-sentiment'."""

    def __init__(self):
        """Initializes the Cardiff NLP XLM-RoBERTa sentiment model."""
        super().__init__("cardiffnlp/twitter-xlm-roberta-base-sentiment")
        self.name = "CardiffnlpXlmRobertaBaseSentimentLM"


class TabularisaiDistilbertMultilingualSentimentLM(SequenceClassificationModel):
    """Sentiment analysis model using 'tabularisai/multilingual-sentiment-analysis'."""

    def __init__(self):
        """Initializes the Tabularis AI DistilBERT sentiment model."""
        super().__init__("tabularisai/multilingual-sentiment-analysis")
        self.name = "TabularisaiDistilbertMultilingualSentimentLM"
