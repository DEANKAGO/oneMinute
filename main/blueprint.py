from flask import Blueprint

main_blueprint = Blueprint(__name__)
from . import views