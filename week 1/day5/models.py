from abc import ABC, abstractmethod

class Book(ABC):
    @abstractmethod
    def study(self):
        print("Iam study books")


class Math(Book):
    def study(self):
        print("Iam study books")