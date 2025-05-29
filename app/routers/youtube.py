import os
import logging
from fastapi import Request
from fastapi import APIRouter, HTTPException, status
from app.models.youtube import YoutubeDownloadRequest, YoutubeDownloadResponse
from app.services.downloader import download_youtube_video

router = APIRouter(prefix="/youtube", tags=["youtube"])


@router.post("/download/", response_model=YoutubeDownloadResponse)
async def download_video(request: YoutubeDownloadRequest, fastapi_request: Request):
    try:
        video_path = await download_youtube_video(request.url)
        filename = os.path.basename(video_path)
        download_url = str(fastapi_request.base_url) + f"downloads/{filename}"
        return YoutubeDownloadResponse(success=True, message="Download successful", download_url=download_url)
    except ValueError as ve:
        logging.error(f"Invalid URL: {ve}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e:
        logging.error(f"Download failed: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Download failed")
