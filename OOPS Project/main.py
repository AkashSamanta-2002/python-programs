from pathlib import Path
import json
import random
import string

class Bank:
    database = Path('data.json')
    data = []

    try:
        if database.exists():
            with open(database) as fs:
                data = json.loads(fs.read())
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occured as {err}")

    @staticmethod
    def __update():
        with open(Bank.database, 'w') as fs:
            fs.write(json.dumps(Bank.data)) 

    @staticmethod
    def __accountnumbergenerator():
        alpha = random.choices(string.ascii_lowercase, k = 3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*~", k = 1)

        acc = alpha + num + spchar
        random.shuffle(acc)

        return "".join(acc)

    def create_account(self):
        user = {
            "name": input("\nEnter your name: "),
            "age": int(input("Enter your age: ")),
            "email": input("Enter your email: "),
            "pin": int(input("Enter your 4 digit pin: ")),
            "account number": Bank.__accountnumbergenerator(),
            "balance": 0
        }

        if user["age"] < 18 :
            print("To create an account you must have age greater than 18\n")
        elif len(str(user["pin"])) != 4:
            print("Pin should have been 4 digit\n")
        else:
            for key in user:
                print(f"{key}: {user[key]}")

            Bank.data.append(user)
            Bank.__update()

    def deposite(self):
        acc = input("\nEnter your account number: ")
        pin = int(input("Enter pin: "))

        userData = [user for user in Bank.data if user["account number"] == acc and user["pin"] == pin]
        
        if not userData:
            print("Invalid account number or pin")
            return
        else:
            amount = int(input("Enter amount you want to deposite: "))
            if amount <= 0:
                print("\nPlease enter a valid amount")
            elif amount > 10000:
                print("You can deposite upto 10,000 only")
                return
            else:
                userData[0]["balance"] += amount

            print(f"Amount deposited successfully")
            print(f"Your current balance is: {userData[0]["balance"]}")
            Bank.__update()

    def withdraw(self):
        acc = input("\nEnter your account number: ")
        pin = int(input("Enter pin: "))
    
        userData = [user for user in Bank.data if user["account number"] == acc and user["pin"] == pin]
    
        if not userData:
            print("Invalid account number or pin")
            return
        else:
            print(f"\nAvailable balance: {userData[0]["balance"]}")
            amount = int(input("Enter amount you want to withdraw: "))

            if amount <= 0:
                print("\nPlease enter a valid amount")
            elif(userData[0]["balance"] < amount):
                print("Insufficient balance")
                return
            else:
                userData[0]["balance"] -= amount
    
            print(f"Amount withdrawn successfully\n")
            print(f"Your current balance is: {userData[0]["balance"]}")
            Bank.__update()

    def show_details(self):
        acc = input("\nEnter your account number: ")
        pin = int(input("Enter pin: "))
            
        userData = [user for user in Bank.data if user["account number"] == acc and user["pin"] == pin]
            
        if not userData:
            print("Invalid account number or pin")
            return
        print()
        for key in userData[0]:
            if(key == "pin"):
                continue
            print(f"{key}: {userData[0][key]}")

    def update_details(self):
        acc = input("\nEnter your account number: ")
        pin = int(input("Enter pin: "))
            
        userData = [user for user in Bank.data if user["account number"] == acc and user["pin"] == pin]
            
        if not userData:
            print("Invalid account number or pin")
            return

        print("Fill the details for change or leave it empty")

        updatedData = {
            "name": input("Enter new name to update or press enter to skip: "),
            "email": input("Enter new email to update or press enter to skip: "),
            "pin": input("Enter new pin (4 numbers) to update or press enter to skip: ")
        }

        if updatedData["pin"] != "" and len(updatedData["pin"]) != 4:
            print("Pin should have been 4 digit\n")
            return

        if(updatedData["name"] == ""):
            updatedData["name"] = userData[0]["name"]
        if(updatedData["email"] == ""):
            updatedData["email"] = userData[0]["email"]
        if(updatedData["pin"] == ""):
            updatedData["pin"] = userData[0]["pin"]

        updatedData["age"] = userData[0]["age"]
        updatedData["account number"] = userData[0]["account number"]
        updatedData["balance"] = userData[0]["balance"]

        if type(updatedData["pin"] == int):
            updatedData["pin"] = int(updatedData["pin"])

        for item in updatedData:
            if updatedData[item] == userData[0][item]:
                continue
            else:
                userData[0][item] = updatedData[item]

        Bank.__update()
        print("Account updated successfully")

    def delete_account(self):
        acc = input("\nEnter your account number: ")
        pin = int(input("Enter pin: "))
            
        userData = [user for user in Bank.data if user["account number"] == acc and user["pin"] == pin]
            
        if not userData:
            print("Invalid account number or pin")
            return

        check = input("Are you sure? (Y/N): ")
        if check == "n" or check == "N":
            return
        else:
            index = Bank.data.index(userData[0])
            Bank.data.pop(index)
            Bank.__update()

            print("Account deleted successfully")



user = Bank()

print("press 1 for creating an account")
print("press 2 for deposite")
print("press 3 for withdraw")
print("press 4 for details")
print("press 5 for update the account")
print("press 6 for delete the account")

res = int(input("Enter your response:- "))

if res == 1:
    user.create_account()
if res == 2:
    user.deposite()
if res == 3:
    user.withdraw()
if res == 4:
    user.show_details()
if res == 5:
    user.update_details()
if res == 6:
    user.delete_account()