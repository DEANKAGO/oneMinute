from flask_sqlalchemy import SQLAlchemy
from ..app import db


db = SQLAlchemy()
class User(db.Model):