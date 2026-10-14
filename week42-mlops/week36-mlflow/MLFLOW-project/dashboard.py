import os
from pathlib import Path

import mlflow
import pandas as pd
import streamlit as st

os.environ.setdefault("MLFLOW_ALLOW_FILE_STORE", "true")

project_dir = Path(__file__).resolve().parent
tracking_uri = (project_dir / "mlruns").as_uri()
mlflow.set_tracking_uri(tracking_uri)

st.set_page_config(page_title="MLflow Dashboard", page_icon="📊", layout="wide")
st.title("Iris Classification Dashboard")
st.caption("Model experiment overview tracked in MLflow")

experiment_name = "Iris Classification"
experiments = mlflow.search_experiments(filter_string=f"name = '{experiment_name}'")

if not experiments:
    st.warning("No MLflow experiment found. Run the training script first.")
    st.stop()

experiment = experiments[0]
runs_df = mlflow.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["attributes.start_time DESC"],
    max_results=20,
)

if runs_df.empty:
    st.warning("No successful runs are available yet.")
    st.stop()

runs_df = runs_df.copy()
runs_df["start_time"] = pd.to_datetime(runs_df["start_time"], unit="ms")
for column in ["params.n_estimators", "params.max_depth", "metrics.accuracy"]:
    if column in runs_df.columns:
        runs_df[column] = pd.to_numeric(runs_df[column], errors="coerce")

st.subheader("Overview")
summary_col1, summary_col2, summary_col3 = st.columns(3)
summary_col1.metric("Runs", len(runs_df))
summary_col2.metric("Best accuracy", f"{runs_df['metrics.accuracy'].max():.4f}")
summary_col3.metric("Latest run", runs_df["start_time"].max().strftime("%Y-%m-%d %H:%M"))

accuracy_chart = runs_df.sort_values("start_time").set_index("start_time")
if "metrics.accuracy" in accuracy_chart.columns:
    st.subheader("Accuracy over time")
    st.line_chart(accuracy_chart[["metrics.accuracy"]])

st.subheader("Run details")
param_df = runs_df[[
    "start_time",
    "tags.mlflow.runName",
    "params.n_estimators",
    "params.max_depth",
    "params.dataset",
    "metrics.accuracy",
]].sort_values("start_time", ascending=False)

st.dataframe(param_df, use_container_width=True, hide_index=True)

st.subheader("Best run")
best_index = runs_df["metrics.accuracy"].idxmax()
best_run = runs_df.loc[best_index]

st.json({
    "run_id": best_run["run_id"],
    "accuracy": round(float(best_run["metrics.accuracy"]), 4),
    "n_estimators": best_run.get("params.n_estimators"),
    "max_depth": best_run.get("params.max_depth"),
    "dataset": best_run.get("params.dataset"),
    "started_at": best_run["start_time"].isoformat() if pd.notna(best_run["start_time"]) else None,
})
