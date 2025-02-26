from pydantic import BaseModel

class LeaderboardEntry(BaseModel):
    username: str
    total_points: int
    least_turns: int

    class Config:
        orm_mode = True
