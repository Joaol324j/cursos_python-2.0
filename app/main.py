from fastapi import FastAPI, Depends, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from app import crud, schemas
from app.database import get_db
from starlette.requests import Request
from app.models import Base
from app.database import engine
from app.routes import courses

Base.metadata.create_all(bind=engine)

app = FastAPI(debug=True)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)

app.include_router(courses.router, prefix="/cursos", tags=["Cursos"])

templates = Jinja2Templates(directory="app/templates")

@app.get("/")
async def read_root(request: Request, db: Session = Depends(get_db)):
    try:
        cursos = crud.get_items(db)
        return templates.TemplateResponse("index.html", {"request": request, "todo_list": cursos})
    except Exception as e:
        return templates.TemplateResponse(
            "index.html",
            {"request": request, "todo_list": [], "error": "Erro ao buscar cursos."}
        )
