from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def display_info(self):
        pass

    def get_name(self):
        return self.__class__.__name__

    def set_color(self, color):
        self.color = color


class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def calculate_area(self):
        return self.length * self.width

    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

    def display_info(self):
        print(f"Shape: {self.get_name()}, Color: {self.color}, Length: {self.length}, Width: {self.width}")


class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius ** 2

    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def display_info(self):
        print(f"Shape: {self.get_name()}, Color: {self.color}, Radius: {self.radius}")


# Example usage
rectangle = Rectangle("Red", 5, 3)
circle = Circle("Blue", 4)

rectangle.display_info()
print("Area:", rectangle.calculate_area())
print("Perimeter:", rectangle.calculate_perimeter())

circle.display_info()
print("Area:", circle.calculate_area())
print("Perimeter:", circle.calculate_perimeter())
