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
    return templates.TemplateResponse("4-solution.html", {"request": request})


@app.get("/ai")
async def ai():
    async def event_stream():
        async with httpx.AsyncClient() as client:
            async with client.stream(
                "POST",
                "http://localhost:11434/api/generate",
                json={
                        "model": "llama3.2",
                        "prompt": """
                                Write a 50 world story about a heroic barn owl and a
                                hockey player named Jesse Casman, president of Oppkey.
                                """
                }
            ) as resp:
                yield {"event": "message", "data": "Starting event stream<br>"}
                await asyncio.sleep(1)
                print(f"Status Code: {resp.status_code}")
                await asyncio.sleep(1)

                yield {"event": "status", "data": f"Status Code: {resp.status_code}<br>"}
                await asyncio.sleep(1)
                yield {"event": "message", "data": "<br><img width='200px' src='https://oppkey.github.io/assets/img/oppkey/people/jesse_hockey.webp'><br>"}
                yield {"event": "message", "data": "<img width='300px' src='https://cdn.pixabay.com/photo/2015/12/25/06/32/barn-owl-1107397_1280.jpg'>"}
                async for line in resp.aiter_lines():
                    # print(line)
                    if not line.strip():
                        continue
                    try:
                        data = json.loads(line)
                        chunk = data.get("response", "")
                        await asyncio.sleep(0.3)
                        print(f"chunk: {repr(chunk)}")
                        yield {"event": "message", "data": chunk}
                        if data.get("done"):
                            break

                    except json.JSONDecodeError:
                        print(f"Could not decode line: {line}")
        await asyncio.sleep(1)
        yield {"event": "close", "data": ""}

    return EventSourceResponse(event_stream())
