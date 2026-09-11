import pandas as pd

data = { # type: ignore
    "name": ["Ali", "Sara", "Amir", "Mina"],
    "age": [20, 25, 30, 22],
    "score": [80, 95, 75, 88]
}

df = pd.DataFrame(data) # type: ignore

print("DATA:")
print(df)

print("\nFIRST ROWS:")
print(df.head())

print("\nSHAPE:")
print(df.shape)

print("\nCOLUMNS:")
print(df.columns.tolist())

print("\nINFO:")
df.info()

print("\nSTATISTICS:")
print(df.describe())

print("\nAVERAGE SCORE:")
print(df["score"].mean())