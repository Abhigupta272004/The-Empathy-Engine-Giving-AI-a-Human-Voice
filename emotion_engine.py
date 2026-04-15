#Transformer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def detect_emotion(text):
    score = analyzer.polarity_scores(text)["compound"]

    if score > 0.5:
        return "very_positive"
    elif score > 0.2:
        return "positive"
    elif score < -0.5:
        return "very_negative"
    elif score < -0.2:
        return "negative"
    else:
        return "neutral"