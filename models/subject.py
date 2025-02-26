from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.db import Base    
from models.db import engine

class Subject(Base):
    __tablename__ = 'subjects'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)  # Math, Science, etc.

    # Relationship to Topic
    topics = relationship("Topic", back_populates="subject")
    units = relationship("Unit", back_populates="subject")
    
