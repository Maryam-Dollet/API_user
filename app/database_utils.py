from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# from config import settings

load_dotenv()
# print(config.settings.model_dump())
DATABASE = os.getenv("DATABASE")
# DATABASE = settings["DATABASE"]
USER = os.getenv("USER")
HOST = os.getenv("HOST")
PASSWORD = os.getenv("PASSWORD")

SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Enables to Connect to the database then to close the connection once the request is fulfilled."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
