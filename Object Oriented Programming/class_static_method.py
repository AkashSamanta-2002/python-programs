class Animal:
    name = "Lion"

    def __init__(self, max_age):
        self.max_age = max_age

    @classmethod    # decorator     
    def getClassAttribute(cls):     # targets class
        print(cls.name)

    @staticmethod
    def staticMethod():
        print("This is a static method")


Animal.getClassAttribute()
Animal.staticMethod()