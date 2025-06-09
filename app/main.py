from fastapi import FastAPI
from app.routes import users, todos

app = FastAPI(title="todolist api")

#register endpoints

app.include_router(users.router)
app.include_router(todos.router)
