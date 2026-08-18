"""
n = int(input("Enter a number: "))
fact = 1

for i in range (1, n+1):
    fact *= i

print(fact)
"""
row_sum = [45,45,45,45,45]

for i in row_sum:
    if i != 45:
        print("Not a vlid sodoku")
        break

else:
    print("Valid for rows")