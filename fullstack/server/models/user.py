from .database import Base 
from sqlalchemy import Column , VARCHAR , DATE , DateTime
from datetime import datetime

# Create User class
class User(Base):
    __tablename__ = 'users'
    username = Column(VARCHAR, unique=True , primary_key=True)
    password = Column(VARCHAR)
    birthday = Column(DATE)
    create_time = Column(DateTime , default=datetime.utcnow() )
    last_login = Column(DateTime , nullable=True )

    def __init__(self, username, password, birthday):
        self.username = username
        self.password = password
        self.birthday = birthday