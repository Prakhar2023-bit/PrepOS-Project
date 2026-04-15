from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

# 1. The data we EXPECT from the frontend when a user signs up
class UserCreate(BaseModel):
    name: str
    email: EmailStr # This automatically validates that it's a real email format!
    target_role: Optional[str] = None
    current_skills: Optional[str] = None

# 2. The data we RETURN to the frontend after creating the user
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    target_role: Optional[str]
    created_at: datetime

    # This tells Pydantic to read data directly from the SQLAlchemy model
    class Config:
        from_attributes = True