# You have been asked to create a simple inventory management system for a small retail store. You need to define a
# Product class using the dataclass module that represents a product in the store. Each Product should have a unique ID,
# a name, a description, a price, and a quantity in  stock. You also need to implement a method calculate_total_cost that
# calculates the total cost of a given number of items of the product, taking into account any discounts that may apply.

from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def calculate_total_cost(self, num_items, discount_percentage=0):
        total_cost = self.price * num_items
        if discount_percentage > 0:
            total_cost -= (total_cost * discount_percentage / 100)
        return total_cost

# Example usage:
product1 = Product(1, "Laptop", "High-performance laptop", 999.99, 10)
print(product1)

num_items = 3
discount_percentage = 10  # Example discount percentage
total_cost = product1.calculate_total_cost(num_items, discount_percentage)
print(f"Total cost for {num_items} items with {discount_percentage}% discount: ${total_cost}")


