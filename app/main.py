from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import insta, youtube, tiktok
import os

app = FastAPI()

# Mount the downloads directory for serving video files
if not os.path.exists("downloads"):
    os.makedirs("downloads")
app.mount("/downloads", StaticFiles(directory="downloads"), name="downloads")

app.include_router(insta.router)
app.include_router(youtube.router)
app.include_router(tiktok.router)

