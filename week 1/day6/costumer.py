from os import name


class Costumer:
    def __init__(self, name):
        self.name = name

        self.accounts = []


    def add_account(self, account):
        self.accounts.append(account)

    def show_accounts(self):
        for account in self.accounts:
            account.display()