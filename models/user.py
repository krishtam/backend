from sqlalchemy import Boolean, Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base    
from models.db import engine

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String)
    grade_level = Column(String)
    level = Column(Integer, default=1)
    # Relationships
    progress = relationship("Progress", back_populates="user")
    inventory_items = relationship("InventoryItem", 
                                 secondary="user_inventories",  # Use the table name as string
                                 back_populates="users")
    leaderboard = relationship("Leaderboard", back_populates="user")
    birthday = Column(DateTime)
    interest = Column(String)
    currency_amount = Column(Float, default=0.0)
    total_progress = Column(Float, default=0.0)
    streak = Column(Integer, default=0)
    last_played_game = Column(DateTime)
    most_recent_unit = Column(String)
    total_points = Column(Integer, default=0)
    least_turns = Column(Integer, default=0)
    rank = Column(String, default="None")
