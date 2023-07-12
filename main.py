from fastapi import FastAPI
from routes.main import health, user
from pymongo import MongoClient


app = FastAPI()
app.title = 'Blog using FastAPI'
app.version = '0.1.0'

app.include_router(health)
app.include_router(user)


""" @app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_CONNECTION_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]
    print("Connected to the MongoDB database!")
 """