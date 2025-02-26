from sqlalchemy import Column, Integer, ForeignKey, Enum
from sqlalchemy.orm import relationship
from models.db import Base

class Leaderboard(Base):
    __tablename__ = "leaderboard"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    total_quiz_points = Column(Integer, default=0)
    total_minigame_points = Column(Integer, default=0)
    rank = Column(Enum("Gold", "Silver", "Bronze", name="rank_enum"), nullable=True)

    user = relationship("User", back_populates="leaderboard")
