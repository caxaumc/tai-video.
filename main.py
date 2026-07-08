from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp

app = FastAPI()

# BẬT TÍNH NĂNG MỞ KHÓA CORS CHO VERCEL KẾT NỐI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cho phép tất cả các trang web (bao gồm Vercel của bạn) gọi tới
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class VideoRequest(BaseModel):
    url: str

@app.get("/")
def read_root():
    return {"message": "Server Python dang chay ngon lanh!"}

@app.post("/get-video")
def get_video(request: VideoRequest):
    video_url = request.url
    if not video_url:
        raise HTTPException(status_code=400, detail="Thieu link video roi ban oi!")
        
    ydl_opts = {
        'format': 'best',
        'quiet': True,
        'no_warnings': True,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            return {
                "success": True,
                "title": info.get('title', 'Video No Title'),
                "download_url": info.get('url')
            }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
        
