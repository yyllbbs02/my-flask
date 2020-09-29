# -*- coding: UTF-8 -*-
from flask import Flask
from flask_login import LoginManager
from flow.test_login.common import db

login_manager = LoginManager()
# 指定了未登陆时跳转的页面，即被拦截后统一跳到user/login这个路由下
login_manager.login_view = "user.login"


def create_app(config_filename=None):
    app = Flask(__name__)
    login_manager.init_app(app)

    if config_filename is not None:
        app.config.from_pyfile(config_filename)
        configure_database(app)

    return app


def configure_database(app):
    db.init_app(app)