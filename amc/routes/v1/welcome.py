from flask import Blueprint
from calculator.welcome import welcome_status

welcome = Blueprint("home", __name__)

welcome.get("/")(welcome_status)
