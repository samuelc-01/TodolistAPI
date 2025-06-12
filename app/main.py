from fastapi import FastAPI, Request
from app.routes import auth, protected, todos
from app.core.exception_handler import register_exception_handlers
from fastapi.middleware.cors import CORSMiddleware
import time
import logging

app = FastAPI()

app.include_router(auth.router)
app.include_router(protected.router)
app.include_router(todos.router)
register_exception_handlers(app)


origins = ["http://localhost:3000", "http://127.0.0.1:3000"]  # ajuste se necessário

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start = time.time()
    response = await call_next(request)
    duration = time.time() - start
    response.headers["X-Process-Time"] = str(duration)
    return response


logging.basicConfig(level=logging.INFO)