from flask import Blueprint, render_template as render_template
from APP.main import main_blueprint as main
from crud import *
import APP


user = Blueprint('user', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/home', methods=['POST'])
def register():
    # query = request.form.get('query1')
    # selected = request.form.get('query')
    # if (not query or not selected):
    # return 'failure'
    # processed_text = query.upper()
    return render_template('index.html')


@main.route('/', methods=['GET', 'POST'])
def add():
    form = New_user()

    if form.is_submitted():

    create_User(object, APP, db)


if __name__ == "__main__":
    main.run(debug=True, use_reloader=False)
