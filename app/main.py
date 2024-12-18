from fastapi import FastAPI
from app import app
from app.api.v1 import auth, users

# Include routers
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])
app.include_router(users.router, prefix="/api/v1/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI Auth System"}