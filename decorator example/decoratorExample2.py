# A simple decorator function
def hello(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function.")
    return wrapper


# Applying the decorator to a function
@hello
def print1():
    print("hello")
def greet():
    print("Hello, World!")

print1()