from pathlib import Path

import joblib

from fastapi import FastAPI
from pydantic import BaseModel, Field


app = FastAPI(
    title="Customer Churn Prediction API",
    description="Predict customer churn using a trained ML model.",
    version="2.0.0",
)


# Load the trained model
PROJECT_DIR = Path(__file__).resolve().parent.parent

MODEL_PATH = (
    PROJECT_DIR
    / "app"
    / "models"
    / "churn_model.joblib"
)

if not MODEL_PATH.exists():
    raise RuntimeError(
        "Trained model not found. "
        "Run: python -m ml.train"
    )

model = joblib.load(MODEL_PATH)


class CustomerData(BaseModel):
    tenure: int = Field(ge=0)
    monthly_charges: float = Field(ge=0)
    support_calls: int = Field(ge=0)


@app.get("/")
def home():
    return {
        "message": "Customer Churn Prediction API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True,
    }


@app.post("/predict")
def predict(customer: CustomerData):

    features = [[
        customer.tenure,
        customer.monthly_charges,
        customer.support_calls,
    ]]

    prediction = int(model.predict(features)[0])

    probabilities = model.predict_proba(features)[0]

    churn_probability = float(
        probabilities[
            list(model.classes_).index(1)
        ]
    )

    return {
        "prediction": prediction,
        "risk_score": round(churn_probability, 4),
        "risk_label": (
            "High" if prediction == 1 else "Low"
        ),
    }