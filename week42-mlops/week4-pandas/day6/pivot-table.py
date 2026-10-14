import pandas as pd
df = pd.DataFrame({
    "region": ["Dubai", "Dubai", "Abudhabi", "Abudhabi", "Dubai"],
    "product": ["Phone", "Laptop", "Phone", "Laptop", "Phone"], 
    "sales": [1000, 2000, 1500, 2500, 1200]
})

# calculate average sales:
pivot = pd.pivot_table(
    df, 
    values="product",
    index="sales",
    columns="region",
    aggfunc="max"
)
print(pivot)

#"mean"
#"sum"
#"max"
#"min"
#"count"

pivot = pd.pivot_table(df,
        values="sales", 
        index="region",
        columns="product",
        aggfunc="sum")
print(pivot)
#pivot_table() → great for summary tables


pivot = pd.pivot_table(df,
    values="sales",
    index="region",
    columns="product",
    aggfunc=["mean", "sum", "max"]
)
print(pivot)

df = pd.DataFrame({
    "region": ["Dubai", "Dubai", "Abu Dhabi", "Abu Dhabi"],
    "product": ["Phone", "Laptop", "Phone", "Laptop"],
    "sales": [1000, 2000, 1500, 2500],
    "quantity": [2, 1, 3, 2]
})

pivot = pd.pivot_table(df,
    values=["sales", "quantity"],
     index="region",
       columns="product",
       aggfunc=["sum"])

print(pivot)
#pivot_table() یک جدول خلاصه ایجاد می‌کند که داده‌ها را بر اساس ردیف‌ها و ستون‌ها گروه‌بندی کرده و یک عملیات آماری روی آنها انجام می‌دهد.












