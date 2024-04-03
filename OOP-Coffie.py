class CoffeeShop:
    def __init__(self, name, menu):
        self.name = name
        self.menu = menu
        self.orders = []

    def add_order(self, item):
        for menu_item in self.menu:
            if menu_item['item'] == item:
                self.orders.append(item)
                return "Order added!"
        return "This item is currently unavailable!"

    def fulfill_order(self):
        if self.orders:
            item = self.orders.pop(0)
            return f"The {item} is ready!"
        else:
            return "All orders have been fulfilled!"

    def list_orders(self):
        return self.orders

    def due_amount(self):
        total_amount = sum(menu_item['price'] for menu_item in self.menu if menu_item['item'] in self.orders)
        return round(total_amount, 2)

    def cheapest_item(self):
        if not self.menu:
            return "No items on the menu."
        cheapest = min(self.menu, key=lambda x: x['price'])
        return cheapest['item']

    def drinks_only(self):
        return [menu_item['item'] for menu_item in self.menu if menu_item['type'] == 'drink']

    def food_only(self):
        return [menu_item['item'] for menu_item in self.menu if menu_item['type'] == 'food']

# Example usage
menu_items = [
    {'item': 'orange juice', 'type': 'drink', 'price': 1.5},
    {'item': 'lemonade', 'type': 'drink', 'price': 1.75},
    {'item': 'cranberry juice', 'type': 'drink', 'price': 2.0},
    {'item': 'pineapple juice', 'type': 'drink', 'price': 2.25},
    {'item': 'lemon iced tea', 'type': 'drink', 'price': 2.5},
    {'item': 'vanilla chai latte', 'type': 'drink', 'price': 3.0},
    {'item': 'hot chocolate', 'type': 'drink', 'price': 2.75},
    {'item': 'iced coffee', 'type': 'drink', 'price': 2.0},
    {'item': 'tuna sandwich', 'type': 'food', 'price': 5.5},
    {'item': 'ham and cheese sandwich', 'type': 'food', 'price': 6.0},
    {'item': 'bacon and egg', 'type': 'food', 'price': 4.5},
    {'item': 'steak', 'type': 'food', 'price': 8.0},
    {'item': 'hamburger', 'type': 'food', 'price': 6.5},
    {'item': 'cinnamon roll', 'type': 'food', 'price': 3.25}
]

tcs = CoffeeShop("Tesha's Coffee Shop", menu_items)

print(tcs.add_order("hot cocoa"))  # This item is currently unavailable!
print(tcs.add_order("iced tea"))   # This item is currently unavailable!
print(tcs.add_order("cinnamon roll"))  # Order added!
print(tcs.add_order("iced coffee"))  # Order added!
print(tcs.list_orders())  # ['cinnamon roll', 'iced coffee']
print(tcs.due_amount())  # 2.17
print(tcs.fulfill_order())  # The cinnamon roll is ready!
print(tcs.fulfill_order())  # The iced coffee is ready!
print(tcs.fulfill_order())  # All orders have been fulfilled!
print(tcs.list_orders())  # []
print(tcs.due_amount())  # 0.0
print(tcs.cheapest_item())  # lemonade
print(tcs.drinks_only())
print(tcs.food_only())
