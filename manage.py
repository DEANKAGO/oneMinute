from flask import Flask
from app import create_app
from flask_script import Manager,Server
from flask_sqlalchemy import SQLAlchemy
from app.main import main_blueprint
import os
from flask import Migrate

# Creating app instance
app = create_app('development')

db = SQLAlchemy()

migrate = Migrate(__name__, db)


def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    db.init_app(app)
    migrate.init_app(app, db)

    return dict(app=app, db=db)
    return app 



manager = Manager(app)
# manager.add_command('server',Server)

manager.add_command('server',Server)
if __name__ == '__main__':
    manager.run()