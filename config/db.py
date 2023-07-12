from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

connection_uri = config["MONGODB_CONNECTION_URI"]
db_name = config["DB_NAME"]

client = MongoClient(connection_uri)
database = client[db_name]

print("Connected to the MongoDB database!")