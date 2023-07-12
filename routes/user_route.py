from fastapi import APIRouter
from config.db import database
from schemas.main import userEntity, usersEntity
from models.main import User
from passlib.hash import sha256_crypt

user = APIRouter()

@user.get('/users' ,tags= ['Find all users'])
def find_all_users():
    #return usersEntity(connection.database.users.find())
    return usersEntity(database.users.find())

@user.get('/users/{id}' ,tags= ['Find user by id'])
def find_user():
    return "Usuarios que esten en la app."

@user.post('/users' ,tags= ['Create a new user'])
def create_user( user: User):
    new_user = dict(user)
    new_user['password']  = sha256_crypt.encrypt(new_user['password'])
    del new_user['id']
    id = database.users.insert_one(new_user).inserted_id
    user = database.users.find_one({'_id': id})
    return userEntity(user)

@user.put('/users/{id}' ,tags= ['Update a user'])
def update_user():
    return "Usuarios que esten en la app."

@user.delete('/users/{id}' ,tags= ['Delete a user'])
def delete_user():
    return "Usuarios que esten en la app."