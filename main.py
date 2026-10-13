from model import HousePriceModel


model = HousePriceModel()

price = model.predict(100)

print(f"Predicted house price: {price}")