from fastapi import FastAPI
from database import init_db
from routers import user_router, leaderboard_router, math_problem_router



# Create FastAPI app
app = FastAPI()

# Include routers
app.include_router(user_router.router)
app.include_router(leaderboard_router.router)
app.include_router(math_problem_router.router)

# Root endpoint

@app.get("/")
def read_root():
    return {"message": "Welcome to the Math Learning API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)