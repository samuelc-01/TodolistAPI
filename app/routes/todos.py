from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.models import Todo
from app.db.database import get_db
from app.routes.protected import get_current_user
from app.schemas.models import User
from app.schemas.schemas import TodoCreate, TodoOut
from typing import List

router = APIRouter()

@router.post("/todos", response_model=TodoOut)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_todo = Todo(**todo.dict(), owner_id=current_user.id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@router.get("/todos", response_model=List[TodoOut])
def read_todos(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Todo).filter(Todo.owner_id == current_user.id).all()
