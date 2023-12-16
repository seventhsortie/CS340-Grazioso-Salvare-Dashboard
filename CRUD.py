from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for the Animal collection in MongoDB """

    def __init__(self, user, passwd, host, port, db, col):
        # Initialise Connection
        self.client = MongoClient(f'mongodb://{user}:{passwd}@{host}:{port}')
        self.database = self.client[db]
        self.collection = self.database[col]

    def create(self, data):
        # Create Method
        if data is not None:
            insert_result = self.collection.insert_one(data)
            return True if insert_result.inserted_id else False
        else:
            raise ValueError("Data parameter is empty")

    def read(self, query):
        # Read Method
        if query is not None:
            return list(self.collection.find(query))
        else:
            raise ValueError("Query is empty")

    def update(self, query, update_values):
        # Update Method
        if query is not None and update_values is not None:
            update_result = self.collection.update_many(query, {'$set': update_values})
            return update_result.modified_count
        else:
            raise ValueError("Query or update values are empty")

    def delete(self, query):
        # Delete Method
        if query is not None:
            delete_result = self.collection.delete_many(query)
            return delete_result.deleted_count
        else:
            raise ValueError("Query is empty")

