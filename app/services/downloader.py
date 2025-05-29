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

async def download_youtube_video(url: str, quality: str = 'best') -> list:
    if not (url.startswith("https://www.youtube.com/") or url.startswith("https://youtu.be/")):
        raise ValueError("Invalid YouTube video URL")
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, _download_youtube, url, quality)

def _download_youtube(url: str, quality: str = 'best') -> list:
    file_paths = []
    with YoutubeDL({'quiet': True}) as ydl:
        info = ydl.extract_info(url, download=False)
        if quality == 'all':
            # Map: {height: format}
            formats_by_height = {}
            for fmt in info['formats']:
                # Any mp4 with video and height (allow video-only, let yt-dlp mux)
                if (
                    fmt.get('ext') == 'mp4'
                    and fmt.get('height')
                    and fmt.get('format_id')
                    and fmt.get('vcodec') != 'none'  # must have video
                ):
                    height = fmt['height']
                    # Only keep one format per height (highest bitrate if duplicates)
                    if height not in formats_by_height or (
                        fmt.get('tbr', 0) > formats_by_height[height].get('tbr', 0)
                    ):
                        formats_by_height[height] = fmt
            for height, fmt in sorted(formats_by_height.items()):
                ydl_opts = {
                    'outtmpl': os.path.join(DOWNLOAD_DIR, f"{info['id']}_{height}p.%(ext)s"),
                    'format': f"{fmt['format_id']}+bestaudio",
                    'quiet': True,
                    'merge_output_format': 'mp4'
                }
                with YoutubeDL(ydl_opts) as ydl_format:
                    ydl_format.download([url])
                file_paths.append(os.path.join(DOWNLOAD_DIR, f"{info['id']}_{height}p.mp4"))
        else:
            ydl_opts = {
                'outtmpl': os.path.join(DOWNLOAD_DIR, '%(id)s.%(ext)s'),
                'format': 'mp4/bestvideo+bestaudio/best',
                'quiet': True,
                'merge_output_format': 'mp4'
            }
            with YoutubeDL(ydl_opts) as ydl_best:
                info = ydl_best.extract_info(url, download=True)
                file_paths.append(ydl_best.prepare_filename(info))
    return file_paths



def _download(url: str) -> str:
    ydl_opts = {
        'outtmpl': os.path.join(DOWNLOAD_DIR, '%(id)s.%(ext)s'),
        'format': 'mp4/bestvideo',
        'quiet': True
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        filename = ydl.prepare_filename(info)
    return filename