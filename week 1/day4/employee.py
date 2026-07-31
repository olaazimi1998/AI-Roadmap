
class Employee:
    def __init__(self, name, salary): # type: ignore
        self.name = name
        self.salary = float(salary) # type: ignore


    def calculate_bonus(self): # type: ignore
        return self.salary * 0.10 # type: ignore


class Manager(Employee):
    def calculate_bonus(self): # type: ignore
        return self.salary * 0.25 # type: ignore

class Developer(Employee):
    def calculate_bonus(self): # type: ignore
        return self.salary * 0.15 # type: ignore
        
