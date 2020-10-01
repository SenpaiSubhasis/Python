from abc import ABC   #this how we archive abstraction in Python

class Shape(ABC):
    #This class Shape becomes an abstract class
    def calculate(self):
        pass

class Rectangle(Shape):
    length = 2
    breadth = 3

    def calculate(self):
        return self.length * self.breadth

class Circle(Shape):
    radius = 4

    def calculate(self):
        return (3.14*self.radius*self.radius)

rec1= Rectangle()
print(rec1.calculate())

cir1 = Circle()
print(cir1.calculate())

