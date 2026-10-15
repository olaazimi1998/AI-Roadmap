from os import name
from pathlib import Path

import joblib
import mlflow
import mlflow.sklearn
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split


# Project folders
PROJECT_DIR = Path(__file__).resolve().parent.parent

MODEL_DIR = PROJECT_DIR / "app" / "models"
MODEL_PATH = MODEL_DIR / "churn_model.joblib"


def train_model():
    # 1. Create sample customer data
    rng = np.random.default_rng(42)

    number_of_customers = 1000

    tenure = rng.integers(
        1, 73, size=number_of_customers
    )

    monthly_charges = rng.uniform(
        20, 150, size=number_of_customers
    )

    support_calls = rng.integers(
        0, 11, size=number_of_customers
    )

    # 2. Create sample labels
    # 1 = customer leaves
    # 0 = customer stays

    churn = (
        (tenure < 12)
        & (support_calls >= 3)
        & (monthly_charges > 70)
    ).astype(int)

    # 3. Prepare features and labels
    X = np.column_stack(
        [tenure, monthly_charges, support_calls]
    )

    y = churn

    # 4. Split the data
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,
    )

    # 5. Start MLflow experiment tracking
    mlflow.set_experiment("customer-churn-prediction")

    with mlflow.start_run():

        # 6. Create and train the model
        model = LogisticRegression(max_iter=1000)

        model.fit(X_train, y_train)

        # 7. Evaluate the model
        predictions = model.predict(X_test)

        accuracy = accuracy_score(
            y_test,
            predictions,
        )

        # 8. Record parameters and metrics
        mlflow.log_param(
            "model_type",
            "LogisticRegression",
        )

        mlflow.log_param(
            "max_iter",
            1000,
        )

        mlflow.log_param(
            "training_samples",
            len(X_train),
        )

        mlflow.log_metric(
            "accuracy",
            float(accuracy),
        )

        # 9. Save the model in MLflow
        mlflow.sklearn.log_model(
            model,
            name="model",
        )

        # 10. Save a copy for our FastAPI application
        MODEL_DIR.mkdir(
            parents=True,
            exist_ok=True,
        )

        joblib.dump(
            model,
            MODEL_PATH,
        )

        print(f"Model accuracy: {accuracy:.3f}")

        print(
            f"Model saved to: {MODEL_PATH}"
        )


if __name__ == "__main__":
    train_model()