from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class InventoryItemBase(BaseModel):
    name: str
    description: str
    price: float
    category: str

class InventoryItemCreate(InventoryItemBase):
    pass

class InventoryItemOut(InventoryItemBase):
    id: int
    acquired_date: Optional[datetime] = None

    class Config:
        from_attributes = True

class UserInventoryOut(BaseModel):
    user_id: int
    items: List[InventoryItemOut]
    total_items: int

    class Config:
        from_attributes = True
