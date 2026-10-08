from pathlib import Path

import mlflow
import mlflow.sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


tracking_uri = "sqlite:///C:/path/to/week36-mlflow/day1/mlflow.db"
mlflow.set_tracking_uri(tracking_uri)
mlflow.set_experiment("Iris Classification")


with mlflow.start_run(run_name="iris-rf-baseline") as run:

    n_estimators = 100
    max_depth = 5

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42
    )

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)

    mlflow.log_metric("accuracy", accuracy)

    mlflow.sklearn.log_model(
        model,
        artifact_path="random_forest_model",
        registered_model_name="IrisRandomForest",
        skops_trusted_types=["sklearn.tree._tree.Tree"],
    )

    print("Run ID:", run.info.run_id)
    print("Tracking URI:", tracking_uri)
    print("Accuracy:", accuracy)   
    # python -m mlflow ui --backend-store-uri "sqlite:///C:/path/to/week36-mlflow/day1/mlflow.db"