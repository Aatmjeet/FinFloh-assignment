from flask import jsonify
from flask_restful import abort
from common.DTO.email_dto import EmailResponse, ErrorResponse
from common.services.email_provider_service import EmailProviderService
from repostory.email_repository import EmailRepository


class EmailController:
	@staticmethod
	def send_email(email_request):
		try:
			# Send the email (Assuming the email_provider_service is implemented to handle provider selection)
			EmailProviderService.send_email(email_request)

			email_id = EmailRepository.send_email(email_request.to_dict())
			return jsonify(EmailResponse(email_id, "pending").to_dict())
		except Exception as e:
			return abort(500, error=str(e))

	@staticmethod
	def mark_as_read(email_id):
		try:
			updated = EmailRepository.mark_as_read(email_id)
			if not updated:
				raise Exception("Email not found")
			return jsonify({"email_id": email_id, "is_read": True})
		except Exception as e:
			abort(404, error=str(e))

	@staticmethod
	def get_status(email_id):
		try:
			email = EmailRepository.get_email_status(email_id=email_id)
			if email is None:
				raise Exception("E-mail not found!")
			return jsonify({"email_id": email.id, "status": email.status})
		except Exception as e:
			return abort(404, error=str(e))
