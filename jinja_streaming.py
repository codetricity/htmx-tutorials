import asyncio
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sse_starlette.sse import EventSourceResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("jinja-streaming.html", {"request": request})


@app.get("/progress")
async def progress(request: Request) -> EventSourceResponse:
    async def event_stream():
        yield {"event": "message", "data": "starting connection"}
        await asyncio.sleep(1)
        for i in range(1, 10):
            yield {"event": "message", "data": f"receiving event {i}"}
            await asyncio.sleep(1)
    return EventSourceResponse(
        event_stream()
    )
