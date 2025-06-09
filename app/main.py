from fastapi import FastAPI
from . import models
from .database import engine
from .routes import auth

app = FastAPI(title="todolist api")

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router, prefix="/auth", tags=["Authetication"])
