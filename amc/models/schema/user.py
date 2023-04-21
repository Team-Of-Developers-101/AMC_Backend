from marshmallow import Schema, fields, validate, EXCLUDE


class UserSchema(Schema):
    id = fields.Str(required=True)
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    gender = fields.Str(
        required=True, validate=validate.OneOf(["Male", "Female", "Others"]))

    class Meta:
        order = True
        unknown = EXCLUDE
