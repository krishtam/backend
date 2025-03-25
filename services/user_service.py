from sqlalchemy.orm import Session
from models.user import User
from schemas.user import UserCreate


class UserService:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()

    def get_user_by_username(self, username: str) -> User:
        return self.db.query(User).filter(User.username == username).first()

    def get_user_by_id(self, user_id: int) -> User:
        return self.db.query(User).filter(User.id == user_id).first()

    def create_user(self, user_data: UserCreate) -> User:
        db_user = User(
            username=user_data.username,
            email=user_data.email,
            password=user_data.password,
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            birthday=user_data.birthday,
            interest=user_data.interest,
            grade_level=user_data.grade_level
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

def update_user_progress(db: Session, user_id: int, new_progress: float):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        user.total_progress += new_progress
        db.commit()
        db.refresh(user)
    return user
