import sys

from sentiment_model import predict_text


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/predict.py \"I love this product\"")
        raise SystemExit(1)

    text = " ".join(sys.argv[1:])
    label, score = predict_text(text)
    print(f"Prediction: {label} ({score:.2%})")
