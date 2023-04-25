from flask import Blueprint
from calculator.v1.user import register, login


user_bp = Blueprint("user", __name__)

user_bp.route("/register", methods=["POST"], strict_slashes=False)(register)
user_bp.route("/login", methods=["POST"], strict_slashes=False)(login)
