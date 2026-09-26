import numpy as np


def sigmoid(z):
    return 1 / (1 + np.exp(-z))


x = np.array([1, 0])

W = np.array([
    [0.5, 0.2],
    [0.3, 0.7]
])

b = np.array([0.1, 0.1])

z = np.dot(x, W) + b

output = sigmoid(z)

print(output)