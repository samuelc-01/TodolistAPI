from fastapi import APIRouter

router = APIRouter(prefix="/todos", tags=["Todos"])

@router.get("/ping")
def ping_todo():
    return {"message": "pong from todo route"}

