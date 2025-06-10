from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.security import create_access_token
from app.db.database import get_db
from app.schemas.models import User, UserCreate

router = APIRouter()

@router.post("/register", response_model=User)
def register_user(user_data: UserCreate = Depends(), db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already exists")

    new_user = User(email=user_data.email, hashed_password=create_access_token({"sub": user_data.email}))
    db.add(new_user)
    db.commit()

    return new_user

@router.get("/ping")
def ping_user():
    return {"message": "pong from user route"}