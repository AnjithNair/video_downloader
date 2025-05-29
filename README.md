# Instagram Reel Downloader API

A FastAPI-based service to download Instagram Reels videos via a simple POST endpoint.

## Setup Instructions

1. **Clone the repository** (if needed):

   ```bash
   git clone <repo-url>
   cd video_downloader
   ```

2. **Create and activate a virtual environment:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the API:**
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

- **Endpoint:** `POST /insta/download/`
- **Request Body:**
  ```json
  {
    "url": "https://www.instagram.com/reel/REEL_ID/"
  }
  ```
- **Response:**
  - `success`: true/false
  - `message`: status message
  - `download_url`: static file download url (if successful)


- **Endpoint:** `POST /youtube/download/`
- **Request Body:**
  ```json
  {
    "url": "https://youtu.be/VIDEO_ID/"
  }
  ```
- **Response:**
  - `success`: true/false
  - `message`: status message
  - `download_url`: static file download url (if successful)




## Project Structure

- `app/` - Main application code
  - `routers/` - API endpoints
  - `services/` - logic
  - `models/` - Pydantic models
- `requirements.txt` - Dependencies
- `README.md` - Instructions
