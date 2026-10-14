from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_ROOT / "data" / "salary_data.csv"
MODEL_DIR = PROJECT_ROOT / "models"
MODEL_PATH = MODEL_DIR / "salary_model.pkl"

CATEGORICAL_FEATURES = ["education", "joblevel", "country"]
NUMERICAL_FEATURES = ["age", "experience"]
TARGET_COLUMN = "salary"
FEATURE_COLUMNS = NUMERICAL_FEATURES + CATEGORICAL_FEATURES


def load_data(csv_path: str | Path = DATA_PATH) -> pd.DataFrame:
    return pd.read_csv(csv_path)


def split_features_target(df: pd.DataFrame):
    X = df[FEATURE_COLUMNS]
    y = df[TARGET_COLUMN]
    return X, y


def build_preprocessor() -> ColumnTransformer:
    return ColumnTransformer(
        transformers=[
            (
                "cat",
                OneHotEncoder(handle_unknown="ignore"),
                CATEGORICAL_FEATURES,
            ),
            (
                "num",
                "passthrough",
                NUMERICAL_FEATURES,
            ),
        ]
    )


def build_pipeline() -> Pipeline:
    model = RandomForestRegressor(n_estimators=200, random_state=42)
    return Pipeline(
        steps=[
            ("preprocessor", build_preprocessor()),
            ("model", model),
        ]
    )


def train_and_evaluate(csv_path: str | Path = DATA_PATH, model_path: str | Path = MODEL_PATH):
    df = load_data(csv_path)
    X, y = split_features_target(df)
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    predictions = pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    model_path = Path(model_path)
    model_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(pipeline, model_path)

    metrics = {
        "mae": mae,
        "rmse": rmse,
        "r2": r2,
    }
    return pipeline, metrics


if __name__ == "__main__":
    model, metrics = train_and_evaluate()
    print("MAE:", metrics["mae"])
    print("RMSE:", metrics["rmse"])
    print("R²:", metrics["r2"])
    print(f"Model saved to: {MODEL_PATH}")
