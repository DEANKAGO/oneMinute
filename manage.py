from flask import Flask
from app import create_app
from flask_script import Manager, Server
from flask_sqlalchemy import SQLAlchemy
from app.main import main_blueprint
import os
from flask_migrate import Migrate
from app.main import views

# Creating app instance
app = create_app('development')
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.sqlite')

db = SQLAlchemy()

migrate = Migrate(app, db)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    db.init_app(app)
    migrate.init_app(app, db)

    return dict(app=app, db=db)
    return app


manager = Manager(app)
# manager.add_command('server',Server)

manager.add_command('server', Server)
if __name__ == '__main__':
    manager.run()
