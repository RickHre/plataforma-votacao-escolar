from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.routes import schemas
from app.database import get_db
from app.routes.auth import get_current_user

router = APIRouter(prefix="/students", tags=["students"])

# Listar todos os alunos (somente professor)
@router.get("/", response_model=list[schemas.UserOut])
def list_students(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role.value != "professor":
        raise HTTPException(status_code=403, detail="Apenas professores podem listar alunos")

    return db.query(models.User).filter(models.User.role == "aluno").all()

# Detalhar um aluno específico (somente professor)
@router.get("/{student_id}", response_model=schemas.UserOut)
def get_student(student_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role.value != "professor":
        raise HTTPException(status_code=403, detail="Apenas professores podem consultar alunos")

    student = db.query(models.User).filter(models.User.id == student_id, models.User.role == "aluno").first()
    if not student:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return student