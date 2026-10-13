import os
from pathlib import Path

import mlflow
import mlflow.sklearn
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

os.environ.setdefault("MLFLOW_ALLOW_FILE_STORE", "true")

project_dir = Path(__file__).resolve().parent
tracking_uri = project_dir / "mlruns"
mlflow.set_tracking_uri(tracking_uri.as_uri())
mlflow.set_experiment("Iris Classification")


data = load_iris()
X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

with mlflow.start_run(run_name="iris-rf-baseline") as run:
    n_estimators = 100
    max_depth = 5

    model = RandomForestClassifier(
        n_estimators=n_estimators,
        max_depth=max_depth,
        random_state=42,
    )

    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    mlflow.log_param("n_estimators", n_estimators)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("dataset", "iris")
    mlflow.log_param("test_size", 0.2)
    mlflow.log_metric("accuracy", accuracy)
    class_distribution = {
        str(label): int((y == idx).sum())
        for idx, label in enumerate(data.target_names)
    }

    mlflow.log_dict(
        {
            "samples": len(X),
            "feature_count": X.shape[1],
            "target_names": list(data.target_names),
            "class_distribution": class_distribution,
        },
        artifact_file="dataset_summary.json",
    )

    mlflow.sklearn.log_model(
        model,
        artifact_path="random_forest_model",
        skops_trusted_types=["sklearn.tree._tree.Tree"],
    )

    print(f"Run ID: {run.info.run_id}")
    print(f"Accuracy: {accuracy:.4f}")