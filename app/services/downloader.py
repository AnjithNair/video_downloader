import asyncio
from yt_dlp import YoutubeDL
import os
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def download_instagram_reel(url: str) -> str:
    if not url.startswith("https://www.instagram.com/reel/"):
        raise ValueError("Invalid Instagram Reels URL")
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _download, url)

async def download_youtube_video(url: str) -> str:
    if not (url.startswith("https://www.youtube.com/") or url.startswith("https://youtu.be/")):
        raise ValueError("Invalid YouTube video URL")
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _download, url)

def _download(url: str) -> str:
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(id)s.%(ext)s'),
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'quiet': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return filename

async def download_tiktok_video(url: str) -> str:
    if not (url.startswith("https://www.tiktok.com/") or "tiktok.com/@" in url):
        raise ValueError("Invalid TikTok video URL")
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _download, url)
