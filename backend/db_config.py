# db_config.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# MongoDB connection URI from environment variable or default to localhost
MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')

# Initialize MongoDB client
client = MongoClient(MONGO_URI)

# Select the database
db = client['rule_engine']

# Optionally: print to confirm connection
print(f"Connected to MongoDB: {db}")
