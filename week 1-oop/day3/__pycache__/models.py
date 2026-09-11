# Inheritance
class Animal:
    def __init__(self, name): # type: ignore
        self.name = name

    def study(self):
        print(f"{self.name} is studying...")


class Dog(Animal):
    pass





class Airplane:
    def __init__(self, name, color): # type: ignore
        self.name = name
        self.color = color


    def engine(self):
        print(f"{self.name} is running fast")

    def tire(self):
        print(f"{self.name} has 3 tire")


class Bowing(Airplane): # type: ignore
    def __init__(self, name, color, passenger): # type: ignore
       super().__init__(name, color) # type: ignore
       self.passenger = passenger # type: ignore







class BankAccount:
    def __init__(self, balance): # type: ignore
        self.__balance = balance
    @property
    def amount(self): # type: ignore
        return self.__balance # type: ignore
    @amount.setter
    def amount(self, value): # type: ignore
        if value < 0:
            print("your balance cant be negitive")
        else:
            self.__balance = balance # type: ignore

    def diposite(self, money): # type: ignore
        if money > 0:
            self.__balance += money # type: ignore
            print(f"{self.__balance} is diposite" ) # type: ignore
        else:
            print("balance must be positive")

    def withdraw(self, money): # type: ignore
        if 0 < money  <= self.__balance: # type: ignore
            self.__balance -= money # type: ignore
            print(f"{money} is giving from your account now {self.__balance}") # type: ignore
        else:
            print("balance is not correct")




class Account1(BankAccount):
    def __init__(self, balance, owner): # type: ignore
        super().__init__(balance) # type: ignore
        self. balance = balance
        self.owner = owner

    def __str__(self):
        return f"{self.balance} belong to {self. owner}"

    def withdraw(self, money): # type: ignore
        super().withdraw(money) # type: ignore







