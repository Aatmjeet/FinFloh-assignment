from flask import request
from flask_restful import Resource, abort
from controllers.email_controller import EmailController
from common.DTO.email_dto import EmailRequest
from common.services.email_provider_factory import EmailProviderFactory
from common.schema.mail_schema import SendMailSchema


class SendEmail(Resource):
	def post(self):
		schema = SendMailSchema()

		try:
			serialized_data = schema.load(request.get_json())
		except Exception as e:
			abort(400, error=str(e))

		mail_provider = EmailProviderFactory().get_email_provider(preferred_provider=serialized_data["mail_provider"])
		email_request = EmailRequest(serialized_data['sender'], serialized_data['receiver'], serialized_data['subject'], serialized_data['body'], mail_provider)
		return EmailController.send_email(email_request)


class EmailStatus(Resource):
	def get(self, email_id):
		return EmailController.get_status(email_id=email_id)


class MarkEmailAsRead(Resource):
	def post(self, email_id):
		return EmailController.mark_as_read(email_id=email_id)
