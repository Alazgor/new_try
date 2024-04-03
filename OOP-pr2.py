class Book:
    def __init__(self, title: str, author: str, ISBN: int, pages_number: int):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.pages_number = pages_number

    def __bool__(self):
        return len(self.title) != 0

    def __repr__(self):
        return f'Book({self.title}, {self.author}, {self.ISBN})'

    def __len__(self):
        return self.pages_number

    def __str__(self):
        return f'{self.title} by {self.author} ({self.ISBN})'

    def __eq__(self, other: 'Book') -> bool:
        if isinstance(other, Book):
            return self.ISBN == other.ISBN
        return False

    def __add__(self, other):
        if isinstance(other, Book):
            if other.author == self.author:
                author = self.author
            else:
                author = self.author + ', ' + other.author
            return Book(self.title, author, self.ISBN, other.pages_number + self.pages_number)
        raise TypeError()

    def __getitem__(self, ind: int):
        if ind == 0:
            return self.title
        elif ind == 1:
            return self.author
        raise IndexError('The index doesn\'t exist')


book1 = Book('Alice in Wonderland', 'Lewis Caroll', 90871456869, 313)
book2 = Book('Harry Potter', 'J.K. Rowling', 9780545582889, 500)

# Test __bool__ method
print(bool(book1))
print(bool(Book('', '', 0, 0)))

# Test __repr__ method
print(repr(book1))

# Test __len__ method
print(len(book1))

# Test __str__ method
print(str(book1))

# Test __eq__ method
print(book1 == book2)

# Test __add__ method
book3 = book1 + book2
print(book3)
print(len(book3))

# Test __getitem__ method
print(book1[0])
print(book1[1])