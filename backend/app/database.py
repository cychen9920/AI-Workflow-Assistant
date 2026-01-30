from sqlalchemy import create_engine #create db connection
from sqlalchemy.orm import sessionmaker, declarative_base #create db sessions, ORM models

DATABASE_URL = "sqlite:///./app.db"

#database connection
engine = create_engine(
    #disable check for one thread
    DATABASE_URL, connect_args={"check_same_thread": False}
)

#create database session
SessionLocal = sessionmaker(bind=engine)

#base class for ORM models
Base = declarative_base()
