from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base

class Topic(Base):
    __tablename__ = 'topics'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    unit_id = Column(Integer, ForeignKey('units.id'))
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    
    unit = relationship('Unit', back_populates='topics')
    subject = relationship('Subject', back_populates='topics')
    math_problems = relationship('StoredMathProblem', back_populates='topic')

