"""
Copyright (c) 2023 - present amc.com
"""
import os
from flask import Flask
from flask_cors import CORS, cross_origin
from amc.configs.config import configs
from flasgger import Swagger
from amc.models import User
from amc.routes.v1.welcome import welcome
from amc.utils.utils import resource_not_found, internal_server_error
from amc.configs.alchemyinit import db, init_app
from amc.configs.swagger import template, swagger_config


def create_app():
    environ = os.getenv("ENVIRONMENT")
    app = Flask(__name__)
    cors = CORS(app, resources={r"/api/v1*": {"origins": "*"}})
    app.config.from_object(configs.get(environ))
    Swagger(app, config=swagger_config, template=template)
    db.app = app
    init_app(app)
    app.register_blueprint(welcome, url_prefix='/api/v1')
    app.register_error_handler(404, resource_not_found)
    app.register_error_handler(500, internal_server_error)

    return app
