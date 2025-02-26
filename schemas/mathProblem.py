from pydantic import BaseModel
from typing import Optional, Any, Dict

class MathProblemBase(BaseModel):
    question: str
    difficulty: int
    topic_id: int
    answer: Optional[float] = None
    explanation: Optional[str] = None
    hints: Optional[list[str]] = None
    metadata: Optional[Dict[str, Any]] = None

class MathProblemCreate(MathProblemBase):
    pass

class MathProblemResponse(MathProblemBase):
    id: int
    
    class Config:
        from_attributes = True
