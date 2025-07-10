import asyncio
import json
from fastapi import FastAPI, Request
import httpx

from fastapi.templating import Jinja2Templates
from sse_starlette import EventSourceResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("4-prep.html", {"request": request})


@app.get("/ai")
async def ai():
    async def event_stream():
        async with httpx.AsyncClient() as client:
            async with client.stream(
                "POST",
                "http://localhost:11434/api/generate",
                json={
                        "model": "llama3.2",
                        "prompt": "What is the capital of France?",
                        "stream": True,
                    },
            ) as resp:
                yield {"event": "message", "data": "Starting event stream<br>"}
                await asyncio.sleep(1)
                print(f"Status Code: {resp.status_code}\n")
                yield {"event": "status", "data": f"HTTP Status Code: {resp.status_code}<br>"}
                await asyncio.sleep(1)

                async for line in resp.aiter_lines():
                    if not line.strip():
                        continue
                    try:
                        data = json.loads(line)
                        # print(line)
                        chunk = data.get("response", "")
                        print(f"chunk: {repr(chunk)}")
                        await asyncio.sleep(0.3)
                        yield {"event": "message", "data": chunk}
                        # print(f"chunk: {chunk}")
                        if data.get("done"):
                            break
                    except json.JSONDecodeError:
                        print(f"Could not decode line: {line}")
        yield {"event": "message", "data": "<br> closing stream <br>"}
        await asyncio.sleep(1)
        yield {"event": "close", "data": ""}
    return EventSourceResponse(event_stream())
