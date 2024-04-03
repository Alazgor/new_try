# Task Nr.1:
# Create a class called Product that takes a name and price as parameters and has __str__ and __repr__ methods defined.
# The __str__ method should return a string in the format "Product: name, Price: price"
# The __repr__ method should return a string in the format "Product('name', price)"

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name}, Price: {self.price}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price})"

product1 = Product("Laptop", 540.99)
print(str(product1))
print(repr(product1))