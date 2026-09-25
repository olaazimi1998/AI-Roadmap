import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load data
df = pd.read_csv(r"C:\Users\olaaz\Documents\AI Roadmap\week23-end-toend-ml-project\project-Employee-Salary-Predicton.py\data\salary_data.csv")


# Features and target
X = df.drop("salary", axis=1)
y = df["salary"]


# Identify columns
categorical_features = [
    "education",
    "department"
]

numerical_features = [
    "Age",
    "Experience"
]


# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        (
            "categorical",
            OneHotEncoder(handle_unknown="ignore"),
            categorical_features
        )
    ],
    remainder="passthrough"
)


# Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# Complete pipeline
pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ]
)


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Train
pipeline.fit(X_train, y_train)


# Predict
predictions = pipeline.predict(X_test)


# Evaluate
mae = mean_absolute_error(y_test, predictions)
mse = mean_squared_error(y_test, predictions)
r2 = r2_score(y_test, predictions)


print("MAE:", mae)
print("MSE:", mse)
print("R2:", r2)


# Save model
joblib.dump(
    pipeline,
    "models/salary_model.pkl"
)

print("Model saved!")