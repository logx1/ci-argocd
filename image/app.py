from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return """
    <html>
      <head>
        <style>
          h1 {
            color: #3498db;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 50px;
          }
          body {
            background: #f4f4f4;
          }
        </style>
      </head>
      <body>
        <h1>Welcome this is version 1</h1>
      </body>
    </html>
    """