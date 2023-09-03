## FinFloh Task

### Introduction
Following is my solution to the finFloh's Engineering assignment.
This project is a backend e-mail service based on `Flask, Flask_restful`
which functions on `REST API endpoints`.

### Tech stack used
This service is build on top of `Flask` that uses a basic `SQLite` database
with `SQLalchemy` ORM to send e-mails and maintain state of emails.

----

### Setup and Install
- First part of install is to create and activate a virtual environment.
I have added a virtual environment `virtual`. Otherwise to create a virtual
environment, use
```
python3 -m venv virtual
```
- Now that we have environment, we activate it and install dependencies using
```commandline
source virtual/bin/activate/
pip install -r requirements.txt
```

- We are all setup now, just run the application using
```commandline
python3 -m flask run --host=0.0.0.0 --port=8000
```

---- 

### Schema
In this application, I have created an `Email` object to maintain the state of emails
in the system.
```
class Email(Base):
    __tablename__ = 'tbl__email'
    id = Column(Integer, primary_key=True)
    sender = Column(String, nullable=False)
    receiver = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    status = Column(String, default='pending', nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    
class MailServiceProvider(Base):
    __tablename__ = 'tbl__mail_service_provider'
    id = Column(Integer, primary_key=True)
    provider_name = Column(String, nullable=False, unique=True)
    default_provider = Column(Boolean, nullable=False)

```
Email schema is present in the `/models/models.py` file.


### Available endpoints

- Send Emails: With a mock send_mail() function,
it sends the mail and maintains the state.
- Through this request, we are sending a `mail_provider`. This is a string
parameter which represents our mailing service provider.
- As mentioned in requirements, if this mailing provider is present then we use
the same mail provider. Otherwise, we fall back to our default provider.
```
POST
http://localhost:5000/email/

with post body
{
    "sender": "test_sender@example.com",
    "receiver": "test_receiver@example.com",
    "subject": "Test Subject",
    "body": "This is a test email body."
    "mail_provider":"Mailgun"
}
```
- Get mail status: Gets the status of a mail with given `id`
```
GET
http://localhost:5000/email/<int:id>
```

- Mark mail as read: With a given `id`, it marks a mail as read
```
POST
http://localhost:5000/email/read/<int:id>
```

---

### Test cases
I have provided test cases for the email service in `tests/`.
I am using unittest package to run my test cases with an `In-memory`
SQLite.

Run tests using:
```
python -m unittest tests/email_service.py
```
---

### Design choices
- For schema verification, I have used marshmallow. Invalid post
body will raise valid error.
- I have currently used `SQLite` for quick prototyping. While scaling,
I would prefer a strong DBMS like postges adhering the CAP theorem.
- Used proper DTO's and followed M-V-C structure.


END