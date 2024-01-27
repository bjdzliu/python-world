from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
    def area(self):
        return 3.14 *self.radius * self.radius

circle= Circle(radius=5)
print(circle.area())

