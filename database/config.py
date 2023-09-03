from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_FILE = 'email_module.db'

engine = create_engine(f'sqlite:///{DATABASE_FILE}', echo=True)
Session = sessionmaker(bind=engine)
