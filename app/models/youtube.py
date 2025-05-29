from pydantic import BaseModel, field_validator
from typing import Optional

class YoutubeDownloadRequest(BaseModel):
    url: str

    @field_validator('url')
    def validate_url(cls, url):
        if not (url.startswith("https://www.youtube.com/") or url.startswith("https://youtu.be/")):
            raise ValueError('URL must be a valid YouTube video link')
        return url

class YoutubeDownloadResponse(BaseModel):
    success: bool
    message: str
    download_url: Optional[str] = None
