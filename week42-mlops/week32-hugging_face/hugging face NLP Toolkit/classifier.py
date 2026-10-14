from transformers import pipeline 

def analyze_sentiment(text):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)

    return result[0]

if __name__ == "__main__":
    text = input("enter a sentence: ")

    result = analyze_sentiment(text)
    
    print("\nSentiment:", result["label"])
    print("Confidence:", result["score"])