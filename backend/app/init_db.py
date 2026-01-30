from app.database import engine, Base
from app import models

#creates corresponding SQL tables

def init_db():
    #creates tables if they don't exist
    Base.metadata.create_all(bind=engine) #create tables if don't exist

if __name__ == "__main__":
    init_db()
    print("Database initialized")
