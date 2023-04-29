import json
from uuid import uuid4
from marshmallow import ValidationError
from sqlalchemy import desc
from amc.configs.extensions import db
from amc.models.schema.user import UserSchema
from amc.models.schema.user import LoginSchema
from amc.models.v1.user import User
from flask_bcrypt import check_password_hash
from amc.utils.utils import wrong_logins, correct_logins


user_schema = UserSchema()
login_schema = LoginSchema()


class UserRepo:
    @staticmethod
    def validate_user(data):
        try:
            validated_user = user_schema.load(data)
        except ValidationError as e:
            raise Exception(e.messages)
        return validated_user

    @staticmethod
    def validate_login(data):
        try:
            validated_login = login_schema.load(data)
        except ValidationError as e:
            raise Exception(e.messages)
        return validated_login

    @staticmethod
    def login(validate):
        username = validate['username']
        password = validate['password']
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.password, password):
            return wrong_logins()
        return correct_logins()

    @staticmethod
    def create_user(validated_user):
        new_user = User(**validated_user)
        db.session.add(new_user)
        db.session.commit()
        resp_data = {**user_schema.dump(new_user)}
        return resp_data
