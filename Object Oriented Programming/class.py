class Car:
    name = "Scorpio N"
    brand = "Mahindra"

    def start(self):
        print("Car started")

    print("Class Initialized")

print(Car.name)     # directly called by class name as class level attribute
print(Car().name)   # make an object then called

Car().start()   # here python automatically pass self it converted to car = Car()  Car.start(car)
Car.start()     # but here no object is passed for self