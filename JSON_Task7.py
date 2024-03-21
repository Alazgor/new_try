import json

# Define the JSON string
json_str = '{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }'

# Parse the JSON string into a Python dictionary
vehicle_data = json.loads(json_str)

# Define the Vehicle class
class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

# Create an instance of the Vehicle class using data from the dictionary
vehicle_obj = Vehicle(name=vehicle_data['name'], engine=vehicle_data['engine'], price=vehicle_data['price'])

# Access attributes of the Vehicle object using dot operator
print(vehicle_obj.name)
print(vehicle_obj.engine)
print(vehicle_obj.price)