from abc import ABC, abstractmethod
import math


class Calculator(ABC):
    @abstractmethod
    def add(self, x, y):
        pass

    @abstractmethod
    def subtract(self, x, y):
        pass

    @abstractmethod
    def multiply(self, x, y):
        pass

    @abstractmethod
    def divide(self, x, y):
        pass

    @abstractmethod
    def power(self, x, y):
        pass


class ArithmeticCalculator(Calculator):
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            return "Cannot divide by zero"

    def power(self, x, y):
        return x ** y


class GeometryCalculator(Calculator):
    def add(self, x, y):
        return "Addition is not applicable for geometry calculations"

    def subtract(self, x, y):
        return "Subtraction is not applicable for geometry calculations"

    def multiply(self, x, y):
        return "Multiplication is not applicable for geometry calculations"

    def divide(self, x, y):
        return "Division is not applicable for geometry calculations"

    def power(self, x, y):
        return "Exponentiation is not applicable for geometry calculations"


# Example usage
arithmetic_calc = ArithmeticCalculator()
geometry_calc = GeometryCalculator()

print(arithmetic_calc.add(5, 3))
print(arithmetic_calc.subtract(5, 3))
print(arithmetic_calc.multiply(5, 3))
print(arithmetic_calc.divide(6, 3))
print(arithmetic_calc.power(2, 3))

print(geometry_calc.add(5, 3))
print(geometry_calc.subtract(5, 3))
print(geometry_calc.multiply(5, 3))
print(geometry_calc.divide(6, 3))
print(geometry_calc.power(2, 3))
