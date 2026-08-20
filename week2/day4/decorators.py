#Function
        #↓
#D ecorator
       # ↓
# Function 
#its too long
def hello(): # type: ignore
    print("hello world")

print("before")
hello()
print("after")


#decorator
def decorator(func): # type: ignore
    def wrapper():
        print("before")
        func()
        print("after")
    return wrapper

def hello(): # type: ignore
    print("hello world")

hello = decorator(hello)
hello()

@decorator
def hello():
    print("hello world")
hello()


print("-----------")

def decorator(func): # type: ignore
    def wrapper(*args, **kwargs): # type: ignore
        print("before")
        result = func(*args, **kwargs) # type: ignore
        print("after")
        return 


    return wrapper # type: ignore
@decorator
def multiply(a, b): # type: ignore
    return a * b # type: ignore
print(multiply(8, 9)) # type: ignore


def decorator(func): # type: ignore
    def wrapper(*args, **kwargs):
        print("before")
        result = func(*args, **kwargs)
        print("after")
        return result
    return wrapper


@decorator
def add(a, b):
    return a + b
print(add(7, 9))


@decorator
def subtract(a, b):
    return a - b
print(subtract(4, 8))


def decorator(func):
    def wrapper(name):

        print("start")

        func(name)

        print("end")

    return wrapper
@decorator
def greet(name):
    print(f"hello {name}")


greet("ola")

import time
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, *kwargs)
        end = time.time()
        print(f"execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def train_model():
    print("training model ...")
    time.sleep(2)
    print("finished") 

train_model()        

@timer
def calculate():
    total = 0
    for i in range(1000000):
        total += i
    return total
print(calculate())


def logger(func):
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


@logger
def login():
    print("user logged in")
login()


logged_in = True
def login_required(func):
    def wrapper():
        if logged_in:
            func()
        else:
            print("access denied")

    return wrapper

@login_required
def dashboard():
    print("dashboard")

dashboard()


from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper



























