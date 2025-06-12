from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas.models import Todo
from app.db.database import get_db
from app.routes.protected import get_current_user
from app.schemas.models import User
from app.schemas.schemas import TodoCreate, TodoOut
from typing import List, Optional

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

@router.put("/todos/{todo_id}", response_model=TodoOut)
def update_todo(todo_id: int, todo_data: TodoCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")

    for key, value in todo_data.dict().items():
        setattr(todo, key, value)

    db.commit()
    db.refresh(todo)
    return todo


@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    todo = db.query(Todo).filter(Todo.id == todo_id, Todo.owner_id == current_user.id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    
    db.delete(todo)
    db.commit()
    return

@router.get("/todos", response_model=List[TodoOut])
def read_todos(skip: int = 0, limit: int = 10, completed: bool = None, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    query = db.query(Todo).filter(Todo.owner_id == current_user.id)
    
    if completed is not None:
        query = query.filter(Todo.completed == completed)
    
    return query.offset(skip).limit(limit).all()
