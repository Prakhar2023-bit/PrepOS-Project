from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base

class Roadmap(Base):
    __tablename__ = "roadmaps"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    # e.g., "Trilogy Innovations - SDE Roadmap"
    title = Column(String, nullable=False)
    
    # We store the AI-generated roadmap as a JSON object so the frontend can render it easily
    content_json = Column(JSON, nullable=False) 

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # This creates a virtual relationship back to the User model
    owner = relationship("User")