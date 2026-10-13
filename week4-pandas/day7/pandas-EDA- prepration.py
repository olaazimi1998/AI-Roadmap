import pandas as pd
# EDA means Exploratory Data Analysis
# It means exploring and understanding your dataset before building a Machine Learning model
#imagine someone give you (movies.cssv)
# you shouldnt do model.fit(X, y)



import pandas as pd

sales = pd.DataFrame({
    "customer_id": [1, 2, 1, 3, 2, 4],
    "product": [
        "Phone",
        "Laptop",
        "Phone",
        "Tablet",
        "Laptop",
        "Phone"
    ],
    "region": [
        "Dubai",
        "Dubai",
        "Sharjah",
        "Abu Dhabi",
        "Dubai",
        "Sharjah"
    ],
    "sales": [
        1000,
        2500,
        1200,
        1800,
        3000,
        1500
    ]
})


# tASK 1: inspect
print(sales.head())

print(sales.shape)

print(sales.info())

#Task2: statistics
print(sales.describe())

#Task3:total sales
print(sales["sales"].sum())

#Average sales
print(sales["sales"].mean())

#sales by region
print(sales.groupby("region")["sales"].sum())

#sales by products
print(sales.groupby("product")["sales"].sum())

# region products
print(sales.groupby(["region", "product"])["sales"].sum())

table = pd.pivot_table(sales,
            values="sales",
            index="region",
            columns="product",
            aggfunc="sum",
            fill_value=0)

print(table)

#workflow
#1. Load
#   ↓
#2. Inspect
#   ↓
#3. Clean
#   ↓
#4. Analyze
#   ↓
#5. Group
#   ↓
#6. Merge
#   ↓
#7. Pivot
#   ↓
#8. Extract Insights