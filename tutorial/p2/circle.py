import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
        print("created")
    def area(self):
        area = math.pi * self.radius ** 2
        return area

c1 = Circle(4)
print(c1.area())

class Hexagon:
    def __init__(self, side):
        self.side = side
        print("created")
    def perimeter(self):
        perimeter = self.side * 6
        return perimeter
    
h1 = Hexagon(6)
print(h1.perimeter())