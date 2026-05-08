#Criar um sistema SSR 

from fastapi import FastAPI , Depends , Request , Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

app = FastAPI(title = "Sistema de login simples")

# Rodar esse codigo:
# python -m uvicorn main:app --reload

templates = Jinja2Templates(directory = "templates")

#Rota - metodo HTTP (get , post)

#Tela de cadastro
@app.get("/cadastro")
def tela_cadastro(request:Request):
    return templates.TemplateResponse(
        request,
        "cadastro.html",
        {"request": request}
    )
#Tela de login
@app.get("/login")
def tela_login(request: Request):
     return templates.TemplateResponse(
        request,
        "login.html",
        {"request": request}
    )
@app.get("/")
def tela_login(request: Request):
     return templates.TemplateResponse(
        request,
        "inicio.html",
        {"request": request}
    )

    
