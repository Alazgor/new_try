class Shape:
    def __init__(self, name, sides):
        self.name = name
        self.sides = sides

    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name, 4)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, name, side_length):
        super().__init__(name, side_length, side_length)
        self.side_length = side_length


# Example usage:
rectangle = Rectangle("Rectangle", 4, 6)
print(rectangle.name)
print(rectangle.sides)
print(rectangle.area())  # Output will be 24

square = Square("Square", 5)
print(square.name)
print(square.sides)
print(square.area())  # Output will be 25
