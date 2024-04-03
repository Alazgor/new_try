from pymongo import MongoClient
from pprint import pprint
from bson.objectid import ObjectId

class LibraryManager:
    def __init__(self, host='localhost', port=27017, db_name='library', collection_name='books'):
        self.client = MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def add_book(self, title, author, genre):
        book_data = {
            'title': title,
            'author': author,
            'genre': genre
        }
        result = self.collection.insert_one(book_data)
        return result.inserted_id

    def get_book(self, book_id):
        return self.collection.find_one({'_id': ObjectId(book_id)})

    def update_book(self, book_id, new_data):
        result = self.collection.update_one({'_id': ObjectId(book_id)}, {'$set': new_data})
        return result.modified_count

    def delete_book(self, book_id):
        result = self.collection.delete_one({'_id': ObjectId(book_id)})
        return result.deleted_count

if __name__ == "__main__":
    library = LibraryManager()

    # add book
    book1_id = library.add_book("Python Programming", "John Smith", "Programming")
    book2_id = library.add_book("Java Basics", "Alice Johnson", "Programming")
    book3_id = library.add_book("C++ Essentials", "Bob Brown", "Programming")

    # get book ID
    pprint(library.get_book(book1_id))

    # updating book data
    updated_data = {'title': 'Updated Python Programming Book'}
    library.update_book(book1_id, updated_data)
    pprint(library.get_book(book1_id))

    # deleting book
    library.delete_book(book3_id)
    pprint(library.get_book(book3_id))
