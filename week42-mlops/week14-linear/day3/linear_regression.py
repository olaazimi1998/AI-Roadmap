import numpy as np
class LinearRegressionScratch:
    def __init__(self, learning_rate=0.01, epochs=1000):
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.w = 0
        self.b = 0

    def predict(self, X):
        return self.w * X + self.b

    def compute_cost(self, X, y):

        predictions = self.predict(X)

        errors = predictions - y

        cost = np.mean(errors ** 2)

        return cost

    def fit(self, X, y):

        n = len(X)

        for epoch in range(self.epochs):

            predictions = self.predict(X)

            errors = predictions - y

            dw = (2 / n) * np.sum(X * errors)

            db = (2 / n) * np.sum(errors)

            self.w = self.w - self.learning_rate * dw

            self.b = self.b - self.learning_rate * db


            if epoch % 100 == 0:
                cost = self.compute_cost(X, y)
                print(f"Epoch {epoch}, Cost: {cost:.2f}")
                