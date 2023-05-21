import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://hello_fastapi:hello_fastapi@localhost/hello_fastapi_dev")

# Create engine
engine = create_engine('sqlite:///database.db', echo=True)

# Create session
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

database = Database(DATABASE_URL)