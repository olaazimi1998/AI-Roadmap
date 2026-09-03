phone_name = input("Phone Name: ")
buy_price = float(input("Buy Price: "))
sell_price = float(input("Sell Price: "))
stock = int(input("Stock: "))
profit = sell_price - buy_price
total_value = sell_price * stock


print("\n --- Product Information ---\n")
print("Phone:", phone_name)
print("Buy Price: $", buy_price)
print("Sell Price: $", sell_price)
print("Stock:", stock)
print("Profit: $" , profit)
print("Total Value: $", total_value)
if stock == 0:
    print("Status: Out of stock")
elif stock < 10:
    print("Status: Low stock")
else:
    print("Status: In stock")

from typing import TypedDict


class Phone(TypedDict):
    name: str
    stock: int
    Brand: str


phones: list[Phone] = [{"name": "iphone 15 pro", "stock": 5, "Brand": "Apple"},
          {"name": "iphone 16 pro", "stock": 6, "Brand": "Apple"},
          {"name": "iphone 14 pro", "stock": 3, "Brand": "Apple"}]
while True:
    print("\n === Mobile Shop ===")
    print("1. Show product")
    print("2. Available product")
    print("3. Exit")

    choice = input("Choose:")
    if choice == "1":
        print("/n -- All product --")
        for phone in phones:
            print(phone["name"], "Stock:", phone["stock"])
    
    elif choice == "2":
        print("\n --available Product--")
        for phone in phones:
            if phone["stock"] > 0:
                print(phone["name"])

    elif choice == "3":
        print("good bye")
        break
    else:
        print("Invalid choice")
        continue

    shop_location = ("Dubai, Diera")
print("Shop location", shop_location)
search = input("Search Phone:").lower()
found = False
for phone in phones:
    if search in phone["name"].lower():
        print("Found", phone["name"],
                  "-",
         phone["sell_price"], "AED")
        found = True
print("phone not found")

sorted_phones = sorted(
    phones,
    key=lambda phone: phone["sell_price"]
)
print("Phone from the cheapest to expensive")
for phone in sorted_phones:
    print(phone["name"], 
          "-",
          phone["sell_price"],
          "AED")


def calculate_profit(buy_price, sell_price):
    profit = sell_price - buy_price
    return profit

try:
    price = float(input(" Price:"))
except ValueError:
    print("Enter a number")

import csv
with open(" products.csv", "r") as file:
    reader = csv.reader(file)
    for product in reader:
        print(product)

import json
with open("products.json", "r") as file:
    data = json.load(file)
    for product in data["products"]:
        print(product["name"], "-", product["sell_price"], "AED")

from datetime import datetime
sale_date = datetime.now()
print("Sale Date:", sale_date.strftime("%Y-%m-%d %H:%M:%S"))


from product import Product

phone = Product("iPhone 15 Pro", 1000, 1200, 5)
print("name:", phone.name)
print(phone.name)
print("Buy Price: $", phone.get_price())
phone.call()



