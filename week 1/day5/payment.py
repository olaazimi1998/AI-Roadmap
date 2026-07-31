from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class Paypal(Payment):
    def pay(self, amount):
        print(f"paid {amount} $ with paypal.")


class Creditcard(Payment):
    def pay(self, amount):
        print(f"paid {amount} $ with creditcard.")
