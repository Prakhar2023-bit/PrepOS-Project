from fastapi import FastAPI
from app.db.session import engine, Base
from app.models import user, roadmap

from app.api.routes import users

# This single line creates all your database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PrepOS API",
    description="Backend for the AI-Augmented Career Accelerator",
    version="1.0.0"
)

app.include_router(users.router, prefix="/users", tags=["Users"])

@app.get("/")
async def health_check():
    return {
        "status": "online", 
        "message": "PrepOS Backend is running securely.",
        "database": "connected and tables created"
    }