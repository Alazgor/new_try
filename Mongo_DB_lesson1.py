from pymongo import MongoClient

def connect_to_mongodb(host, port, database_name):
    client = MongoClient(host, port)
    return client[database_name]

def insert_document(collection, document):
    return collection.insert_one(document).inserted_id

if __name__ == "__main__":
    # Connection details
    mongodb_host = 'localhost'
    mongodb_port = 27017
    database_name = 'Students'  # Name DB
    collection_name = 'students'  # Name Collection

    # Connect to MongoDB
    db = connect_to_mongodb(mongodb_host, mongodb_port, database_name)
    collection = db[collection_name]
    print(f"Connected to MongoDB: {mongodb_host}:{mongodb_port}, Database: {database_name}")

    document = {
        "name": "John",
        "age": 35,
        "email": "johndoe@example.com"
    }
    inserted_id = insert_document(collection, document)
    print(f"Inserted document with ID: {inserted_id}")

    result = collection.find({'name': 'John'})
    print(list(result))


