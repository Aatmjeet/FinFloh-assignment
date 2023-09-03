from repostory.mail_service_provider import MailServiceProviderRepository
from flask_restful import abort


class EmailProviderFactory:
    def get_email_provider(self, preferred_provider):
        mail_provider = MailServiceProviderRepository.get_mail_provider(provider_name=preferred_provider)
        if mail_provider is None:
            return self.get_fallback_provider()
        return mail_provider.provider_name

    @staticmethod
    def get_fallback_provider():
        default_provider = MailServiceProviderRepository.get_default_provider()
        if default_provider is None:
            abort(400, error="No fallback default mail provider found, kindly register default mail provider!")
        return default_provider.provider_name
