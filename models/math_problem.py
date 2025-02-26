from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.db import Base

class MathProblem(Base):
    __tablename__ = 'math_problems'
    
    id = Column(Integer, primary_key=True)
    problem = Column(String)
    solution = Column(String)
    grade_level = Column(String)
    
    unit_id = Column(Integer, ForeignKey('units.id'))  # Foreign key to Unit
    topic_id = Column(Integer, ForeignKey('topics.id'))  # Foreign key to Topic
    
    unit = relationship('Unit')  # Linking to the Unit
    topic = relationship('Topic', back_populates='math_problems')  # Linking to the Topic