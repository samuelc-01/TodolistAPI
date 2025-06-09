from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, schemas
from ..database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:db.close()

@router.post("register", response_model=schemas.UserCreate)
def register_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="email already registered")
    
    new_user = models.User(
        username=user.username,
        email=user.email,
        password=user.password # hash after
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user