from pymongo import MongoClient
from config import settings

client = None

def connect_db():
    global client
    try:
        client = MongoClient(settings.MONGODB_URL)
        client.admin.command('ping')
        print("Connected to MongoDB successfully!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")

def get_db():
    if client is None:
        connect_db()
    if client:
        return client.assignment
    else:
        raise ConnectionError("Database connection is not established.")
