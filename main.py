from fastapi import FastAPI
from app.database.init_db import init_and_seed_db
from app.routers import user_router, leaderboard_router, math_problem_router

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_and_seed_db()

# Include routers
app.include_router(user_router.router)
app.include_router(leaderboard_router.router)
app.include_router(math_problem_router.router) 