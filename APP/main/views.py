from flask import Blueprint, redirect, url_for, render_template as render_template
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


@main.route('/add', methods=['GET', 'POST'])
def add():
    form = New_User()

    if form.is_submitted():
        from ...manage import db
        from APP.models import User
        from ...crud import create_User

        obj = {'name': form.name.data, 'email': form.email.data,
               'password': form.password.data}

    create_User(object, User, db)
    return redirect(url_for('main.index'))
    return render_template('add_user.html',)

    # except Exception as e:
    # return render_template("error.html", mess=e)

    # if __name__ == "__main__":
    #     main.run(debug=True, use_reloader=False)

@main.route("/delete/<id>",methods=["GET", "POST"])
def delete(id):
    from APP.models import User
    user=User.query.get(id)
    page_title=f"Delete User: {user.name}"
    return render_template("users/delete.html",page_title=page_title,user=user.name)


@main.route('/comment/new/<int:pitch_id>', methods = ['GET', 'POST'])
# @login_required
def new_comment(comment_id):
  """
  View new comment page function that returns the comments on pitches
  """