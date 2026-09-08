from fastapi import FastAPI
from app.database import Base, engine
from app.routes import auth

app = FastAPI(title="Plataforma de Votação Escolar")

# Cria as tabelas no SQLite
Base.metadata.create_all(bind=engine)

app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "MVP da Plataforma de Votação Escolar iniciado!"}