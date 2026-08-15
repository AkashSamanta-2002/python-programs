# class Animal:
#     name = "Animal class"
#     def sound(self):
#         print("This is animal sound")

# class Lion(Animal):
#     name = "Lion class"
#     def lionSound(self):
#             print("This is Lion sound")

# lion = Lion()

# lion.sound()


# class Vehicle:
#     def __init__(self, name, brand):
#         self.name = name
#         self.brand = brand

#     def showVehicleDetails(self):
#         print(f"name: {self.name}\nbrand: {self.brand}")

# class Electric_vehicle(Vehicle):
#     def __init__(self, name, brand, battery):
#         super().__init__(name, brand)
#         self.battery = battery

#     def showElectricVehicleDetails(self):
#         super().showVehicleDetails()
#         print(f"battery: {self.battery}")


# ev = Electric_vehicle("xuv700", "Mahindra", 800)
# ev.showElectricVehicleDetails()
# ev.showVehicleDetails()


# class Vehicle:
#     name1 = "vehicle class"
#     def __init__(self, brand):
#         self.brand = brand

# class Four_Wheeler:
#     name = "Four wheeler class"
#     def __init__(self, hasAlloy):
#         self.hasAlloy = hasAlloy

# class EV(Four_Wheeler, Vehicle):
#     def __init__(self, hasAlloy):
#         super().__init__(hasAlloy)          # this targets the constructor of the class which we pass at the first only

# ev = EV()

# print(ev.name)      # heirarchy => EV -> Four_Wheeler -> Vehicle (How the classes we pass) -> object    (MRO: Method Resolution Order)

