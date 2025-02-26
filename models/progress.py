from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base    
from models.db import engine

class Progress(Base):
    __tablename__ = 'progress'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    unit_id = Column(Integer, ForeignKey('units.id'))

    # The progress for this particular unit
    progress_percentage = Column(Float, default=0.0)

    # Relationship to User and Unit
    user = relationship("User", back_populates="progress")
    unit = relationship("Unit", back_populates="progress_data")
    

