from pydantic import BaseModel, field_validator
from typing import Optional

class TiktokDownloadRequest(BaseModel):
    url: str

    @field_validator('url')
    def validate_url(cls, url):
        if not (url.startswith("https://www.tiktok.com/") or "tiktok.com/@" in url):
            raise ValueError('URL must be a valid TikTok video link')
        return url

class TiktokDownloadResponse(BaseModel):
    success: bool
    message: str
    download_url: Optional[str] = None
