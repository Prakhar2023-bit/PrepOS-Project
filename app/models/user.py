from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    name = Column(String, nullable=False)
    
    # We will store their target role (e.g., "AI-Augmented SDE")
    target_role = Column(String, nullable=True) 
    
    # Store their current skills to pass to the AI later
    current_skills = Column(String, nullable=True) 

    created_at = Column(DateTime(timezone=True), server_default=func.now())