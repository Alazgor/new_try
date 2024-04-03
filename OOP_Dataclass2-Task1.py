from dataclasses import dataclass

@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float
    quantity_in_stock: int

    def calculate_total_cost(self, num_items: int, discount: float = 0.0) -> float:
        """
        Calculate the total cost of purchasing a given number of items of the product,
        taking into account any discounts that may apply.

        Args:
            num_items (int): The number of items to calculate the total cost for.
            discount (float, optional): The discount rate as a percentage. Defaults to 0.0 (no discount).

        Returns:
            float: The total cost of purchasing the specified number of items.
        """
        if num_items <= 0:
            return 0.0

        if discount < 0 or discount > 100:
            raise ValueError("Discount must be between 0 and 100.")

        # Calculate the total cost without discount
        total_cost = self.price * num_items

        # Apply discount if applicable
        total_cost -= total_cost * (discount / 100)

        return total_cost

# Example usage:
if __name__ == "__main__":
    # Create a product instance
    product1 = Product(1, "Phone", "Smartphone", 500.0, 10)

    # Calculate total cost for purchasing 5 items with no discount
    total_cost_no_discount = product1.calculate_total_cost(5)
    print("Total cost without discount:", total_cost_no_discount)

    # Calculate total cost for purchasing 3 items with a 10% discount
    total_cost_with_discount = product1.calculate_total_cost(3, discount=10)
    print("Total cost with discount:", total_cost_with_discount)
