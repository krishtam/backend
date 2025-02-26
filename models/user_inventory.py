from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.db import Base

class UserInventory(Base):
    __tablename__ = 'user_inventories'
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    inventory_item_id = Column(Integer, ForeignKey('inventory_items.id'))