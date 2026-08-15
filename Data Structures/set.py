# s1 = {1,2,3,4,5}

# # s1[0] # Not allowed

# def greet():
#     print("Hello")

# s2 = {1,"Hello", (1,2,3), greet}   # Only this are allowed
# s3 = {1,"Hello", (1,2,3), greet()}   # Only this are allowed

# for ele in s3:
#     print(ele)

a = {1,2,3,4,5}
b = {3,4,5,6,7}

# print(a.union(b))
print(a | b)    # same

# print(a.intersection(b))
print(a & b)    # same

# print(a.difference(b))
print(a - b)  # same

# print(a.symmetric_difference(b))      # only remove the common portions
print(a ^ b)
print(b ^ a)


b -= a      # also valid
print(b)