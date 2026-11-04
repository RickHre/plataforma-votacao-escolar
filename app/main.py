from fastapi import FastAPI

from app.database import Base, engine, init_db
from app import models
from app.routes import health
from app.routes.v1.router import api_router as api_v1_router

app = FastAPI(title="Plataforma de Votação Escolar")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(health.router)
app.include_router(api_v1_router, prefix="/api/v1")
