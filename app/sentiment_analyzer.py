from .config import CONFIG


class SentimentAnalyzer:
    """A sentiment analysis handler that dynamically loads a model based on configuration.

    This class initializes the appropriate sentiment analysis model as specified in the configuration file
    and provides a method to analyze text sentiment.
    """

    def __init__(self):
        """Initializes the SentimentAnalyzer and loads the appropriate sentiment model based on CONFIG.

        Raises:
            KeyError: If the specified model name is not found in the configuration.
        """
        model_name = CONFIG["sentiment-analyer"]["model"]

        if model_name == "CardiffnlpXlmRobertaBaseSentimentLM":
            from .models import CardiffnlpXlmRobertaBaseSentimentLM
            self.model = CardiffnlpXlmRobertaBaseSentimentLM()
        elif model_name == "TabularisaiDistilbertMultilingualSentimentLM":
            from .models import TabularisaiDistilbertMultilingualSentimentLM
            self.model = TabularisaiDistilbertMultilingualSentimentLM()
        else:
            raise KeyError(f"Error: Invalid model '{model_name}' specified in configuration.")

    def analyze(self, text: str) -> tuple:
        """Analyzes the sentiment of the given text using the configured model.

        Args:
            text (str): The input text to be analyzed.

        Returns:
            tuple: A tuple containing the sentiment analysis result (list of dicts)
                   and the computation time in seconds (float).
        """
        return self.model.compute_sentiment(text)
