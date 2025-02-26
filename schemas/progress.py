from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class ProgressBase(BaseModel):
    user_id: int
    unit_id: Optional[int] = None
    topic_id: Optional[int] = None
    score: float = 0.0
    completed: bool = False
    last_attempt: Optional[datetime] = None

class ProgressCreate(ProgressBase):
    pass

class ProgressUpdate(BaseModel):
    score: Optional[float] = None
    completed: Optional[bool] = None
    last_attempt: Optional[datetime] = None

class ProgressOut(ProgressBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

class UserProgressSummary(BaseModel):
    total_progress: float
    completed_units: int
    completed_topics: int
    average_score: float
    last_activity: Optional[datetime]
    recent_achievements: List[str] = []

    class Config:
        from_attributes = True
