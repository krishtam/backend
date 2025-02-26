from sqlalchemy import Column, Integer, String, Float
from models.db import Base
from models.db import engine
from sqlalchemy.orm import relationship
class InventoryItem(Base):
    __tablename__ = 'inventory_items'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    description = Column(String)
    price = Column(Float, default=0.0)
    category = Column(String)  
    users = relationship("User", 
                        secondary="user_inventories",
                        back_populates="inventory_items")

