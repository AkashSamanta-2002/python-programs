class Account:
    __amount = 0

    def __init__(self, name):
        self.__name = name

    def deposite(self, amount):
        self.__amount += amount
        print(f"{amount} amount deposited\nCurrent amount is: {self.__amount}")

    def withdraw(self, amount):
        self.__amount -= amount
        print(f"{amount} amount withdrawn\nCurrent amount is: {self.__amount}")

    def check_account(self):
        print(f"\nName: {self.__name}\nAmount: {self.__amount}\n")

savings_account = Account("Akash")

savings_account.deposite(2000)
savings_account.deposite(3000)

savings_account.check_account()

savings_account.withdraw(3000)

savings_account.check_account()

# print(savings_account.__amount)       # Gives error as it is a private attribute
# print(savings_account.__name)       # Gives error as it is a private attribute