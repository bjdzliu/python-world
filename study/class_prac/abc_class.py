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
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length * self.side_length

    def perimeter(self):
        return 4 * self.side_length

# 创建一个抽象类的实例会引发TypeError
# shape = Shape()  # 这行会引发TypeError

# 创建子类的实例
circle = Circle(radius=5)
square = Square(side_length=4)

# 调用抽象类中定义的方法
print("Circle Area:", circle.area())  # 输出: Circle Area: 78.5
print("Circle Perimeter:", circle.perimeter())  # 输出: Circle Perimeter: 31.400000000000002

print("Square Area:", square.area())  # 输出: Square Area: 16
print("Square Perimeter:", square.perimeter())  # 输出: Square Perimeter: 16
