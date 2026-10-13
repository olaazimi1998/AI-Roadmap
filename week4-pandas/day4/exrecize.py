
import pandas as pd
data = {
    "product": ["Laptop", "Phone", "Laptop", "Tablet", "Phone", "Tablet"],
    "region": ["Istanbul", "Ankara", "Istanbul", "Izmir", "Ankara", "Istanbul"],
    "sales": [1500, 800, 2000, 600, 1200, 900]
}

df = pd.DataFrame(data)

print(df.groupby("region")["sales"].sum())

print(df.groupby("region")["sales"].mean())

print(df.groupby("region")["sales"].max())

print(df.groupby(["region", "product"])["sales"].sum())
print(df.groupby("region")["sales"].sum().sort_values(ascending=False))


#making dataframes

customers = pd.DataFrame({
    "customer_id": [1, 2, 3],
    "customer_name": ["Ali", "Sara", "Amir"],
    "region": ["Istanbul", "Ankara", "Izmir"]
})

orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104],
    "customer_id": [1, 2, 1, 3],
    "product": ["Laptop", "Phone", "Tablet", "Monitor"],
    "sales": [1500, 800, 1200, 600]
})

print(orders)

print(customers)
# Merge
print(orders.merge(customers, on="customer_id"))

# on is connect to dataframe   on=: we say this key
print(orders)
print(customers)
print("\n")

#left mergeتمام سفارش‌های orders را نگه دار و اطلاعات مشتری را اضافه کن.

print(orders.merge(customers, on="customer_id", how="left"))

print("\n")
#right mergeیعنی همه customerها را نگه می‌دارد.

print(orders.merge(customers, on="customer_id", how="right"))

print("\n")
# outerمه رکوردهای هر دو جدول را نگه دار.

#حتی اگر match وجود نداشته باشد.

#در آن حالت ممکن است NaN ایجاد شو
print(orders.merge(customers, on="customer_id", how="outer"))

print("\n")














