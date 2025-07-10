import asyncio
from fastapi import FastAPI, Request
import httpx

from fastapi.templating import Jinja2Templates
from sse_starlette import EventSourceResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("llm-connect.html", {"request": request})


@app.get("/ai")
async def ai():
    async def event_stream():
        async with httpx.AsyncClient() as client:
            resp = await client.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": "llama3.2",
                    "prompt": "What is the capital of France?"
                }
            )
            yield {"event": "message", "data": "Starting event stream"}
            await asyncio.sleep(1)
            print(f"Status Code: {resp.status_code}")
            await asyncio.sleep(1)

            yield {"event": "status", "data": f"Status Code: {resp.status_code}"}
            await asyncio.sleep(1)
            print(resp.text)
            yield {"event": "message", "data": resp.text}
            await asyncio.sleep(1)
            yield {"event": "close", "data": ""}

    return EventSourceResponse(event_stream())
