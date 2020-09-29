# -*- coding: UTF-8 -*-
from flask import render_template, request, redirect, Flask, Blueprint
from flask_login import login_user, login_required
from model.user_model import User
from model import login_manager
from form.login_form import LoginForm

# Blueprint 蓝图
userRoute = Blueprint('user', __name__, url_prefix='/', template_folder='../templates')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@userRoute.before_request
def before_request():
    pass


@userRoute.route('/')
def hello_world():
    #return "hi"
    return redirect('/login')

@userRoute.route('/success')
@login_required
def index():
    return render_template('success.html')


@userRoute.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if not form.validate_on_submit():
            print form.errors
            return render_template('login.html', form=form)

        user = User.query.filter(User.accountNumber == form.accountNumber.data,
                                 User.password == form.password.data).first()
        if user:
            login_user(user)
            return render_template('success.html')

    return render_template('login.html', form=form)