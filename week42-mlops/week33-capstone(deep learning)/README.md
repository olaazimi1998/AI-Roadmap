# Deep Learning Sentiment Analysis

A complete deep learning project for classifying review text into three sentiment classes: negative, neutral, and positive.

## Project overview

This project demonstrates a simple NLP pipeline using PyTorch:

1. Load review text from a CSV dataset
2. Clean and tokenize the text
3. Build a vocabulary
4. Convert reviews into bag-of-words vectors
5. Train a small neural network for sentiment classification
6. Evaluate the model
7. Predict the sentiment of new review text

## Problem statement

Given a product review, the model should identify whether the sentiment is negative, neutral, or positive.

## Technologies

- Python
- PyTorch
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Project structure

```text
week33-capstone(deep learning)/
├── data/
│   └── reviews.csv
├── models/
│   ├── sentiment_model.pth
│   ├── vocab.json
│   └── metrics.json
├── notebooks/
│   ├── eda.ipynb
│   ├── preprocessing.ipynb
│   ├── evaluation.ipynb
│   └── test.ipynb
├── src/
│   ├── sentiment_model.py
│   ├── train.py
│   ├── predict.py
│   └── __init__.py
├── README.md
├── requirements.txt
└── .gitignore
```

## Setup

```bash
pip install -r requirements.txt
```

## Training

```bash
cd "week33-capstone(deep learning)"
python src/train.py
```

## Prediction

```bash
cd "week33-capstone(deep learning)"
python src/predict.py "I absolutely loved this product!"
```

Example output:

```text
Prediction: positive (94.56%)
```

## Current model result

The project includes a trained model and evaluation metrics in `models/metrics.json`.
Model accuracy is tracked in the metrics file after training.

## Visualizations

- Sentiment distribution
- Word frequency analysis
- Prediction distribution
- Confusion matrix

## Notes

This project is intentionally lightweight and beginner-friendly, making it suitable for learning the full deep learning workflow without requiring large datasets or heavy infrastructure.