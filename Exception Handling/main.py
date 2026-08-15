num = int(input("Enter a number: "))

try:
    print(10/num)
except ZeroDivisionError:
    print("Divide by 0 is not allowed")
else: 
    print("There is no exception")
finally:
    print("Finally block")

print("End of the code")


# try:
#     print(10/num)
# except Exception as err:
#     print(f"Sorry there is an error: {err}")
#     # print("Divide by 0 is not allowed")
# finally:
#     print("End of the excerption")

# print("End of the code")