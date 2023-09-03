from database.config import Session
from models.models import Email


class EmailRepository:

	@staticmethod
	def get_email_status(email_id):
		session = Session()
		email_record = session.query(Email).filter_by(id=email_id).one_or_none()
		session.close()
		return email_record

	@staticmethod
	def send_email(email_request):
		session = Session()

		email = Email(**email_request)
		session.add(email)
		session.commit()
		new_id = email.id
		session.close()
		return new_id

	@staticmethod
	def mark_as_read(email_id):
		session = Session()
		email_record = session.query(Email).filter_by(id=email_id).one_or_none()
		if email_record is None:
			return False
		email_record.is_read = True
		session.commit()
		session.close()
		return True
