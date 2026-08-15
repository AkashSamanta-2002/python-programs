"""
class Animal:
    @property
    def sound(self):
        print("Animal sound")

animal = Animal()
# animal.sound()    # This will not run as now sound is a property not a method
animal.sound
"""

#  create decorator
"""
# We have to create a wrapper function
def my_decorator(fun):      # The parameter fun is the function which is used after the decorator it will pass automatically
    def wrapper():
        print("Start of the wrapper function")
        fun()
        print("End of the wrapper function")

    return wrapper

@my_decorator
def greet():
    print("Hello, Good Morning")

greet()
"""
"""
def decorate(fun):
    def wrapper(a, b):      # the given parameters are accepted by the wrapper function
        fun(a, b)
        print("Thank you")

    return wrapper

@decorate
def add(a, b):
    print(f"The addition of {a} and {b} is {a + b}")

add(10, 2)
"""

# for multiple arguments

def my_decorator(fun):
    def wrapper(*args, **kwargs):
        print("Start wrapper")
        fun(*args, **kwargs)
        print("End wrapper")

    return wrapper

@my_decorator
def fun(a, b, c, d):
    print(f"A: {a}\nB: {b}\nC: {c}\nD: {d}")

fun(2,3,4,5)
fun(d=2,b=3,a=1,c=2)