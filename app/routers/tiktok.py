import os
import logging
from fastapi import Request, APIRouter, HTTPException, status
from app.models.tiktok import TiktokDownloadRequest, TiktokDownloadResponse
from app.services.downloader import download_tiktok_video

router = APIRouter(prefix="/tiktok", tags=["TikTok"])

@router.post("/download/", response_model=TiktokDownloadResponse)
async def download_tiktok(request: TiktokDownloadRequest, fastapi_request: Request):
    try:
        video_path = await download_tiktok_video(request.url)
        filename = os.path.basename(video_path)
        download_url = str(fastapi_request.base_url) + f"downloads/{filename}"
        return TiktokDownloadResponse(success=True, message="Download successful", download_url=download_url)
    except ValueError as ve:
        logging.error(f"Invalid URL: {ve}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e:
        logging.error(f"Download failed: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Download failed")
