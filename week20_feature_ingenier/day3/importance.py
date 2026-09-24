#Feature Importance
#Now we learn another important method for Feature Selection.

#🇬🇧 English
#Feature importance tells us how useful each feature is for making predictions.




import pandas as pd
from sklearn.tree import DecisionTreeRegressor


data = {
    "area": [100, 150, 200, 250, 300, 350],
    "bedrooms": [2, 3, 3, 4, 4, 5],
    "age": [10, 8, 5, 3, 2, 1],
    "price": [200000, 300000, 400000, 500000, 600000, 700000]
}
df = pd .DataFrame(data)

X = df[["area", "bedrooms", "age"]]
y = df["price"]

model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)

importance = model.feature_importances_

print(importance)





feature_importance = pd.Series(
    model.feature_importances_,
    index=X.columns
)

print("Feature Importance:")
print(feature_importance)

feature_importance = feature_importance.sort_values(
    ascending=False
)

print(feature_importance)

feature_importance.plot(kind="pie")

import matplotlib.pyplot as plt

plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Importance")

plt.show()


