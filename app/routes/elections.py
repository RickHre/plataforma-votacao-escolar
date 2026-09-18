from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.routes import schemas
from app.database import get_db
from app.routes.auth import get_current_user

router = APIRouter(prefix="/elections", tags=["elections"])

@router.post("/", response_model=schemas.ElectionOut)
def create_election(election: schemas.ElectionCreate, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role.value != "professor":
        raise HTTPException(status_code=403, detail="Apenas professores podem criar eleições")

    db_election = models.Election(title=election.title, created_by=current_user.id)
    db.add(db_election)
    db.commit()
    db.refresh(db_election)
    return db_election

@router.get("/", response_model=list[schemas.ElectionOut])
def list_elections(db: Session = Depends(get_db)):
    return db.query(models.Election).all()