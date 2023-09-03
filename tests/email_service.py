import unittest
from app import app
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.models import Base, MailServiceProvider


class TestEmailService(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app = app.test_client()

        # Create a new in-memory SQLite database
        self.engine = create_engine('sqlite:///:memory:')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

        # Set up the database
        Base.metadata.create_all(self.engine)


    def tearDown(self):
        # Teardown: clean up the database after each test
        self.session.close()
        self.engine.dispose()

    def test_send_email(self):
        # creating default_mail_provider for testing
        default_mail_provider = MailServiceProvider(provider_name="SendGrid", default_provider=True)
        self.session.add(default_mail_provider)
        self.session.commit()
        data = {
            "sender": "test_sender@example.com",
            "receiver": "test_receiver@example.com",
            "subject": "Test Subject",
            "body": "This is a test email body.",
            "mail_provider": "Mailgun"
        }
        response = self.app.post('/email/', json=data)
        print(response.get_json())
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertIn("email_id", response_data)
        self.assertEqual(response_data["status"], "pending")

    def test_send_email_invalid_data(self):
        data = {
            # Missing some required fields
            "sender": "test_sender@example.com",
            "receiver": "test_receiver@example.com",
        }
        response = self.app.post('/email/', json=data)
        self.assertEqual(response.status_code, 400)
        response_data = response.get_json()
        self.assertIn("error", response_data)


if __name__ == '__main__':
    unittest.main()
