from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import httpx

app = FastAPI()

@app.get("/api")
async def handle_download(url: str):
    # API trung gian lấy link không watermark
    api_endpoint = f"https://api.tiklydown.eu.org/api/download?url={url}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(api_endpoint)
            data = response.json()
            if data.get("status") == 200:
                # Trích xuất link video không watermark
                video_url = data["video"]["noWatermark"]
                return RedirectResponse(url=video_url)
        except Exception:
            pass
    return {"error": "Không lấy được link, thử link khác đi b!"}
    
