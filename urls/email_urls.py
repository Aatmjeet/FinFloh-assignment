from flask import Blueprint
from flask_restful import Api
from views.email_service_views import SendEmail, EmailStatus, MarkEmailAsRead


# Create the Blueprint
api_blueprint = Blueprint('api', __name__)

# Create the API and add the resources to it
urls = Api(api_blueprint)

urls.add_resource(SendEmail, '/email/')
urls.add_resource(EmailStatus, '/email/<int:email_id>')
urls.add_resource(MarkEmailAsRead, '/email/read/<int:email_id>')
