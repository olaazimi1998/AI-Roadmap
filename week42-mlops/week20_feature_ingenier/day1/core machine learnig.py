#What is Feature Engineering?
#Feature Engineering یعنی:
#
#Taking existing data and creating better information/features for the model.

import pandas as pd
data = {
    "area":[100, 200, 300, 400],
    "bedrooms": [2, 4, 6, 8],
    "price": [200000, 300000, 400000, 500000]
}
df = pd.DataFrame(data)
print(df)

df["area_per_bedroom"] = df["area"] / df["bedrooms"]
print(df)

df["year_built"] = [2010, 2005, 1990, 1980]
print(df)
current_year = 2026

df["house_age"] = current_year - df["year_built"]

print(df)

data = {
    "area": [100, 150, 200],
    "city": ["Dubai", "Abu Dhabi", "Dubai"]
}

df = pd.DataFrame(data)

print(df)

#pd.get_dumies()

df_encoded = pd.get_dummies(df, columns=["city"]).astype(int)
print(df_encoded)



print("--------------------------")
from sklearn.preprocessing import LabelEncoder
encoder = LabelEncoder()
df["city_encoding"] = encoder.fit_transform(df["city"]) # type: ignore
print(df) 


import pandas as pd

data = {
    "salary": [3000, 3500, 4000, 4500, 5000, 5500, 100000]
}

df = pd.DataFrame(data)

Q1 = df["salary"].quantile(0.25)
Q3 = df["salary"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)

print("Lower:", lower_bound)
print("Upper:", upper_bound)


outliers = df[
    (df["salary"] < lower_bound) |
    (df["salary"] > upper_bound)
]

print("Outliers:")
print(outliers)


import numpy as np

df["log_salary"] = np.log1p(df["salary"])

print(df)


import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    "age": [20, 25, 30, 35, 40],
    "salary": [2000, 3000, 5000, 8000, 10000]
}

df = pd.DataFrame(data)

scaler = StandardScaler()

df[["age", "salary"]] = scaler.fit_transform(
    df[["age", "salary"]]
)

print(df)




