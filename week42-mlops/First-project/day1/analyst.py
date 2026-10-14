import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

from sqlalchemy import false

from sqlalchemy import false
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
df.to_csv("C:\\Users\\olaaz\\Documents\\AI Roadmap\\First-project\\day1\\products.csv", index=False)
product_names = df["name"].tolist()
profits = df["profit"].tolist()

plt.bar(product_names, profits)  # type: ignore[reportUnknownMemberType]
plt.xlabel("Product Name") # type: ignore
plt.ylabel("Profit")  # type: ignore[reportUnknownMemberType]
plt.title("Profit by Product") # type: ignore
plt.xticks(rotation=45, ha='right') # type: ignore
plt.scatter(product_names, profits, color='red') # type: ignore
plt.plot(product_names, profits, color='green', marker='o') # type: ignore
plt.show() # type: ignore
















