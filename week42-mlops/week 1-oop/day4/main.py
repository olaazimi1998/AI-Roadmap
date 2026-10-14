from models import Cat, Dog
d = Dog()
c = Cat()
c.speak()
d.speak()


# method overridding
from models import Father, Son
father = Father("Ali")
son = Son("Ahmad")

father.read()
son.read()

#1 example of polymorphism
from employee import Employee, Manager, Developer # type: ignore
employees = [ # type: ignore
    Manager("zaid", 2000), 
    Developer("hasib", 3000)
]

for emp in employees: # type: ignore
    print(emp.name) # type: ignore
    print(emp.calculate_bonus()) # type: ignore


# 2 example
from bank import BankAccount, SavingAccount, CurrentAccount # type: ignore
b = BankAccount("Marwa", 1000)

b.diposit(400) # type: ignore
b.withdraw(20) # type: ignore
b.withdraw(-89) # type: ignore


s = SavingAccount("Mahdia", 2000)
s.diposit(900) # type: ignore
s.diposit(-90) # type: ignore


