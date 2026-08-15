# Abstraction doesn't exist in python but we can achieve that using libraries

from abc import ABC, abstractmethod

class Abstarct(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Abstarct):
    PI = 3.14
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius ** 2

    def perimeter(self):
        return 2 * self.PI * self.radius 

class Square(Abstarct):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

circle = Circle(3)
print(f"Circle area: {circle.area()}\nCircle perimeter: {circle.perimeter()}")

sq = Square(3)
print(f"Square area: {sq.area()}\nSquare perimeter: {sq.perimeter()}")