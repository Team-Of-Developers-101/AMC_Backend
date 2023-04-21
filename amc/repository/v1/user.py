import json
from uuid import uuid4
from marshmallow import ValidationError
from sqlalchemy import desc
from amc.configs.alchemyinit import db
from amc.models.schema.user import UserSchema
from amc.models.v1.user import User


user_schema = UserSchema()


class UserRepo:
    @staticmethod
    def validate_user(data):
        try:
            validated_user = user_schema.load(data)
        except ValidationError as e:
            raise Exception(e.messages)
        return validated_user

    @staticmethod
    def create_user(validated_user):
        new_user = User(**validated_user)
        db.session.add(new_user)
        db.session.commit()
        resp_data = {**user_schema.dump(new_user)}
        return resp_data

    @staticmethod
    def all_users():
        all = User.query.order_by(desc("created_at")).all()
        serialized_data = json.loads(user_schema.dumps(all, many=True))
        return serialized_data
