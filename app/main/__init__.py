from flask import Blueprint
main = Blueprint('main', __name__)
# from flask_migrate import Migrate 

# main_blueprint = Blueprint('main_blueprint', __name__)
from . import views