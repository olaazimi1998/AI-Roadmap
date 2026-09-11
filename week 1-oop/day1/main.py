
from models import Calculator
calculate = Calculator()
print(calculate.subtract(8, 9)) # type: ignore
print(calculate.power(4, 6)) # type: ignore
print(calculate.percentage(2, 2)) # type: ignore

from models import MLModel
model = MLModel()
model.evaluate()
model.predict()
model.train()

from models import House

n1 = House("Motahara", "Red", "Math") # type: ignore
n2 = House("Mahdia", "Blue", "English") # type: ignore

n1.info()
n1.cry()
n1.laugh()
n2.cry()
n2.laugh()
print(n1)
print(repr(n1))

from models import Car
car1 = Car("Toyota")

car1.info()
car1.accelator()
car1.accelator()
car1.brake()


from models import House2
h1 = House2("1", "125", "diera")
h2 = House2("2", "150", "sharja")
print(h1.area) # type: ignore
print(h2.location) # type: ignore


from models import Housing
h1 = Housing("do", "23", "she") 
h2 = Housing("hi", "55", "hello") 
print(h1.name) 
print(h2.area) # type: ignore

from models import Teacher
teacher = Teacher("Sara")
print(teacher.name) # type: ignore
