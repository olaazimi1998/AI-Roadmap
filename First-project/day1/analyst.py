import pandas as pd
import matplotlib.pyplot as plt

from pathlib import Path
file_path = Path(__file__).parent /"products.csv"
df = pd.read_csv(file_path)
df = pd.DataFrame(df)
print(df)
df.head(5)
df.info()
print(df["sell_price"].mean())
print(df["sell_price"].max())
print(df["sell_price"].min())
print(df["name"].value_counts())

df["profit"] = (df["sell_price"] - df["buy_price"]) * df["stock"]

plt.bar(df["name"], df["profit"])
plt.xlabel("Product Name")
plt.ylabel("Profit")
plt.title("Profit by Product")
plt.xticks(rotation=45, ha='right')
plt.scatter(df["name"], df["profit"], color='red')
plt.plot(df["name"], df["profit"], color='green', marker='o')
plt.show()
















