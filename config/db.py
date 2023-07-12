from pymongo import MongoClient
from dotenv import dotenv_values

config = dotenv_values(".env")

connection = MongoClient(config["MONGODB_CONNECTION_URI"])
connection.database = connection.mongodb_client[config["DB_NAME"]]
print("Connected to the MongoDB database!")