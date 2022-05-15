from flask import Flask
from app import create_app
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy
from app.main import main_blueprint
import os
from flask_migrate import Migrate
from app.main import views
from app.models import db

# Creating app instance
app = create_app('development')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')
app.config['SECRET_KEY'] = 'abc123'

migrate = Migrate(app, db)

manager = Manager(app)

manager.add_command('server', Server)
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
