# Create a set of data classes to model an online bookstore management system. The classes should include Author,
# Book, Customer, and Order. Your goal is to design a system that enables the management of books, authors, customers,
# and orders in an online bookstore.

from dataclasses import dataclass
from typing import List

@dataclass
class Author:
    author_id: int
    name: str
    birth_year: int

@dataclass
class Book:
    book_id: int
    title: str
    author: Author
    publication_year: int
    price: float
    quantity_in_stock: int

    def sell(self, quantity):
        if quantity <= self.quantity_in_stock:
            self.quantity_in_stock -= quantity
        else:
            print(f"Not enough stock of {self.title} available.")

@dataclass
class Customer:
    customer_id: int
    name: str
    email: str

@dataclass
class Order:
    order_id: int
    customer: Customer
    books: List[Book]
    total_price: float
    status: str

    def __init__(self, order_id, customer, books, status="Pending"):
        self.order_id = order_id
        self.customer = customer
        self.books = books
        self.total_price = self.calculate_total_price()
        self.status = status

    def calculate_total_price(self):
        total_price = sum(book.price for book in self.books)
        return total_price

    def ship_order(self):
        if self.status == "Pending":
            for book in self.books:
                book.sell(1)  # Assuming one book per order for simplicity
            self.status = "Shipped"
            print("Order shipped successfully.")
        else:
            print("Order has already been shipped.")

# Sample usage

# Create authors
author1 = Author(1, "John Doe", 1980)
author2 = Author(2, "Jane Smith", 1975)

# Create books
book1 = Book(1, "Python Programming", author1, 2020, 29.99, 50)
book2 = Book(2, "Data Science Handbook", author2, 2018, 39.99, 30)

# Create a customer
customer1 = Customer(1, "Alice Johnson", "alice@example.com")

# Create an order
order_books = [book1, book2]
order = Order(1, customer1, order_books)

# Display order details
print(f"Order ID: {order.order_id}")
print(f"Customer: {order.customer.name}")
print("Books:")
for book in order.books:
    print(f"- {book.title} by {book.author.name}")
print(f"Total Price: ${order.total_price}")
print(f"Status: {order.status}")

# Ship the order
order.ship_order()

# Display updated stock quantity
print("Updated Stock Quantity:")
for book in order.books:
    print(f"- {book.title}: {book.quantity_in_stock}")
