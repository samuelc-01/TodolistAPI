from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/ping")
def ping_user():
    return {"message": "pong from user route"}