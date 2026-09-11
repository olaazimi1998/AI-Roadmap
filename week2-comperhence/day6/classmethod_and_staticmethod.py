# instance method
from os import name


class Names:

    def __init__(self, name):
    
        self.name = name # type: ignore

    def show_name(self):
        print(self.name)

n = Names("ola")
n.show_name()


# classmethode
class Student:
    school = "AI acadimy"

    @classmethod
    def show_school(cls):
        print(cls.school)

Student.show_school()

class Student:
    school = "ABC school"
    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

Student.change_school("python acacemy")
print(Student.school)

class Mlmodel:
    def __init__(self, model_name):
        self.model_name = model_name

    @classmethod
    def load_model(cls, filename):
        print(f"loading {filename} ...")
        return cls("resnet50")

model = Mlmodel.load_model("model.pkl")
print(model.model_name)






