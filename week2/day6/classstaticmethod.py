#staticmethod
class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
print(Calculator.add(10, 40))


class User:
    @staticmethod
    def is_valid_email(email):
        return "a" in email


print(User.is_valid_email("ali@gmail.com"))


class Temprature:
    @staticmethod
    def celcius_to_fahrenheit(c):
        return(c * 9 / 5) + 32

print(Temprature.celcius_to_fahrenheit(30))

class Example:
    class_variable = 100
    def __init__(self, value):
        self.value = value

    def instance_method(self):
        print(self.value)


    @classmethod
    def class_method(cls):
        print(cls.class_variable)


    @staticmethod
    def static_method():
        print("hello")


obj = Example(20)

obj.instance_method()


Example.class_method()

Example.static_method()


class Car:
    company = "toyota"

    @classmethod
    def change_name(cls, new_name):
        cls.company = new_name

Car.change_name("corola")
print(Car.company)


















