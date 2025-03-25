from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database.init_db import init_and_seed_db
from app.routers import user_router, leaderboard_router, math_problem_router, auth_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins in development
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_event():
    """Initialize database on startup"""
    init_and_seed_db()

# Include routers
app.include_router(auth_router.router)  # Make sure auth_router is included
app.include_router(user_router.router)
app.include_router(leaderboard_router.router)
app.include_router(math_problem_router.router)

# Add a test endpoint to verify API is working
@app.get("/")
async def root():
    return {"message": "API is running"} 