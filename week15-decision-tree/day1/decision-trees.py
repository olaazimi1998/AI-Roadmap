import os

import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [
    [20],
    [22],
    [25],
    [28],
    [35],
    [40],
    [45],
    [50],
]

y = [0, 0, 0, 0, 1, 1, 1, 1]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
)

model = DecisionTreeClassifier(max_depth=2, random_state=42)
model.fit(X_train, y_train)

prediction = model.predict(X_test)
accuracy = accuracy_score(y_test, prediction)
print("Accuracy", accuracy)

plt.figure(figsize=(10, 6))
plot_tree(
    model,
    feature_names=["Age"],
    class_names=["No", "Yes"],
    filled=True,
    rounded=True,
)
plt.title("Decision Tree for Age Classification")
output_path = os.path.join(os.path.dirname(__file__), "tree.png")
plt.savefig(output_path, dpi=200, bbox_inches="tight")
print(f"Graph saved to: {output_path}")
plt.show()
