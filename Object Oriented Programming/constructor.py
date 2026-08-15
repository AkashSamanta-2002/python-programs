class Car:
    def __init__(self, name, brand):    # self is nothing but this in python
        self.name = name           # Instance attribute
        self.brand = brand

    def getInfo(self):      # Instance method
        print(f"Car name: {self.name}\nCar brand: {self.brand}")

    def start(self):
        print("Car started")


# car = Car("Scorpio", "Mahindra")
# print(car.name, car.brand)

car1 = Car("Thar", "Mahindra")


car1.start()
car1.getInfo()