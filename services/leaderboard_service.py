from sqlalchemy.orm import Session
from sqlalchemy import func
from models.user import User
from models.leaderboard import Leaderboard

def get_leaderboard(db: Session):
    # Get all users ordered by points in descending order (user's rank is determined by their position)
    return db.query(User).order_by(User.total_points.desc()).all()

def get_users_by_rank(db: Session, rank: str):
    # Get users based on their rank range (Gold, Silver, Bronze)
    leaderboard = get_leaderboard(db)
    
    if rank == "Gold":
        return leaderboard[:5]  # Users ranked 1-5 (Gold)
    elif rank == "Silver":
        return leaderboard[5:20]  # Users ranked 6-20 (Silver)
    elif rank == "Bronze":
        return leaderboard[20:50]  # Users ranked 21-50 (Bronze)
    else:
        return []

def get_user_rank_number(db: Session, user_id: int):
    # Find the user's rank based on their position in the leaderboard
    leaderboard = get_leaderboard(db)
    rank = next((index + 1 for index, user in enumerate(leaderboard) if user.id == user_id), None)
    return rank

def get_user_rank_tier(db: Session, user_id: int):
    rank = get_user_rank_number(db, user_id)
    
    if not rank:
        return None
    
    # Determine the tier based on the rank number
    if rank <= 5:
        return "Gold"
    elif rank <= 20:
        return "Silver"
    elif rank <= 50:
        return "Bronze"
    else:
        return "Out of Top 50"
