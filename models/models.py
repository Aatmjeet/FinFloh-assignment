from database.config import engine
from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Email(Base):
    __tablename__ = 'tbl__email'
    id = Column(Integer, primary_key=True)
    sender = Column(String, nullable=False)
    receiver = Column(String, nullable=False)
    subject = Column(String, nullable=False)
    body = Column(Text, nullable=False)
    status = Column(String, default='pending', nullable=False)
    is_read = Column(Boolean, default=False, nullable=False)
    provider_name = Column(String, nullable=False)


class MailServiceProvider(Base):
    __tablename__ = 'tbl__mail_service_provider'
    id = Column(Integer, primary_key=True)
    provider_name = Column(String, nullable=False, unique=True)
    default_provider = Column(Boolean, nullable=False)


Base.metadata.create_all(engine)