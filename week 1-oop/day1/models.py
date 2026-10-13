




name = "ola"
print(name)
glass = "plate"
print(glass)
age = 25
print(age)
sum = 1+3
print(type(sum))
age = 33
print(type(age))

a = 6
b = 7
print(a + b )

f = 7
j = 9
print(7 / 9)

class Student: # type: ignore
    def __init__(self):
        print("hello")
s1 = Student()
s2 = Student()


class Student:
    def __init__(self, name, age): # type: ignore
        self.name = name 
        self.age = age
s = Student("Ali", "12")
print(s.age)
s = Student("sara", "23")
print(s.name)





class Dog:
    def __init__(self, name): # pyright: ignore[reportUnknownParameterType, reportMissingParameterType]
        self.name = name 
d1 = Dog("cavin")
d2 = Dog("coco")
print(d1.name)
print(d2.name)













class Housing: # pyright: ignore[reportRedeclaration]
    def __init__(self, name, location, area): # type: ignore
        self.name = name
        self.location = location
        self.area = area





#class
class House2: # type: ignore
    def __init__(self, name, area, location): # type: ignore
        self.name = name
        self.area = area
        self.location = location
    
    # provide basic useful implementations
    def info(self):
        """Print basic information about the house."""
        print(f"House name: {self.name}")
        print(f"Location: {self.location}") # type: ignore
        print(f"Area: {self.area}")

    def relocate(self, new_location): # type: ignore
        """Change the house location."""
        self.location = new_location # type: ignore
        print(f"{self.name} relocated to {self.location}") # type: ignore

    def resize(self, new_area: str): # type: ignore
        """Update the house area."""
        self.area = new_area
        print(f"{self.name} area updated to {self.area}") # type: ignore
    






#classes oop

      



class Car:
    def __init__(self, brand): # type: ignore
        self.brand = brand
        self.speed = 0
    def accelator(self): # type: ignore
        self.speed += 20 # type: ignore
        print("accelator is press")
        print("car speed", self.speed, "km/ h") # type: ignore

    def brake(self):
        self.speed -= 20
        if self.speed < 0:
            self.speed = 0
        print("brak got")
        print("car speed", self.speed, "km/ h")

    def info(self):
        print("brand:", self.brand) # type: ignore
        print("car speed", self.speed, "km/ h")














class House:
    def __init__(self, name, color, book): # type: ignore
        self.name = name 
        self.color = color 
        self.book = book

    def laugh(self):
        message = f"{self.name} is laughing comfortably in the {self.color} house."
        print(message)

    def cry(self):
        message = f"{self.name} is crying and needs a warm hug."
        print(message)

    def info(self):
        print(f"House owner: {self.name}")
        print(f"House color: {self.color}")
        print(f"Favorite book: {self.book}") # type: ignore

    def change_book(self, new_book): # type: ignore
        self.book = new_book # type: ignore
        print(f"{self.name} changed favorite book to {self.book}") # type: ignore

    def __repr__(self):
        return f"House(name={self.name!r}, color={self.color!r}, book={self.book!r})" # type: ignore

    def __str__(self):
        return f"{self.name}'s {self.color} house loves {self.book}" # type: ignore








class MLModel:
    def train(self):
        print("training")

    def evaluate(self):
        print("evaluating")

    def predict(self):
        print("predicting")









import math # type: ignore

class Calculator:
    def add(self, a, b): # type: ignore
        return a+b # type: ignore

    def subtract(self, a, b): # type: ignore
        return a-b # type: ignore

    def multiply(self, a, b): # type: ignore
        return a*b # type: ignore

    def divide(self, a, b): # type: ignore
        return a/b # type: ignore

    def power(self, base, exponant): # type: ignore
        return base**exponant # type: ignore

    def percentage(self, part, total): # type: ignore
        return (part / total) * 100 # type: ignore







#encapsulation with examples:

 #public attribute:
class Teacher:
    def __init__(self, name): # type: ignore
        self.name = name















