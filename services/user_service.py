from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate


def create_user(db: Session, user_data: UserCreate):

    db_user = User(
        username=user_data.username,
        email=user_data.email,
        first_name=user_data.first_name,
        last_name=user_data.last_name,
        birthday=user_data.birthday,
        interest=user_data.interest,
        grade_level=user_data.grade_level,
        password=user_data.password,
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def update_user_progress(db: Session, user_id: int, new_progress: float):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.total_progress += new_progress
        db.commit()
        db.refresh(user)
    return user
