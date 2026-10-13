
Step 1
Create project

       ↓

Step 2
Prepare dataset

       ↓

Step 3
Train baseline model

       ↓

Step 4
Add MLflow

       ↓

Step 5
Log parameters

       ↓

Step 6
Log metrics

       ↓

Step 7
Log artifacts

       ↓

Step 8
Run 5 experiments

       ↓

Step 9
Compare runs

       ↓

Step 10
Choose best model

       ↓

Step 11
Register/version model

       ↓

Step 12
README + GitHub

          MACHINE LEARNING
                 │
                 ▼
             Experiment
                 │
        ┌────────┴────────┐
        ▼        ▼        ▼
      Run 1    Run 2    Run 3
        │        │        │
        ▼        ▼        ▼
     Params   Params   Params
     Metrics  Metrics  Metrics
     Models   Models   Models
     Files    Files    Files
        │        │        │
        └────────┼────────┘
                 ▼
          Compare Runs
                 │
                 ▼
           Best Model
                 │
                 ▼
          Model Registry
                 │
                 ▼
             Versioning

## Run and view the model

Run the training script from this directory:

```bash
python main.py
```

The script stores tracking data in `mlflow.db` in this directory and registers
the model as `IrisRandomForest`. Start the UI against that same database:

```bash
python -m mlflow ui --backend-store-uri "sqlite:///C:/path/to/week36-mlflow/day1/mlflow.db"
```

Replace the path with the absolute path to this project's `mlflow.db`. The run's
model files are under the run's **Artifacts**; the registered version is under
**Models** in the UI.