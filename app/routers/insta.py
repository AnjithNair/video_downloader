from fastapi import APIRouter, HTTPException, status
from app.models.insta import InstaDownloadRequest, InstaDownloadResponse
from app.services.downloader import download_instagram_reel
import logging

router = APIRouter(prefix="/insta", tags=["Instagram"])

@router.post("/download/", response_model=InstaDownloadResponse)
async def download_reel(request: InstaDownloadRequest):
    try:
        video_path = await download_instagram_reel(request.url)
        return InstaDownloadResponse(success=True, message="Download successful", file_path=video_path)
    except ValueError as ve:
        logging.error(f"Invalid URL: {ve}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e:
        logging.error(f"Download failed: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Download failed")
