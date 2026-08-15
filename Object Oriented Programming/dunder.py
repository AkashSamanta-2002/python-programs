class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Hii {self.name}"

    def __add__(self, other):
        return self.age + other.age

akash = Human("akash", 24)
print(akash)

aditya = Human("aditya", 17)
print(aditya)

print(f"The sum of age is: {akash + aditya}")