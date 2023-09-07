import os

import openai
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

import melody_generator
from api import steps, snapshots

app = FastAPI(
    title="Music Craft AI",
    description="Esta es una API de composición musical",
    version="1.0.0",
)

templates = Jinja2Templates(directory="templates")

openai.api_key = os.getenv("OPENAI_API_KEY")

app.include_router(steps.router, prefix="/steps", tags=["steps"])
app.include_router(snapshots.router, prefix="/snapshots", tags=["snapshots"])


@app.get("/")
def index(request: Request):
    if request.method == "POST":
        melody, scale, mode, description = melody_generator.get_results()
        result = f"""
                    Escala: {scale}      <br>
                    Modo: {mode}           <br>
                    Melodia: {melody}           <br>
                    Descripción: {description} <br>
                """
        return RedirectResponse(url=f"/?result={result}")

    query_params = request.query_params
    print(f"query_params: {query_params}")

    query_params_dict = dict(query_params)
    result = query_params_dict.get("result", "")
    return templates.TemplateResponse("index.html", {"request": request, "result": result})
