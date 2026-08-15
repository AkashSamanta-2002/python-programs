# print all even numbers from 1 to 20

"""
# Normal technique
l = []
for i in range(1, 21):
    if(i%2 == 0):
        l.append(i)

print(l)
"""

"""
# using comprehensions
l = [i for i in range(1, 21) if i % 2 == 0]

print(l)
"""

# dictionary comprehension

d = {key: key ** 2 for key in range (1, 21) if key % 2 ==0}
print(d)