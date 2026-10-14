def repeat(times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(times):
                func(*args, **kwargs)
        return wrapper 
    return decorator


@repeat(3)
def hello(name):
    print(f"hello {name}")

hello("Alice")
        

def log(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"[{level}] running {func.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@log("info")
def train():
    print("training model...")

train()

def require_admin(func):
    def wrapper(is_admin):
        if is_admin:
            return func(is_admin)
        print("access dinied")

    return wrapper

@require_admin
def delete_database(is_admine):
    print("database deleted.")

delete_database(True)
delete_database(False)



def star(func):
    def wrapper():
        print("*" * 20)
        func()

    return wrapper


def dash(func):
    def wrapper():
        print("-" * 20)

        func()

    return wrapper

@star
@dash

def hello():
    print("hello")
    
hello()

print("____________")

import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution Time: {end - start: .2f} seconds")


        return result
    return wrapper


@timer
def train_model():
    print("Training...")

    time.sleep(5)

    print("Finished")

train_model()



import functools
def repeat(num_times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
                return result

        return wrapper
    return decorator
        

import time
import functools
def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"exection time{func.__name__}: {end_time - start_time: .4f} second")
        return result

    return wrapper


    

import functools
def log(level):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{level}] running {func.__name__}")
            return func(*args, **kwargs)

        return wrapper

    return decorator

@repeat(5)
@timer
@log("info")
def train_model():
    print("process finished")
train_model()

























































