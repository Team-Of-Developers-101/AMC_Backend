"""
User class
"""
import os
from datetime import datetime
from amc.configs.extensions import db
from sqlalchemy import Enum, func, text
from uuid import uuid4
from flask_login import UserMixin
from flask_bcrypt import generate_password_hash


class User(db.Model, UserMixin):
    """model for users"""
    __tablename__ = "users"
    id = db.Column(
        db.String(length=50), primary_key=True,
        default=lambda: str(uuid4), unique=True
    )
    username = db.Column(db.String(length=50), nullable=False, unique=True)
    email = db.Column(db.String(length=50), nullable=False, unique=True)
    password = db.Column(db.String(250))
    gender = db.Column(Enum("Male", "Female"))
    created_at = db.Column(db.DateTime, server_default=func.now())
    if os.getenv("DB_URI"):
        updated_at = db.Column(
            db.DateTime,
            server_default=text(
                "CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP")
        )
    else:
        updated_at = db.Column(
            db.DateTime, onupdate=datetime.utcnow, nullable=True)
    # state_id = db.Column(db.Integer, db.ForeignKey('state.id'))
    # TODO In states table
    # users = db.relationship("User", backref='states')

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
