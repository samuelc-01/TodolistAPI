from fastapi import FastAPI
from .db.database import Base, engine
from .schemas.models import User
from .routes import auth

app = FastAPI(title="todolist api")

Base.metadata.create_all(bind=engine)
#User.Base.metadata.create_all(bind=engine)
app.include_router(auth.router, prefix="/auth", tags=["Authetication"])
