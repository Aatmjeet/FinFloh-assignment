class EmailRequest:
    def __init__(self, sender, receiver, subject, body, provider_name):
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.provider_name = provider_name

    def to_dict(self):
        return {
            "sender": self.sender,
            "receiver": self.receiver,
            "subject": self.subject,
            "body": self.body,
            "provider_name": self.provider_name
        }


class EmailResponse:
    def __init__(self, email_id, status):
        self.email_id = email_id
        self.status = status

    def to_dict(self):
        return {
            "email_id": self.email_id,
            "status": self.status
        }


class ErrorResponse:
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {
            "message": self.message,
            "status_code": self.status_code
        }
