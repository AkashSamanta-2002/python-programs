# def fun1():
#     print("This is function 1\n")

# def fun2():
#     print("This is function 2\n")

# list = [fun1, fun2]

# # list[0]()
# # list[1]()

# print(list)
# print(type(list[0]))

# print(dir(list))

# help(list)


# list1 = [1,2,3]
# list2 = list1

# print(list2)

# list1[0] = 1000         # Hard copy 

# print(list1, list2)

# list1 = [1,2,3]
# list2 = list1.copy()

# print(list2)

# list1[0] = 1000         # shallow copy 

# print(list1, list2)


# list1 = [1,[3,4,5,6],3]
# list2 = list1.copy()

# print(list2)

# list1[1][0] = 1000  # But the inner list is still hard copy   that is actually a reference

# print(list1, list2)

list1 = [1, [3, 4, 5, 6], 3]

list2 = [
    item.copy() if isinstance(item, list) else item
    for item in list1
]

list1[1][0] = 1000

print(list1)
print(list2)

d = {}
print(isinstance(d, dict))

# str = "Akash"     # strings in python is immutable
# str[0] = 'a'
# print(str)

"""
l = [
    {"name": "Akash"},
    {"name": "Aditya"},
]

print(l.index({"name": "Aditya"}))
"""