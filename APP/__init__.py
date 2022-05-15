import os
from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from app.main import main_blueprint

bootstrap = Bootstrap()


def create_app(config_name):

    app = Flask(__name__, template_folder='./templates')

    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    app.register_blueprint(main_blueprint)

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms

    return app
