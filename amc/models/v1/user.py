"""
User class
"""
from amc.configs.alchemyinit import db
from sqlalchemy import Enum, func, text
from uuid import uuid4
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash


class User(db.Model, UserMixin):
    """model for users"""
    __tablename__ = "users"
    id = db.Column(db.String(length=50), primary_key=True,
                   default=str(uuid4), unique=True)
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(250))
    gender = db.Column(Enum("Male", "Female", "Others"))
    created_at = db.Column(db.DateTime, server_default=func.now())
    updated_at = db.Column(
        db.DateTime,
        server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
    )

    def __init__(self, id, username, email, password, gender) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.password = generate_password_hash(password).decode('utf8')
        self.gender = gender

    def __repr__(self):
        return {
            "id": {self.id}, "username": {self.username},
            "email": {self.email}, "gender": {self.gender}
        }
