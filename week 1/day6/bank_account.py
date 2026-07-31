class BankAccount:
    def __init__(self, account_number, owner, balance): # type: ignore
        self.account_number = account_number # type: ignore
        self.owner = owner
        self.__balance = balance

    def diposit(self, amount):
        if amount <= 0:
            print("Invalid amount")
            return
        self.__balance += amount
        print(f"{amount}$ diposit successfull, now your account is {self.__balance}")

    def withdraw(self, amount):
        if  amount <= 0 or amount > self.__balance :
            print("not enough balance")
            return
        self.__balance -= amount
        print(f"{amount}$ is successfully withdraw, now your account is {self.__balance}")



    def display(self):
        print("Account:", self.account_number)
        print("Owner:", self.owner)
        print("Balance", self.__balance)

    def get_balance(self):
        return self.__balance # type: ignore