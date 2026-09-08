from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from app.database import SessionLocal
from app import models

router = APIRouter(prefix="/auth", tags=["auth"])

# Dependência para obter sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Modelo Pydantic para entrada
class UserCreate(BaseModel):
    username: str
    password: str
    role: str  # "professor" ou "aluno"

@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Verifica se já existe
    existing_user = db.query(models.User).filter(models.User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    new_user = models.User(
        username=user.username,
        password=user.password,  # depois vamos aplicar hash
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "Usuário cadastrado com sucesso", "user": new_user.username}

@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return {"message": "Login realizado com sucesso", "role": db_user.role}