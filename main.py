from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import httpx

app = FastAPI()

# API này nhận link từ web của b, sau đó tự điều hướng đến link tải trực tiếp
@app.get("/api")
async def handle_download(url: str):
    # Sử dụng API trung gian ổn định để lấy link no-watermark
    api_endpoint = f"https://api.tiklydown.eu.org/api/download?url={url}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api_endpoint)
        data = response.json()
        if data.get("status") == 200:
            return RedirectResponse(url=data["video"]["noWatermark"])
    return {"error": "Không lấy được link"}
    
