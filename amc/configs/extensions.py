"""Application extensions module
- Copyright (c) 2023 - present amc.com
"""
from flask import redirect, url_for
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.pool import QueuePool
from flask_cors import CORS
from flasgger import Swagger
from amc.configs.swagger import template, swagger_config


db = SQLAlchemy(
    engine_options={
        "pool_pre_ping": True,  # re-connects if connection is not alive
        "pool_size": 10,  # no. of conns that will be persisted in the pool
        "poolclass": QueuePool
    }
)


def init_app(app):
    """
    The init_app function is a Flask extension initializer.
    It takes the application object as an argument and does the initializations
    of several extensions used.
    The function also returns a tuple of objects that were created or
    initialized, so that we can use them later in our code.

    * app: Create the database and to initialize the swagger documentation
    * return: A tuple of the app, cors and migrate objects
    """
    db.init_app(app)
    Swagger(app, config=swagger_config, template=template)
    migrate = Migrate(app, db)
    cors = CORS(app, resources={r"/api/v1*": {"origins": "*"}})
    with app.app_context():
        db.create_all()

    @app.route("/")
    def default():
        """
        The default function is a redirect to the home.index function, which
        is the base route of our application.
        """
        return redirect(url_for("home.welcome_status"))
    return (app, cors, migrate)
