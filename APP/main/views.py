from flask import Blueprint, redirect, url_for, render_template
from app.main import main_blueprint as main
from crud import *
import app
from .forms import New_User


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/home', methods=['GET', 'POST'])
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
        from crud import create_User

        obj = {'name': form.name.data, 'email': form.email.data,
               'password': form.password.data}

        create_User(obj)
        return redirect(url_for('main_blueprint.index'))
    return render_template('add_user.html', form=form)


@main.route("/delete/<id>", methods=["GET", "POST"])
def delete(id):
    from app.models import User
    user = User.query.get(id)
    page_title = f"Delete User: {user.name}"
    return render_template("users/delete.html", page_title=page_title, user=user.name)


@main.route('/comment/new/<int:pitch_id>', methods=['GET', 'POST'])
# @login_required
def new_comment(comment_id):
    """
    View new comment page function that returns the comments on pitches
    """
