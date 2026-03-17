from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def detect_intent(text):

    result = classifier(text)[0]["label"]

    if result == "NEGATIVE":
        return "insurance claim"

    return "general service"
