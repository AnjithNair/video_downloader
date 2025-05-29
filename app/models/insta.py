from pydantic import BaseModel, validator
from typing import Optional

class InstaDownloadRequest(BaseModel):
    url: str

    @validator('url')
    def validate_url(cls, url):
        if not url.startswith('https://www.instagram.com/reel/'):
            raise ValueError('URL must be a valid Instagram Reels link')
        return url

class InstaDownloadResponse(BaseModel):
    success: bool
    message: str
    file_path: Optional[str] = None
