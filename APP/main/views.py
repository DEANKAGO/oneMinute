from flask import Blueprint, render_template as render_template
from APP.main import main_blueprint as main
from crud import *
import APP
from .forms import New_User


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
    form = New_User()

    if form.is_submitted():
        from ...manage import db
        from APP.models import User
        from ...crud import create_User

        obj={'name':form.name.data,'email':form.email.data,'password':form.password.data}

    create_User(object, User, db)


if __name__ == "__main__":
    main.run(debug=True, use_reloader=False)
