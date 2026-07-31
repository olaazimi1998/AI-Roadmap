#Encapsulation is one of the four fundamental principles of Object-Oriented Programming.

#It means:


#Keeping an object's data and the methods that work on that data together while controlling how the data can be accessed or modified.



class BankAccount:
    def __init__(self):
        self.balance = 1000

    def diposite(self, amount): # type: ignore
        self.balance += amount # type: ignore
        print(f"{amount} money is settlement")
        print(f"now your account is {self.balance}") # type: ignore
    def withdraw(self, amount): # type: ignore
        if amount <= self.balance: # type: ignore
            self.balance -= amount # type: ignore # type: ignore
            print(f"{amount} money is giving from your acount")
            print(f"now your acount is {self.balance}") #type: ignore


class Pen:
    def __init__(self):
        self.__name = "Ali"


# 1- private
# 2- Getter
# 3- setter
class School:
    def __init__(self, name, age): # type: ignore
        self.__name = name
        self.__age = age # type: ignore

    def get_age(self): # type: ignore
        return self.__age # type: ignore
    
    def set_age(self, age): # type: ignore
        if age > 0:
            self.__age = age # type: ignore

        else:
            print("Age can not be negetive.")



#  property
class BANKACCOUNT:
    def __init__(self):
        self.__balance = 1000
    @property
    def balance(self):
        return self.__balance





# property
class BankAccount1:
    def __init__(self):
        self.__balance = 10000

    @property
    def balance(self):
        return self.__balance


    @balance.setter
    def balance(self, amount): # type: ignore

        if amount > 0:
            return self.__balance

        else:
            print("balance canot be negitave")




class Temprature:
    def __init__(self, celsius): # type: ignore
        self.__celsius = celsius

    @property
    def celsius(self): # type: ignore
        return self.__celsius # type: ignore

    @celsius.setter # type: ignore
    def celsius(self, amount): # type: ignore
        if amount > 0:
            self.__celsius = amount # type: ignore
        else:
            print("Invalide Temrature")


"""print(account.balance)
        │
        ▼
@property
def balance(self):
    return self.__balance
        │
        ▼
Returns the value"""


"""

account.balance = 2000
        │
        ▼
@balance.setter
def balance(self, value):
    self.__balance = value
        │
        ▼
Updates the value"""




#example
class Bank1account:
    def __init__(self): # type: ignore
        self.__balance = 7000

    @property
    def balance(self): # type: ignore
        return self.__balance  # type: ignore
    @balance.setter
    def balance(self, amount): # type: ignore
        if amount > 1000: # type: ignore
            self.__balance = amount # type: ignore
        else:
            print("balance cant ne negitive")

               








































