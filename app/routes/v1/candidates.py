from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.candidate import Candidate
from app.schemas.candidate import CandidateCreate, CandidateRead, CandidateUpdate

router = APIRouter(prefix="/candidates", tags=["candidates"])

@router.get("/", response_model=list[CandidateRead], status_code=status.HTTP_201_CREATED)
def get_candidates(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stmt = (
        select(Candidate)
            .where(Candidate.deleted_at.is_(None))
            .order_by(Candidate.id)
            .offset(skip)
            .limit(limit)
    )
    return db.scalars(stmt).all()

@router.get("/{candidate_id}", response_model=CandidateRead, status_code=status.HTTP_201_CREATED)
def get_candidate_by_id(candidate_id: int, db: Session = Depends(get_db)):
    candidate = db.get(Candidate, candidate_id)
    if candidate is None or candidate.deleted_at is not None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Candidato não encontrado.")
    return candidate

@router.post("/", response_model=CandidateRead, status_code=status.HTTP_201_CREATED)
def create_candidate(candidate: CandidateCreate, db: Session = Depends(get_db)):
    stmt = select(Candidate.id).where(Candidate.number == candidate.number)
    if db.scalar(stmt) is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Número do candidato já usado.")

    new_candidate = Candidate(
        fullname=candidate.fullname,
        name=candidate.name,
        number=candidate.number,
        description=candidate.description,
    )
    db.add(new_candidate)
    db.commit()
    db.refresh(new_candidate)
    return new_candidate

@router.patch("/{candidate_id}", response_model=CandidateRead, status_code=status.HTTP_201_CREATED)
def update_candidate(candidate_id: int, candidate: CandidateUpdate, db: Session = Depends(get_db)):
    db_candidate = db.get(Candidate, candidate_id)
    if db_candidate is None or db_candidate.deleted_at is not None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")

    data = candidate.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(db_candidate, field, value)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Número do candidato já usado.")

    db.refresh(db_candidate)
    return db_candidate

@router.delete("/{candidate_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_candidate(candidate_id: int, db: Session = Depends(get_db)):
    db_candidate = db.get(Candidate, candidate_id)
    if db_candidate is None or db_candidate.deleted_at is not None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")
    db_candidate.deleted_at = datetime.now(timezone.utc)
    db.commit()
