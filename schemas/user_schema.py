def userEntity(item) -> dict:
    return {
        'id' : str(item['_id']),
        'name' : item['name'],
        'email' : item['email'],
        'password' : item['password'],
        'about' : item['about']
    }
    
def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]