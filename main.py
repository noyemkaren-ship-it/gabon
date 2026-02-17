from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from database import add_user, get_all_users, delete_user

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
async def main(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get("/ph.html")
async def main(request: Request):
    return templates.TemplateResponse("ph.html", {"request": request})

@app.get("/index.html")
async def gabon(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/armenia.html")
async def armenia(request: Request):
    return templates.TemplateResponse("armenia.html", {"request": request})

@app.get("/rusha.html")
async def rusha(request: Request):
    return templates.TemplateResponse("rusha.html", {"request": request})

@app.get("/american.html")
async def america(request: Request):
    return templates.TemplateResponse("american.html", {"request": request})

@app.get("/indi.html")
async def indi(request: Request):
    return templates.TemplateResponse("indi.html", {"request": request})

@app.get("/city.html")
async def city(request: Request):
    return templates.TemplateResponse("city.html", {"request": request})

@app.get("/phil.html")
async def phil(request: Request):
    return templates.TemplateResponse("phil.html", {"request": request})

@app.get("/sh.html")
async def sh(request: Request):
    return templates.TemplateResponse("sh.html", {"request": request})

@app.get("/currencies.html")
async def curr(request: Request):
    return templates.TemplateResponse("currencies.html", {"request": request})

@app.get("/create.html")
async def create_page(request: Request):
    return templates.TemplateResponse("create.html", {"request": request})

@app.post("/add-photo")
async def add_photo(image_url: str = Form(...)):
    all_photos = get_all_users()
    new_id = 1
    if all_photos:
        new_id = max(p['id'] for p in all_photos) + 1
    add_user(new_id, image_url)
    return RedirectResponse(url="/instagram.html", status_code=303)

@app.get("/instagram.html")
async def insta(request: Request):
    all_photos = get_all_users()
    return templates.TemplateResponse("instagram.html", {"request": request, "photos": all_photos})

@app.get("/delete/{id}")
async def dele(user_id: int):
    delete_user(user_id)
    return RedirectResponse(url="/instagram.html", status_code=303)

@app.get("/Запрос_на_создания_фото_автору_нажмите_try_it_out:_затем_execute", tags=["Запос_Автору_на_добавления_фото_в_2_основные_категории"], summary="Добавить фото в категории девочки/мальчики")
def giter(photo_url: str, categoria: str):
    print("Запрос на создания")
    print(f"фото{photo_url}, категория{categoria}")
    return {"message": "Ваш запрос обрабатывается!"}