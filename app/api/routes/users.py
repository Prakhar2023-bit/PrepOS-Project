from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse

router = APIRouter()

@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user profile.
    """
    # 1. Check if the user already exists
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Convert the Pydantic schema into a SQLAlchemy model
    new_user = User(
        name=user.name,
        email=user.email,
        target_role=user.target_role,
        current_skills=user.current_skills
    )
    
    # 3. Save to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user