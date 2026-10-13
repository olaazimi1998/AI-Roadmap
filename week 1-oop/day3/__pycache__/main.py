from models import Animal 
a = Animal("cat")
a.study()


from models import Dog
d = Dog("labobo")
d.study()



from models import Airplane
a = Airplane("first", "blue")
a.engine()


from models import Bowing
b = Bowing("second", "red", 8 ) # type: ignore
print(b.passenger) # type: ignore
b.engine()
print(b.name) # type: ignore
print(b.color) # type: ignore






from models import BankAccount, Account1
a = BankAccount(1000)
print(a.amount) # type: ignore

a.withdraw(200) # type: ignore
a.withdraw(78) # type: ignore
a.diposite(400) # type: ignore

o = Account1(6000, "ali")
o.withdraw(1000) # type: ignore









