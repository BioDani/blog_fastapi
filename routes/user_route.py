from fastapi import APIRouter, Response, status
from config.db import database
from schemas.main import userEntity, usersEntity
from models.main import User
from passlib.hash import sha256_crypt
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

user = APIRouter()


@user.get('/users', tags=['users'], response_model= list[User])
def find_all_users():
    return usersEntity(database.users.find())


@user.get('/users/{id}', tags=['users'], response_model= User)
def find_user(id: str):
    user = userEntity(database.users.find_one({'_id': ObjectId(id)}))
    del user['password']
    return user


@user.post('/users', tags=['users'], response_model= User)
def create_user(user: User):
    new_user = dict(user)
    new_user['password'] = sha256_crypt.encrypt(new_user['password'])
    del new_user['id']
    id = database.users.insert_one(new_user).inserted_id
    user = database.users.find_one({'_id': id})
    return userEntity(user)



@user.put('/users/{id}', tags=['users'], response_model= User)
def update_user(id: str, user: User):
    database.users.find_one_and_update(
        {'_id': ObjectId(id)},
        {'$set': dict(user)}
    )
    
    user = userEntity(database.users.find_one({'_id': ObjectId(id)}))
    del user['password']
    return user


@user.delete('/users/{id}', tags=['users'], status_code= status.HTTP_204_NO_CONTENT)
def delete_user(id: str):
    database.users.find_one_and_delete({'_id': ObjectId(id)})
    return Response(status_code=HTTP_204_NO_CONTENT)
