import pandas as pd

train = pd.read_csv(r"C:\Users\olaaz\Documents\AI Roadmap\week22-kaggle-competetion\data\train.csv")
test = pd.read_csv(r"C:\Users\olaaz\Documents\AI Roadmap\week22-kaggle-competetion\data\test.csv")

train.head()

test.head()

print(train.head())
print(train.info())
print(train.describe())
print("Train shape:", train.shape)
print("Test shape:", test.shape)