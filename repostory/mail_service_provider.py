from database.config import Session
from models.models import MailServiceProvider


class MailServiceProviderRepository:

	@staticmethod
	def get_mail_provider(provider_name):
		session = Session()
		provider = session.query(MailServiceProvider).filter_by(provider_name=provider_name).one_or_none()
		session.close()
		return provider

	@staticmethod
	def get_default_provider():
		session = Session()
		default_provider = session.query(MailServiceProvider).filter_by(default_provider=True).one_or_none()
		session.close()
		return default_provider
