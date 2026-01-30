#defines ORM models (tables)

from sqlalchemy import Column, Integer, String, Text
from .database import Base

#Analysis: each row is a single AI analysis
class Analysis(Base):
    __tablename__ = "analyses"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False) #original input text
    result = Column(Text, nullable=False) #LLM output (JSON)
