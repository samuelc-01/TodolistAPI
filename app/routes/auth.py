from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import verify_password, create_access_token
from app.db.database import get_db
from app.schemas.models import User
from app.schemas.token import Token
from app.core.security import get_password_hash

#test commit vscode
router = APIRouter()

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email== form_data.username).first()

    if not user:
        raise HTTPException(status_code=401, detail="user does not exist")

    if  not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=400, detail="input not valid")

    token = create_access_token({"sub": user.email})
    return {"access_token": token, "token_type": "bearer"}

