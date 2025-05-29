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
        file_paths = await download_youtube_video(request.url, request.quality)
        if request.quality == 'all':
            download_urls = [str(fastapi_request.base_url) + f"downloads/{os.path.basename(fp)}" for fp in file_paths]
            return YoutubeDownloadResponse(success=True, message="All qualities downloaded", download_url=download_urls)
        else:
            filename = os.path.basename(file_paths[0]) if file_paths else None
            download_url = str(fastapi_request.base_url) + f"downloads/{filename}" if filename else None
            return YoutubeDownloadResponse(success=True, message="Download successful", download_url=download_url)
    except ValueError as ve:
        logging.error(f"Invalid URL: {ve}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(ve))
    except Exception as e:
        logging.error(f"Download failed: {e}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Download failed")
