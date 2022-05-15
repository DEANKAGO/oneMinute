from unicodedata import category
from flask_sqlalchemy import SQLAlchemy
from crud import *
import app

# from werkzeug.security import generate_password_hash,check_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    email = db.Column(db.String)
    password = db.Column(db.String)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<name: {}>'.format(self.name)

    # pass_secure = db.Column(db.String)
    # @property
    # def passwords(self):
    #     raise AttributeError('You cannot read the password attribute')

    # @password.setter
    # def passwords(self,password):
    #     self.pass_secure = generate_password_hash(password)

    # def verify_password(self, password):
    #     return check_password_hash(self.pass_secure, password)


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)

    def __init__(self, object):
        self.comment = object['comment']


class Pitches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship(Categories, backref=db.backref('pitches'))

    def __init__(self, object):
        self.category = object['category']


class Votes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    downvote = db.Column(db.Integer, db.ForeignKey('pitches.id'))

    def __init__(self, object):
        self.name = object['name']
        self.downvote = object['downvote']
        self.upvote = object['upvote']

    def __repr__(self):
        return {'name': self.name, 'downvote': self.downvote, 'upvote': self.upvote}
