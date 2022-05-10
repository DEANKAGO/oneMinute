from unicodedata import category
from flask_sqlalchemy import SQLAlchemy
from ..app import db
from werkzeug.security import generate_password_hash,check_password_hash


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    comments = db.Column(db.String)

    pass_secure = db.Column(db.String)
    @property
    def passwords(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def passwords(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.pass_secure, password)



    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)


class Pitches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    category = db.relationship(Categories, backref=db.backref('pitches'))

class Votes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Integer, db.ForeignKey(''))
    downvote = db.Column(db.Integer, db.ForeignKey(''))
