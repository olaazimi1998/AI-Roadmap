from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Iterable, Tuple

import numpy as np
import pandas as pd
import torch
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from torch import nn

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "reviews.csv"
MODEL_PATH = ROOT / "models" / "sentiment_model.pth"
VOCAB_PATH = ROOT / "models" / "vocab.json"
METRICS_PATH = ROOT / "models" / "metrics.json"

LABEL_TO_ID = {"negative": 0, "neutral": 1, "positive": 2}
ID_TO_LABEL = {value: key for key, value in LABEL_TO_ID.items()}
TOKEN_RE = re.compile(r"[a-z']+")


class SentimentNet(nn.Module):
    def __init__(self, vocab_size: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(vocab_size, 32),
            nn.ReLU(),
            nn.Linear(32, 3),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)


def clean_text(text: str) -> str:
    return " ".join(TOKEN_RE.findall(str(text).lower()))


def build_vocab(reviews: Iterable[str]) -> Dict[str, int]:
    vocab: Dict[str, int] = {}
    for review in reviews:
        for token in clean_text(review).split():
            if token not in vocab:
                vocab[token] = len(vocab)
    return vocab


def encode_review(review: str, vocab: Dict[str, int]) -> np.ndarray:
    vector = np.zeros(len(vocab), dtype=np.float32)
    for token in clean_text(review).split():
        idx = vocab.get(token)
        if idx is not None:
            vector[idx] += 1.0
    return vector


def load_dataset(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_csv(path)
    if {"review", "sentiment"} - set(df.columns):
        raise ValueError("CSV must contain 'review' and 'sentiment' columns.")
    df["review"] = df["review"].astype(str)
    df["sentiment"] = df["sentiment"].astype(str).str.lower()
    return df


def train_model() -> Dict[str, float]:
    df = load_dataset()
    reviews = df["review"].tolist()
    labels = df["sentiment"].map(LABEL_TO_ID).to_numpy()

    vocab = build_vocab(reviews)
    X = np.vstack([encode_review(review, vocab) for review in reviews]).astype(np.float32)
    y = labels.astype(np.int64)

    model = SentimentNet(len(vocab))
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=0.03)

    X_train_t = torch.tensor(X)
    y_train_t = torch.tensor(y)

    model.train()
    for epoch in range(1, 200):
        optimizer.zero_grad()
        logits = model(X_train_t)
        loss = criterion(logits, y_train_t)
        loss.backward()
        optimizer.step()

    model.eval()
    with torch.no_grad():
        predictions = model(X_train_t).argmax(dim=1)

    accuracy = accuracy_score(y, predictions.numpy())
    report = classification_report(
        y,
        predictions.numpy(),
        target_names=["negative", "neutral", "positive"],
        output_dict=True,
    )
    cm = confusion_matrix(y, predictions.numpy(), labels=[0, 1, 2])

    MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
    torch.save(
        {
            "model_state_dict": model.state_dict(),
            "vocab": vocab,
            "label_to_id": LABEL_TO_ID,
            "id_to_label": ID_TO_LABEL,
        },
        MODEL_PATH,
    )

    with VOCAB_PATH.open("w", encoding="utf-8") as f:
        json.dump(vocab, f, ensure_ascii=False, indent=2)

    metrics = {
        "accuracy": float(accuracy),
        "classification_report": report,
        "confusion_matrix": cm.tolist(),
    }
    with METRICS_PATH.open("w", encoding="utf-8") as f:
        json.dump(metrics, f, ensure_ascii=False, indent=2)

    return {
        "accuracy": float(accuracy),
        "train_samples": int(len(X)),
        "test_samples": 0,
    }


def predict_text(text: str, model_path: Path = MODEL_PATH, vocab_path: Path = VOCAB_PATH) -> Tuple[str, float]:
    with vocab_path.open("r", encoding="utf-8") as f:
        vocab = json.load(f)

    vector = encode_review(text, vocab).astype(np.float32)
    model = SentimentNet(len(vocab))
    checkpoint = torch.load(model_path, map_location="cpu")
    model.load_state_dict(checkpoint["model_state_dict"])
    model.eval()

    with torch.no_grad():
        logits = model(torch.tensor(vector.reshape(1, -1)))
        probabilities = torch.softmax(logits, dim=1).numpy()[0]
        predicted_index = int(logits.argmax(dim=1).item())

    label = ID_TO_LABEL[predicted_index]
    score = float(probabilities[predicted_index])
    return label, score


if __name__ == "__main__":
    result = train_model()
    print(f"Training complete. Accuracy: {result['accuracy']:.2%}")
