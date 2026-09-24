import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    "age": [20, 25, 30, 35, 40],
    "salary": [2000, 3000, 5000, 7000, 10000],
    "experience": [1, 3, 5, 8, 12]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Create new feature
df["salary_per_experience"] = (
    df["salary"] / df["experience"]
)

print("\nAfter Feature Engineering:")
print(df)

# Scaling
scaler = StandardScaler()

df[["age", "salary", "experience"]] = scaler.fit_transform(
    df[["age", "salary", "experience"]]
)

print("\nAfter Scaling:")
print(df)


import pandas as pd

data = {
    "age": [22, 25, 30, 35, 40, 45, 50],
    "salary": [2500, 3000, 4000, 5500, 8000, 12000, 100000],
    "experience": [1, 2, 5, 8, 12, 20, 25],
    "city": [
        "Dubai",
        "Dubai",
        "Sharjah",
        "Dubai",
        "Abu Dhabi",
        "Dubai",
        "Sharjah"
    ],
    "price": [200000, 250000, 300000, 400000, 500000, 600000, 700000]
}

df = pd.DataFrame(data)

print(df)

df["salary_per_experience"] = (
    df["salary"] / df["experience"]
)
print(df)

df = pd.get_dummies(
    df, 
    columns=["city"]
).astype(int)
print(df)
Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = df[
    (df["salary"] < lower) |
    (df["salary"] > upper)
]

print("Outliers:")
print(outliers)

correlation = df.corr(numeric_only=True)

print("Correlation:")
print(correlation)


from sklearn.preprocessing import StandardScaler

features = [
    "age",
    "salary",
    "experience"
]

scaler = StandardScaler()

df[features] = scaler.fit_transform(
    df[features]
)

print(df)
