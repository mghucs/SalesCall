import os
from pymongo import MongoClient

class Mongo():
    def __init__(self):
        self.client = MongoClient(os.environ.get("ATLAS_URI"))
        self.collection = self.client[os.environ.get("DB_NAME")][os.environ.get("COLLECTION")]
        print("Connected to the MongoDB database!")

    def insert(self, transcript):
        self.collection.insert_one(transcript)
