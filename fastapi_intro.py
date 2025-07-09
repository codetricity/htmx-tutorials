from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def home():
    return """
        <html>
        <head>
            <script src="https://cdn.tailwindcss.com?plugins=typography"></script>
        
        </head>
        <body class="prose p-6">
        <h1>Welcome to the story of birds</h1>
        <img src="https://cdn.pixabay.com/photo/2018/05/01/17/30/adler-3366239_1280.jpg">
        </body>
        </html>
        """
