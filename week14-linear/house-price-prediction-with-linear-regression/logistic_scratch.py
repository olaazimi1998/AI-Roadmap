import numpy as np


# -------------------------
# 1. Dataset
# -------------------------

X = np.array([10, 20, 30, 40, 50, 60], dtype=float)

y = np.array([0, 0, 0, 1, 1, 1], dtype=float)


# -------------------------
# 2. Sigmoid function
# -------------------------

def sigmoid(z):
    return 1 / (1 + np.exp(-z))


# -------------------------
# 3. Parameters
# -------------------------

w = 0.0
b = 0.0

learning_rate = 0.01
epochs = 1000

n = len(X)


# -------------------------
# 4. Training
# -------------------------

for epoch in range(epochs):

    # Calculate z
    z = w * X + b

    # Calculate probability
    y_pred = sigmoid(z)

    # Calculate gradients
    dw = (1 / n) * np.sum(X * (y_pred - y))
    db = (1 / n) * np.sum(y_pred - y)

    # Update parameters
    w = w - learning_rate * dw
    b = b - learning_rate * db


# -------------------------
# 5. Show learned values
# -------------------------

print("Weight:", w)
print("Bias:", b)


# -------------------------
# 6. New prediction
# -------------------------

age = 45

z = w * age + b

probability = sigmoid(z)

prediction = 1 if probability >= 0.5 else 0


print("Age:", age)
print("Probability:", probability)
print("Prediction:", prediction)