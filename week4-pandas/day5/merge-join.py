import pandas as pd
customers = pd.DataFrame({
    "customer_id": [1, 2, 3, 4],
    "name": ["Ali", "Sara", "John", "Mary"]
})
orders = pd.DataFrame({
    "order_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 1, 3, 5],
    "amount": [100, 200, 150, 300, 250]
})

print(pd.merge(customers, orders, on="customer_id", how="inner"))
left_df = pd.merge(customers, orders, on="customer_id", how="left")
print(left_df)


print(pd.merge(customers, orders, on="customer_id", how="right"))


# which orders doesnt have customers:
no_orders = left_df[left_df["order_id"].isna()] 
print(no_orders)

# amount of the customers buys
task_4 = left_df.groupby("customer_id")["amount"].sum()
print(task_4)

task_5 = left_df.groupby(["customer_id", "name"])["amount"].sum().reset_index()
task_5 = task_5.rename(columns={"amount": "total_spent"})
print(task_5)

