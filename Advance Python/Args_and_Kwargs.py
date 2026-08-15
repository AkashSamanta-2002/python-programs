"""
def greet():
    print("Hello")

def fun(*args, **kwargs):       # in args it becomes tuple, kwargs becomes dictionary
    print(f"Args: {args}")
    print(f"kwargs: {kwargs}")

fun(1,2,3,4,"Akash Samanta", 
    [1, 2, 3], greet, a=10, b=20)
"""
"""
# args captured positional arguments 
def add(*args):
    sum = 0
    for item in args:
        sum += item

    return sum

print(add(10, 20))
print(add(10, 20, 50, 39, 834, 345))
"""
"""
#kwargs captures keyword arguments
def fun(**kwargs):
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")


fun(a = 10, b = True, c = "Akash")
"""

def fun(**user):
    for key in user:
        print(f"{key}: {user[key]}")

fun(name = "Akash", age = 24, address = {"vill": "Mankur", "Post": "Mankur", "District": "Howrah", "State": "West Bengal", "Pin Code": 711303})