from fastapi import APIRouter
from config.db import connection
from schemas.user_schema import userEntity, usersEntity
from models.user_model import User

user = APIRouter()

@user.get('/users' ,tags= ['Find all users'])
def find_all_users():
    return usersEntity(connection.database.users.find())

@user.get('/users/{id}' ,tags= ['Find user by id'])
def find_user():
    return "Usuarios que esten en la app."

@user.post('/users' ,tags= ['Create a new user'])
def create_user( user: User):
    new_user = dict(user)

@user.put('/users/{id}' ,tags= ['Update a user'])
def update_user():
    return "Usuarios que esten en la app."

@user.delete('/users/{id}' ,tags= ['Delete a user'])
def delete_user():
    return "Usuarios que esten en la app."