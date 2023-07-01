from marshmallow import Schema, fields


class NoteInputSchema(Schema):
    title = fields.String(required=True)
    content = fields.String(required=True)


class UserInputSchema(Schema):
    username = fields.String(required=True)
    email = fields.Email(required=True)
    password = fields.String(required=True)
