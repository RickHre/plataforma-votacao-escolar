from fastapi import FastAPI
from app.database import Base, engine
from app import models
from app.routes import auth, students, candidates, votes, dashboard, elections, view

# Cria todas as tabelas definidas em models.py
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(students.router)
app.include_router(candidates.router)
app.include_router(votes.router)
app.include_router(dashboard.router)
app.include_router(elections.router)
app.include_router(view.router)
