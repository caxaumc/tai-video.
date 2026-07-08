from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import httpx

app = FastAPI()

@app.get("/api")
async def handle_download(url: str):
    # API này lấy link từ TiklyDown và chuyển hướng trình duyệt tới file video
    api_url = f"https://api.tiklydown.eu.org/api/download?url={url}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_url)
            data = response.json()
            if data.get("status") == 200:
                # Lấy link video không watermark và redirect
                return RedirectResponse(url=data["video"]["noWatermark"])
        except Exception as e:
            return {"error": "Lỗi server: " + str(e)}
    return {"error": "Không tìm thấy video"}
    
