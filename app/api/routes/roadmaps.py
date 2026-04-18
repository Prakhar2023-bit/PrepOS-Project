from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.services.ai_engine import generate_career_roadmap

router = APIRouter()

# 1. The input schema (what the user types in)
class RoadmapRequest(BaseModel):
    target_role: str
    current_skills: str = "None specified"

# 2. The endpoint
@router.post("/generate")
def create_roadmap(request: RoadmapRequest):
    """
    Generate a 3-step AI-powered roadmap for a specific role.
    """
    try:
        # Call the AI Engine
        roadmap_json = generate_career_roadmap(
            target_role=request.target_role, 
            current_skills=request.current_skills
        )
        
        # Return the generated JSON directly to the user/frontend
        return {"status": "success", "data": roadmap_json}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))