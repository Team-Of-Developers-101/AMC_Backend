from uuid import uuid4
from flask import request
from amc.repository.v1.user import UserRepo
from amc.utils.utils import custom_response, error_response


def register():
    request_data = request.get_json()
    id = str(uuid4())
    request_data.update({"id": id})
    validated_user = UserRepo.validate_user(request_data)
    new_user = UserRepo.create_user(validated_user)
    return custom_response(message=f"new user has been created", data=new_user, status_code=201)

def login():
    request_data = request.get_json()
    validate = UserRepo.validate_login(request_data)
    return UserRepo.login(validate)
