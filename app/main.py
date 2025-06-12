from fastapi import FastAPI
from app.routes import auth, protected, todos

app = FastAPI()

app.include_router(auth.router)
app.include_router(protected.router)
app.include_router(todos.router)
