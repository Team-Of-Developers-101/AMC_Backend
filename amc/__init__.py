"""Application Factory
- Copyright (c) 2023 - present amc.com
"""

from flask import Flask
from amc.configs.config import configs
from amc.models import User
from amc.routes.v1.welcome import welcome
from amc.routes.v1.user import user_bp
from amc.utils.utils import (
    constants, resource_not_found,
    internal_server_error, wrong_logins, correct_logins
)
from amc.configs.extensions import db, init_app


def create_app():
    """
    The create_app function is the entry point for our application.
    It takes no arguments and returns a Flask object that we can use to run
    our app.
    The function does the following:
    * Creates an instance of Flask using __name__ as the argument, which
        tells flask where to look for templates and static files
        (among other things).

    * return: An instance of the flask class
    """
    environ = constants.environ
    app = Flask(__name__)
    app.config.from_object(configs.get(environ))
    db.app = app
    init_app(app)
    app.register_blueprint(welcome, url_prefix='/api/v1')
    app.register_blueprint(user_bp, url_prefix='/api/v1/')
    app.register_error_handler(401, wrong_logins)
    app.register_error_handler(401, correct_logins)
    app.register_error_handler(404, resource_not_found)
    app.register_error_handler(500, internal_server_error)

    return app
