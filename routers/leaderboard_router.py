from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import leaderboard_service   
from schemas.leaderboard_out import LeaderboardOut
from models import User
from models.db import get_db

router = APIRouter()

# Get the entire leaderboard (users ranked by total points)
@router.get("/leaderboard", response_model=list[LeaderboardOut])
def get_leaderboard(db: Session = Depends(get_db)):
    return leaderboard_service.get_leaderboard(db)

# Get all users by rank (Gold, Silver, Bronze)
@router.get("/leaderboard/rank/{rank}", response_model=list[LeaderboardOut])
def get_users_by_rank(rank: str, db: Session = Depends(get_db)):
    users = leaderboard_service.get_users_by_rank(db, rank)
    if not users:
        raise HTTPException(status_code=404, detail=f"No users found in {rank} rank")
    return users

# Get a user's rank number (placement on the leaderboard)
@router.get("/leaderboard/user/{user_id}/rank_number")
def get_user_rank_number(user_id: int, db: Session = Depends(get_db)):
    rank = leaderboard_service.get_user_rank_number(db, user_id)
    if not rank:
        raise HTTPException(status_code=404, detail="User not found or invalid rank")
    return {"rank_number": rank}

# Get a user's rank tier (Gold, Silver, Bronze)
@router.get("/leaderboard/user/{user_id}/rank_tier")
def get_user_rank_tier(user_id: int, db: Session = Depends(get_db)):
    tier = leaderboard_service.get_user_rank_tier(db, user_id)
    if not tier:
        raise HTTPException(status_code=404, detail="User not found or invalid tier")
    return {"rank_tier": tier}
