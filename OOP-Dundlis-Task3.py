class Book:
    def __init__(self, title, author, ISBN, pages):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.pages = pages

    def __bool__(self):
        return bool(self.title)

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', '{self.ISBN}')"

    def __len__(self):
        return self.pages

    def __str__(self):
        return f"{self.title} by {self.author} ({self.ISBN})"

    def __eq__(self, other):
        return self.ISBN == other.ISBN

    def __add__(self, other):
        combined_title = self.title
        combined_author = self.author
        combined_ISBN = self.ISBN
        combined_pages = self.pages + other.pages
        return Book(combined_title, combined_author, combined_ISBN, combined_pages)

    def __getitem__(self, index):
        if index == 0:
            return self.title
        elif index == 1:
            return self.author
        else:
            raise IndexError("Index out of range")

# Example usage:
book1 = Book("Title1", "Author1", "ISBN1", 200)
book2 = Book("Title2", "Author2", "ISBN2", 300)

print(bool(book1))          # Output: True
print(len(book1))           # Output: 200
print(str(book1))           # Output: Title1 by Author1 (ISBN1)
print(repr(book1))          # Output: Book('Title1', 'Author1', 'ISBN1')
print(book1 == book2)       # Output: False
print(book1 + book2)        # Output: Book('Title1', 'Author1', 'ISBN1') - combined book
print(book1[0])             # Output: Title1
print(book1[1])             # Output: Author1
