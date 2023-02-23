class Shape():
    def __init__(self, type):
        self.type = type
    def what_am_i(self):
        print("I am a shape")
        



class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def perimeter(self):
        perimeter = 2 * self.length + 2 * self.width
        return perimeter

class Square(Shape):
    Squares = []
    def __init__(self, side):
        self.Squares.append(side)
        self.side = side
        
    def perimeter(self):
        perimeter = self.side * 4
        return perimeter
    
    def changeSide(self, change):
        self.side += change

    def __repr__(self):
        string = str(self.side)
        for i in range(0,3):
            string += " by " + str(self.side)
        return string
    def same(self, other):
        if self is other:
            return True
        else:
            return False
        
    
s1 = Square(4)
s3 = Square(1038189)
s2 = s1
s1.changeSide(2)

r1 = Rectangle(2,4)
print(r1.perimeter())
print(r1.what_am_i())

class Rider():
    def __init__(self, name):
        self.name = name
    
        

class Horse():
    def __init__(self, breed, rider):
        self.breed = breed
        self.rider = rider
 
mark = Rider("Mark")
h1 = Horse("Pony", mark)
print(h1.rider.name)

print(s1)
print(s2.same(s1))
print(s1.same(s3))