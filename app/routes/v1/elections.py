from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.election import Election
from app.schemas.election import ElectionCreate, ElectionRead

router = APIRouter(prefix="/elections", tags=["elections"])

@router.get("/", response_model=list[ElectionRead])
def get_elections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stmt = (
        select(Election)
            .order_by(Election.id)
            .offset(skip)
            .limit(limit)
    )
    return db.scalars(stmt).all()

@router.get("/{election_id}", response_model=ElectionRead)
def get_election_by_id(election_id: int, db: Session = Depends(get_db)):
    election = db.get(Election, election_id)
    if election is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Eleição não encontrada.")
    return election

@router.post("/", response_model=ElectionRead, status_code=status.HTTP_201_CREATED)
def create_election(election: ElectionCreate, db: Session = Depends(get_db)):
    stmt = select(Election.id).where(Election.title == election.title)
    if db.scalar(stmt) is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Eleição já cadastrada.")

    new_election = Election(
        title=election.title,
        starts_at=election.starts_at,
        ends_at=election.ends_at,
    )
    db.add(new_election)
    db.commit()
    db.refresh(new_election)
    return new_election
