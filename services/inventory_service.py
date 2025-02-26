from models import User, InventoryItem, user_inventory
from models.db import SessionLocal

db = SessionLocal()

def purchase_item(user_id: int, item_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    item = db.query(InventoryItem).filter(InventoryItem.id == item_id).first()
    
    if user and item and user.currency_amount >= item.price:
        user.currency_amount -= item.price
        db.execute(user_inventory.insert().values(user_id=user_id, inventory_item_id=item_id))
        db.commit()
        return {"message": "Item purchased successfully"}
    
    return {"error": "Not enough currency or item not found"}
