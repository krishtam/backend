from pydantic import BaseModel
from typing import List

class LeaderboardUser(BaseModel):
    user_id: int
    username: str
    total_points: int
    rank: str  # Gold, Silver, or Bronze

    class Config:
        orm_mode = True  # Allows conversion from SQLAlchemy model to Pydantic model

class LeaderboardOut(BaseModel):
    gold: List[LeaderboardUser]
    silver: List[LeaderboardUser]
    bronze: List[LeaderboardUser]

    class Config:
        orm_mode = True  # Allows conversion from SQLAlchemy model to Pydantic model
