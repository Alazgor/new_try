# "The provided code defines classes for Book, User, and LibrarySystem. Book and User classes represent
# individual books and library users, respectively. The LibrarySystem class manages the library's functionality,
# including adding books, registering users, borrowing and returning books, and listing available books and users.
#  Books and users are added to the library system, and users can borrow and return books.
#  The system keeps track of the availability of books and maintains a record of which books each user has borrowed.
#  Users can be listed along with the books they've borrowed, and available books can also be listed.
#  Overall, the code sets up a basic library system where users can interact with the library's collection of books."

from typing import List


class Book:
    def __init__(self, title: str, author: str, isbn: str, num_copies: int) -> None:
        self.title = title
        self.author = author
        self.isbn = isbn
        self.num_copies = num_copies


class User:
    def __init__(self, name: str, email: str) -> None:
        self.name = name
        self.email = email
        self.books_borrowed: List[Book] = []


class LibrarySystem:
    books: List[Book] = []
    users: List[User] = []

    @classmethod
    def add_book(cls, book: Book) -> None:
        cls.books.append(book)

    @classmethod
    def register_user(cls, user: User) -> None:
        cls.users.append(user)

    @classmethod
    def borrow_book(cls, user: User, isbn: str) -> None:
        for book in cls.books:
            if book.isbn == isbn:
                if book.num_copies > 0:
                    book.num_copies -= 1
                    user.books_borrowed.append(book)
                    print(f"{user.name} has borrowed '{book.title}'.")
                    return
                else:
                    print("Sorry, no copies of this book are available.")
                    return
        print("Sorry, the book with the given ISBN is not available in the library system.")

    @classmethod
    def return_book(cls, user: User, isbn: str) -> None:
        for book in user.books_borrowed:
            if book.isbn == isbn:
                book.num_copies += 1
                user.books_borrowed.remove(book)
                print(f"{user.name} has returned '{book.title}'.")
                return
        print("Sorry, the user has not borrowed the book with the given ISBN.")

    @classmethod
    def list_books(cls) -> List[Book]:
        return cls.books

    @classmethod
    def list_users(cls) -> List[User]:
        return cls.users


# Adding books to the library
book3 = Book("1984", "George Orwell", "9876", 4)
book4 = Book("To Kill a Mockingbird", "Harper Lee", "5432", 2)
LibrarySystem.add_book(book3)
LibrarySystem.add_book(book4)

# Registering users
user3 = User("Alice Smith", "alice@example.com")
user4 = User("Bob Johnson", "bob@example.com")
LibrarySystem.register_user(user3)
LibrarySystem.register_user(user4)

# Borrowing books
LibrarySystem.borrow_book(user3, "9876")
LibrarySystem.borrow_book(user4, "5432")
LibrarySystem.borrow_book(user3, "5432")
LibrarySystem.borrow_book(user3, "1234")  # Non-existent ISBN

# Returning books
LibrarySystem.return_book(user3, "9876")
LibrarySystem.return_book(user3, "5432")
LibrarySystem.return_book(user4, "5432")

# Listing available books
print("\nAvailable Books:")
books_available = LibrarySystem.list_books()
for book in books_available:
    print(f"{book.title} by {book.author}, ISBN: {book.isbn}, Copies available: {book.num_copies}")

# Listing users and their borrowed books
print("\nUsers and their borrowed books:")
users_list = LibrarySystem.list_users()
for user in users_list:
    print(f"{user.name} ({user.email}) has borrowed:")
    for book in user.books_borrowed:
        print(f"- {book.title} by {book.author}, ISBN: {book.isbn}")
