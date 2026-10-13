class BankAccount:
    def __init__(self, owner, balance):  # type: ignore
        self.owner = owner
        self.balance = balance

    def diposit(self, amount): # type: ignore
        if amount > 0:
            self.balance += amount # type: ignore
            print(f"{amount} $ is send to your account now your account is {self.balance}") # type: ignore

        else:
            print("your balance cant be nigitive")


    def withdraw(self, amount): # type: ignore
        if amount <= self.balance:            # type: ignore
            self.balance -= amount # type: ignore

            print(f"{amount} $ is withdraw from your account now your account is {self.balance}") # type: ignore

        else:
            print("insufficient balance")



class SavingAccount(BankAccount):
    def withdraw(self, amount): # type: ignore
        if amount > 1000:
            print("Daily limit exceeded.")

        else:
            super().withdraw(amount) # type: ignore


    def diposit(self, amount): # type: ignore
        super().diposit(amount) # type: ignore

class CurrentAccount(BankAccount):
    def withdraw(self, amount): # type: ignore
        print("current account progressing")
        super().withdraw(amount) # type: ignore


    def diposit(self, amount): # type: ignore
        super().diposit(amount) # type: ignore