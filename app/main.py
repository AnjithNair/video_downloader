from fastapi import FastAPI
from app.routers import insta

app = FastAPI()

app.include_router(insta.router)
