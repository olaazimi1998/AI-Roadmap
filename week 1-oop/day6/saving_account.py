from bank_account import BankAccount 
class Savingaccount(BankAccount):
    def __init__(self, account_number, owner, balance, interest):
        super().__init__(account_number, owner, balance)
        self.interest = interest

    def add_interest(self):
        interest_money = self.get_balance() * self.interest
        self.diposit(interest_money)

        
        