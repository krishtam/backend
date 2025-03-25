from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import user_service, inventory_service, progress_service
from models import User, InventoryItem
from schemas.user import UserOut, UserCreate, User as UserSchema
from schemas.inventory import InventoryItemOut
from schemas.progress import ProgressOut
from models.db import get_db
from services.user_service import UserService

router = APIRouter()

# Get a user by their ID

@router.get("/users/{user_id}", response_model=UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = user_service.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Get a user's inventory
@router.get("/users/{user_id}/inventory", response_model=list[InventoryItemOut])
def get_user_inventory(user_id: int, db: Session = Depends(get_db)):
    return inventory_service.get_inventory_by_user(db, user_id)

# Add an item to user's inventory
@router.post("/users/{user_id}/inventory", response_model=InventoryItemOut)
def add_item_to_inventory(user_id: int, item_id: int, db: Session = Depends(get_db)):
    return inventory_service.add_item_to_user_inventory(db, user_id, item_id)

# Remove an item from user's inventory
@router.delete("/users/{user_id}/inventory/{item_id}")
def remove_item_from_inventory(user_id: int, item_id: int, db: Session = Depends(get_db)):
    return inventory_service.remove_item_from_inventory(db, user_id, item_id)

# Get a user's progress (including completed units, scores, etc.)
@router.get("/users/{user_id}/progress", response_model=ProgressOut)
def get_user_progress(user_id: int, db: Session = Depends(get_db)):
    return progress_service.get_user_progress(db, user_id)

# Update the user's progress (e.g., after completing a challenge or quiz)
@router.post("/users/{user_id}/progress")
def update_user_progress(user_id: int, progress_data: ProgressOut, db: Session = Depends(get_db)):
    return progress_service.update_user_progress(db, user_id, progress_data)

# Get user rank based on performance (total points, quiz results, etc.)
@router.get("/users/{user_id}/rank")
def get_user_rank(user_id: int, db: Session = Depends(get_db)):
    return user_service.get_user_rank(db, user_id)

@router.post("/users/", response_model=UserSchema)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user with the provided details.
    """
    # Check if user with email already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )
    
    # Check if username is taken
    db_user = db.query(User).filter(User.username == user.username).first()
    if db_user:
        raise HTTPException(
            status_code=400,
            detail="Username already taken"
        )
    

    
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=500,
            detail=f"Error creating user: {str(e)}"
        )
