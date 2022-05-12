from flask import render_template as render_template
from app.main import main_blueprint as main


@main.route('/')
def index():
    return render_template('index.html')
