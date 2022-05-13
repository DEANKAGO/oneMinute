from unicodedata import category
from flask_sqlalchemy import SQLAlchemy
from crud import *
import APP

# from werkzeug.security import generate_password_hash,check_password_hash


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    comments = db.Column(db.String)

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
    upvote = db.Column(db.Integer, db.ForeignKey(''))
    downvote = db.Column(db.Integer, db.ForeignKey(''))




    def __init__(self, object):
        self.name = object['name']
        self.downvote = object['downvote']
        self.upvote = object['upvote']

    def __repr__(self):
        return {'name': self.name, 'downvote': self.downvote, 'upvote': self.upvote}



