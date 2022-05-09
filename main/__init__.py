from flask import Blueprint
from flask_sqlalchemy import Migrate 

main_blueprint = Blueprint('main_blueprint', __name__)
from . import views