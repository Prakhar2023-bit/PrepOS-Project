from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str # NEW: Demand a password on registration
    target_role: Optional[str] = None
    current_skills: Optional[str] = None

# 2. The data we RETURN to the frontend after creating the user
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    target_role: Optional[str]

    # This tells Pydantic to read data directly from the SQLAlchemy model
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str # NEW: Demand a password on login