from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .main import main_blueprint

db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.register_blueprint(main_blueprint)
    app.config['SQLALCHEMY_DATABASE_URI']
    db.init_app(app)

    return app


if __name__ == '__main__':
    create_app()
