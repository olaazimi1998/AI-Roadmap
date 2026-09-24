import pandas as pd 

import numpy as np

def prepare_features(train):
    train["Age"].fillna(train["Age"].median(), inplace=True)
    train["Embarked"].fillna(train["Embarked"].mode()[0], inplace=True)

    train["Sex"] = train["Sex"].map({"male": 1, "female": 0})
    train["Embarked"] = train["Embarked"].map({"S": 0, "C": 1, "Q": 2})

    train = train.drop(["Name", "Ticket", "Cabin"], axis=1)
