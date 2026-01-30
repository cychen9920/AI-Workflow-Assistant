#implement CRUD operations

from sqlalchemy.orm import Session
from .models import Analysis

#create
def create_analysis(db: Session, text: str, result: str):
    entry = Analysis(text=text, result=result)
    db.add(entry)
    #add row to database
    db.commit()
    db.refresh(entry)
    #return ORM object
    return entry

#read
def get_analyses(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Analysis).offset(skip).limit(limit).all()

#update


#delete
