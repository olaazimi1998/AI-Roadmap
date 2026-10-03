from sentiment_model import train_model


if __name__ == "__main__":
    result = train_model()
    print(f"Training samples: {result['train_samples']}")
    print(f"Accuracy: {result['accuracy']:.2%}")
