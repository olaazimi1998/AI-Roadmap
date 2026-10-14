from pathlib import Path

import joblib
import pandas as pd
from fastapi import FastAPI, Query

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "salary_model.pkl"
FEATURE_COLUMNS = ["age", "experience", "education", "joblevel", "country"]

app = FastAPI(title="Employee salary Prediction API")


def load_model():
    if not MODEL_PATH.exists():
        import sys

        sys.path.append(str(PROJECT_ROOT))
        from src.preprocessing import train_and_evaluate

        train_and_evaluate()

    return joblib.load(MODEL_PATH)


model = load_model()


@app.get("/")
def home():
    return {"message": "Employee Salary prediction API"}


@app.get("/predict")
def predict(
    age: int = Query(..., description="Employee age"),
    experience: int = Query(..., description="Years of experience"),
    country: str = Query(..., description="Employee country"),
    education: str = Query(..., description="Education level"),
    joblevel: str = Query("Mid", description="Job level (default: Mid)"),
):
    data = pd.DataFrame(
        [{
            "age": age,
            "experience": experience,
            "education": education,
            "joblevel": joblevel,
            "country": country,
        }],
        columns=FEATURE_COLUMNS,
    )
    prediction = model.predict(data)

    return {"predicted_salary": float(prediction[0])}


# uvicorn api.main:app --reload