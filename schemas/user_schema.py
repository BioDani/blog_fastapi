def userSchema(item) -> dict:
    return {
        'id' : item['id'],
        'name' : item['name'],
        'email' : item['email'],
        'password' : item['password'],
        'about' : item['about']
    }