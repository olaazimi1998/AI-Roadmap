#BANKACCOUNT

class Bankaccount:
    def __init__(self, owner, balance = 0):
        self.owner = owner
        bank_name = "Ai Bank"
        self.balance = balance
    @classmethod
    def change_name(cls, new_name):
        cls.bank_name = new_name



    @classmethod
    def new_balance(cls, owner):
        return cls(owner, 1000)

    @classmethod
    def is_valid_withdrawal(cls, amount):
        return amount > 0

    def diposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} is diposit")

        else:
            print("your amount is unsufficient")

    def withdraw(self, amount):
        if Bankaccount.is_valid_withdrawal(amount):
            if amount <= self.balance:
                self.balance -= amount
                print(f"{amount} is withdraw from your account")
            else:
                print("The withdraw is invalid.")
my_account = Bankaccount.new_balance(1000)
print(my_account.balance)
Bankaccount.change_name("sara bank")
print(Bankaccount.bank_name)
my_account.withdraw(200)

my_account.diposit(300)










