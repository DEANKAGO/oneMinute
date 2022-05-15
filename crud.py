from flask_bcrypt import Bcrypt
from app.models import User

bcrypt = Bcrypt()


def create_User(object):
    if 'password' in object:
        newPassword = bcrypt.generate_password_hash(object['password'])
        object['password'] = newPassword
    user = User(**object)
    # user = User(name=object['name'],
    #             email=object['email'],
    #             password=object['password'])

    return {'created': True}
