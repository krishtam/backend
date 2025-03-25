from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date

class UserBase(BaseModel):
    username: str
    email: EmailStr
    first_name: str
    last_name: str
    birthday: date
    interest: Optional[str] = None
    grade_level: str

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    grade_level: str

class UserOut(UserBase):
    id: int
    total_points: int = 0
    total_progress: float = 0.0
    rank: Optional[str] = None
    
    class Config:
        from_attributes = True

class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    interest: Optional[str] = None
    grade_level: Optional[str] = None

class User(UserBase):
    id: int
    points: int = 0
    level: int = 1
    is_active: bool = True

    class Config:
        from_attributes = True
