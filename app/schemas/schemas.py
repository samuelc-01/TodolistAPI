from pydantic import BaseModel, EmailStr
from typing import Optional

class UserOut(BaseModel):
    id: int
    username: str
    email: EmailStr

    class Config:
        orm_mode = True



class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    completed: Optional[bool] = False

class TodoCreate(TodoBase):
    pass

class TodoOut(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
