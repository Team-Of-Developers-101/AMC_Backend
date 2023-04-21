"""
Copyright (c) 2023 - present amc.com
"""
import os
import random
import string
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())


class Config(object):
    DEBUG = False
    TESTING = False
    # Set up the App SECRET_KEY
    SECRET_KEY = os.getenv('SECRET_KEY', None)
    # suppress sqlalchemy modification errors
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    if not SECRET_KEY:
        SECRET_KEY = ''.join(
            random.choice(
                string.ascii_letters
            ) for i in range(32)
        )
    SWAGGER = {
        'title': "Flask API",
        'uiversion': 3
    }
    CORS_HEADERS = 'Content-Type'
    # print(SECRET_KEY)


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI")
    pass


class DevConfig(Config):
    DEBUG = True
    sql_lite = "sqlite:///dev_database.db"
    SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", default=sql_lite)


configs = {'development': DevConfig, 'production': ProdConfig}
