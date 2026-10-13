from abc import ABC, abstractmethod

class MLModel(ABC):

    @abstractmethod
    def train(self):
        pass

    @abstractmethod
    def predict(self):
        pass

class LinearRegression(MLModel):

    def train(self):
        print("linear Regeression is training")

    def predict(self):
        print("predicting")


class DecisionTree(MLModel):
    def train(self):
        print("Decision Tree is training")

    def predict(self):
        print("predicting")



