from pathlib import Path

import joblib
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "salary_model.pkl"
FEATURE_COLUMNS = ["age", "experience", "education", "joblevel", "country"]


def load_model(model_path: str | Path = MODEL_PATH):
    return joblib.load(model_path)


def predict_salary(payload, model=None):
    if model is None:
        model = load_model()

    if isinstance(payload, dict):
        row = pd.DataFrame([payload], columns=FEATURE_COLUMNS)
    elif isinstance(payload, pd.DataFrame):
        row = payload[FEATURE_COLUMNS]
    else:
        raise TypeError("payload must be a dictionary or DataFrame")

    prediction = model.predict(row)
    return float(prediction[0])


if __name__ == "__main__":
    sample = {
        "age": 35,
        "experience": 8,
        "education": "Master",
        "joblevel": "Senior",
        "country": "USA",
    }

    salary_prediction = predict_salary(sample)
    print(f"Predicted salary: ${salary_prediction:,.2f}")
