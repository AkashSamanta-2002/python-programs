"""
# normal function
def add(a, b):
    return a + b

print(add(2, 3))
"""

"""
# lambda function
add = lambda a, b : a + b

print(add(2, 3))
"""

num = int(input("Ennter a number: "))
# check_even_odd = lambda a : print("Even") if a % 2 == 0 else print("Odd")
# check_even_odd(num)

check_even_odd = lambda a : "Even" if a % 2 == 0 else "Odd"
print(f"The number is {check_even_odd(num)}")
