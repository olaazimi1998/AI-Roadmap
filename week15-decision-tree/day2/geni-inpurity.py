from sklearn.tree import DecisionTreeClassifier

X = [
    [18],
    [19],
    [20],
    [30],
    [31],
    [32],
    [35]
]

y = [
    0,
    0,
    0,
    1,
    1,
    1,
    1
]

model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=2,
    random_state=42
)

model.fit(X, y)

prediction = model.predict([[30]])

print("Prediction:", prediction)
from sklearn.tree import plot_tree
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plot_tree(
    model,
    feature_names=["Age"],
    class_names=["No", "Yes"],
    filled=True
)

plt.show()