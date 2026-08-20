import pandas as pd

data = {
    "product": ["Laptop", "Phone", "Tablet", "Monitor", "Keyboard", "Mouse"],
    "region": ["Istanbul", "Ankara", "Istanbul", "Izmir", "Ankara", "Istanbul"],
    "sales": [1500, 800, 1200, 600, 300, 450]
}

df = pd.DataFrame(data)

print(df)

# if you want to see groupby you must add aggregation function
#df.groupby("column")["value"].sum
print(df.groupby("region"))


#in addition sales of every region
print(df.groupby("region")["sales"].sum())

# in adition sales of mean()
print(df.groupby("region")["sales"].mean())

# Max sales of every region
print(df.groupby("region")["sales"].max())

#min sales of region
print(df.groupby("region")["sales"].min())

result = df.groupby("region")["sales"].agg(["max", "min", "mean", "sum"])
print(result)

#groupby  base on columns:
result = df.groupby(["region", "product"])["sales"].sum()
print(result)

# count of order in every region:
print(df.groupby("region").size())

print(df.groupby("region")["product"].count())

#sorting groupby base on high sales to low
print(df.groupby("region")["sales"].
      sum().sort_values(ascending=False)
      )





