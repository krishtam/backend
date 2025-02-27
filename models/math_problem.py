from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from models.db import Base

class MathProblem:
    """
    A simple class to hold math problem data (not a SQLAlchemy model)
    """
    def __init__(self, problem: str, solution: str, grade_level: str, 
                 unit_id: int = None, topic_id: int = None,
                 unit: str = None, topic: str = None):
        self.problem = problem
        self.solution = solution
        self.grade_level = grade_level
        self.unit_id = unit_id
        self.topic_id = topic_id
        self.unit = unit
        self.topic = topic

    def to_dict(self):
        return {
            "problem": self.problem,
            "solution": self.solution,
            "grade_level": self.grade_level,
            "unit_id": self.unit_id,
            "topic_id": self.topic_id,
            "unit": self.unit,
            "topic": self.topic
        }

class StoredMathProblem(Base):
    """SQLAlchemy model for stored problems"""
    __tablename__ = 'math_problems'
    
    id = Column(Integer, primary_key=True)
    problem = Column(String)
    solution = Column(String)
    grade_level = Column(String)
    
    unit_id = Column(Integer, ForeignKey('units.id'))
    topic_id = Column(Integer, ForeignKey('topics.id'))
    
    unit = relationship('Unit')
    topic = relationship('Topic', back_populates='math_problems')

    def to_dict(self):
        return {
            "id": self.id,
            "problem": self.problem,
            "solution": self.solution,
            "grade_level": self.grade_level,
            "unit_id": self.unit_id,
            "topic_id": self.topic_id
        }