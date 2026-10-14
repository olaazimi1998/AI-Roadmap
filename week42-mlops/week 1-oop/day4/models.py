# polymorphism
class Dog:
    def speak(self):
        print("woof woof")

class Cat:
    def speak(self):
        print("meo meo")


class Father:
    def __init__(self, name): # type: ignore
        self.name = name
    def read(self):
        print(f"{self.name} raeding book.")


class Son(Father):
    def __init__(self, name): # type: ignore
        super().__init__(name) # type: ignore
    
    def read(self):
        super().read()
        print(f"{self.name} like reading books.")

    