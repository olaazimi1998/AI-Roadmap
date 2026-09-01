class Product:
    def __init__(self, name, buy_price, sell_price, stock):
        self.name = name
        self._buy_price = buy_price
        self.sell_price = sell_price
        self.stock = stock
    def get_price(self):
        return self._buy_price
class smartphone(Product):
    def call(self):
        print(self.name, " can make calls")

