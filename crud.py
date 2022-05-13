from flask_bcrypt import Bcrypt
from app.models import db

bcrypt = Bcrypt()


def create_User(object, app, db):
  if 'password' in object:
    newPassword = bcrypt.generate_password_hash(object['password'])
    object['password'] = newPassword
  return {'status': False, '_payload': 'object does not contain password'}


def create_data(object, app, db):
    print()
