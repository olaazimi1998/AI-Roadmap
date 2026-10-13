           
from bank_account import BankAccount


account = BankAccount(50000, "sara", 80000)
print(account.owner)
print(account.account_number)


account.diposit(200)
account.diposit(-300)
account.diposit(200)


account.withdraw(700)
account.withdraw(600)
account.withdraw(-200)


account.display()

account.get_balance()

account.display()


from saving_account import Savingaccount

saving = Savingaccount(3,"david", 2000, 5 )
print(saving.get_balance())
saving.add_interest()





from costumer import Costumer # type: ignore

ahmed = Costumer("Ahmed")
sara = Costumer("sara")

account1 = BankAccount(1, "ali", 400)

account2 = BankAccount(3, "sara", 600)






from bank import Bank
bank = Bank()

bank.add_costumer(ahmed)
bank.add_costumer(sara)

ahmed.add_account(account1)
sara.add_account(account2)

print()
ahmed.show_accounts()

print()
sara.show_accounts()