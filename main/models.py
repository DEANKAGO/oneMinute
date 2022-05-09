from flask_sqlalchemy import SQLAlchemy
from ..app import db


db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True)
    comments = db.Column(db.String)

    def __init__(self, name) -> None:
        self.name = name

    def __str__(self) -> str:
        return self.name


class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text)


class Pitches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.Integer, db.ForeignKey('categories.id'))