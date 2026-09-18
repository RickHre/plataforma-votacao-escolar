from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.routes import schemas
from app.database import get_db
from app.routes.auth import get_current_user

router = APIRouter(prefix="/candidates", tags=["candidates"])

@router.post("/", response_model=schemas.CandidateOut)
def create_candidate(candidate: schemas.CandidateCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role.value != "professor":
        raise HTTPException(status_code=403, detail="Apenas professores podem cadastrar candidatos")

    db_candidate = models.Candidate(
        name=candidate.name,
        turma=candidate.turma,
        created_by=current_user.id
    )
    db.add(db_candidate)
    db.commit()
    db.refresh(db_candidate)
    return db_candidate

@router.get("/", response_model=list[schemas.CandidateOut])
def list_candidates(db: Session = Depends(get_db)):
    return db.query(models.Candidate).all()