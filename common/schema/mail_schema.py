from flask_marshmallow import Marshmallow
from marshmallow import fields

marshmallow = Marshmallow()


class SendMailSchema(marshmallow.Schema):
    sender = fields.Str(required=True)
    receiver = fields.Str(required=True)
    subject = fields.Str(required=True)
    body = fields.Str(required=True)
    mail_provider = fields.Str(required=True)

