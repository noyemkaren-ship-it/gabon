from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def main(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/index.html")
def gabon(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/armenia.html")
def armenia(request: Request):
    return templates.TemplateResponse("armenia.html", {"request": request})

@app.get("/rusha.html")
def rusha(request: Request):
    return templates.TemplateResponse("rusha.html", {"request": request})

@app.get("/american.html")
def america(request: Request):
    return templates.TemplateResponse("american.html", {"request": request})

@app.get("/indi.html")
def indi(request: Request):
    return templates.TemplateResponse("indi.html", {"request": request})

@app.get("/city.html")
def city(request: Request):
    return templates.TemplateResponse("city.html", {"request": request})

@app.get("/phil.html")
def phil(request: Request):
    return templates.TemplateResponse("phil.html", {"request": request})