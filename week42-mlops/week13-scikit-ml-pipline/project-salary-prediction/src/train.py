import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression


# Load data
df = pd.read_csv(r"C:\Users\olaaz\Documents\AI Roadmap\week13-scikit-ml-pipline\project-salary-prediction\data\employee.csv")
print(df.head())
# Features and target
X = df[["age", "experience"]]
y = df["salary"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])

# Train
pipeline.fit(X_train, y_train)

# Predict
predictions = pipeline.predict(X_test)

# Results
print("Actual:", y_test.values)
print("Predicted:", predictions)