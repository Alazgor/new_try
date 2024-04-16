from pymongo import MongoClient
from datetime import datetime, timedelta

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['grocery_store']
collection = db['items']

# Sample data insertion
sample_data = [
    {"name": "Laptop", "category": "Electronics", "price": 1000, "quantity": 5, "year_made": "2022-01-01"},
    {"name": "Smartphone", "category": "Electronics", "price": 800, "quantity": 10, "year_made": "2022-02-15"},
    {"name": "Apple", "category": "Fruits", "price": 2, "quantity": 100, "year_made": "2023-03-10"},
    {"name": "Banana", "category": "Fruits", "price": 1, "quantity": 200, "year_made": "2023-04-05"},
    {"name": "Bread", "category": "Food", "price": 3, "quantity": 50, "year_made": "2023-05-20"}
]

# Insert sample data and print details of added items
print("Details of added items:")
for item in sample_data:
    inserted_id = collection.insert_one(item).inserted_id
    added_item = collection.find_one({"_id": inserted_id})
    print(added_item)

# Task 1: Get all electronic items monetary value made 1 year, 2 months, and 12 days from today
query_date = datetime.now() - timedelta(days=(365 + 30*2 + 12))
electronic_items = collection.find({"category": "Electronics", "year_made": {"$gte": query_date}})
total_value = sum(item["price"] * item["quantity"] for item in electronic_items)
print("\nTotal monetary value of electronic items made 1 year, 2 months, and 12 days ago:", total_value)

# Task 2: Get average price for all items/categories in the store
average_price = collection.aggregate([{"$group": {"_id": "$category", "average_price": {"$avg": "$price"}}}])
print("\nAverage prices for each category:")
for category in average_price:
    print("Category:", category["_id"], "- Average Price:", category["average_price"])

# Task 3: Get all items which names start with letter 'a' and cost is between 10 and 100
items_a = collection.find({"name": {"$regex": "^A", "$options": "i"}, "price": {"$gte": 10, "$lte": 100}})
print("\nItems whose names start with 'A' and cost is between 10 and 100:")
for item in items_a:
    print("Item:", item["name"], "- Price:", item["price"])

# Task 4: Find all item names (only) for prices > 50 and quantity < 10
item_names = collection.find({"price": {"$gt": 50}, "quantity": {"$lt": 10}})
print("\nItem names for prices > 50 and quantity < 10:")
for item in item_names:
    print("Item name:", item["name"])
# Updating task 3 from previews lesson:
# Calculate the average price per unit for those retrieved
low_quantity_low_price_items = collection.find({"quantity": {"$lte": 10}, "price": {"$lte": 20.00}})
print("\nItems where quantity is less or equal to 10 and price is equal or less than 20.00:")
average_price_per_unit = 0
total_items = 0
for item in low_quantity_low_price_items:
    total_items += 1
    print("Item:", item["name"], "- Year Made:", item["year_made"])
    average_price_per_unit += item["price"] / item["quantity"] if item["quantity"] != 0 else 0

if total_items != 0:
    average_price_per_unit /= total_items
    print("Average Price Per Unit:", average_price_per_unit)

# Get all items where quantity is 5, 10, and 15 respectively
quantities_to_find = [5, 10, 15]
print("\nItems where quantity is 5, 10, and 15 respectively:")
for quantity in quantities_to_find:
    items_with_quantity = collection.find({"quantity": quantity})
    print(f"\nItems with quantity {quantity}:")
    for item in items_with_quantity:
        print("Item:", item["name"], "- Year Made:", item["year_made"])