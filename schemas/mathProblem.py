from pydantic import BaseModel, ConfigDict
from typing import Optional, Any, Dict

class MathProblemBase(BaseModel):
    id: int | None = None
    problem: str
    solution: str
    grade_level: str
    unit_id: int | None = None
    topic_id: int | None = None
    answer: Optional[float] = None
    explanation: Optional[str] = None
    hints: Optional[list[str]] = None

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )


class MathProblemCreate(MathProblemBase):
    pass

class MathProblem(MathProblemBase):
    id: int

    model_config = ConfigDict(
        from_attributes=True,
        arbitrary_types_allowed=True
    )
