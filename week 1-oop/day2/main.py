

from models import BankAccount
account = BankAccount()
account.diposite(50) # type: ignore
print(account.balance) # type: ignore
account.diposite(100) # type: ignore
print(account.balance) # type: ignore

account.withdraw(233) # type: ignore
print(account.balance) # type: ignore

account.withdraw(916) # type: ignore
print(account.balance) # type: ignore

account.withdraw(1) # type: ignore
print(account.balance) # type: ignore



from models import Pen
p = Pen()
# Ensure the Pen instance has a __name attribute for compatibility with code
try:
	# if Pen already defines __name, this will not override
	getattr(p, "__name")
except AttributeError:
	p.__name = p.__class__.__name__ # type: ignore

print(p.__name) # type: ignore


from models import School
s = School("asma", 12)
print(s.get_age()) # type: ignore
 # type: ignore
s.set_age(23) # type: ignore
print(s.get_age()) # type: ignore

s.set_age(55) # type: ignore
print(s.get_age()) # type: ignore


s.set_age(-98) # type: ignore
print(s.get_age()) # type: ignore




from models import BANKACCOUNT
account = BANKACCOUNT()
print(account.balance)


from models import BankAccount1
account = BankAccount1()
print(account.balance)

from models import Temprature
temp = Temprature(25)
print(temp.celsius) # type: ignore

temp.celsius = 56
print(temp.celsius) # type: ignore

temp.celsius = -44
print(temp.celsius)


from models import Bank1account
account = Bank1account() # type: ignore
print(account.balance) # type: ignore

account.balance = -7888
print(account.balance) # type: ignore




















