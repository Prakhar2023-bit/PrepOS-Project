from fastapi import FastAPI
from app.db.session import engine, Base

# Import the models so SQLAlchemy knows they exist before creating tables
from app.models import user, roadmap 

# This single line creates all your database tables automatically
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="PrepOS API",
    description="Backend for the AI-Augmented Career Accelerator",
    version="1.0.0"
)

@app.get("/")
async def health_check():
    return {
        "status": "online", 
        "message": "PrepOS Backend is running securely.",
        "database": "connected and tables created"
    }