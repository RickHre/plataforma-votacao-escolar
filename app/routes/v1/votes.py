from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select, func
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.vote import Vote
from app.models.election import Election
from app.models.candidate import Candidate
from app.schemas.vote import VoteCreate, VoteRead

router = APIRouter(prefix="/votes", tags=["votes"])

@router.get("/", response_model=list[VoteRead])
def get_votes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stmt = (
        select(Vote)
            .order_by(Vote.id)
            .offset(skip)
            .limit(limit)
    )
    return db.scalars(stmt).all()

@router.get("/{vote_id}", response_model=VoteRead)
def get_vote_by_id(vote_id: int, db: Session = Depends(get_db)):
    vote = db.get(Vote, vote_id)
    if vote is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Voto não encontrado.")
    return vote

@router.get("/user/{user_id}", response_model=list[VoteRead])
def get_vote_by_user_id(user_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stmt = (
        select(Vote)
            .where(Vote.user_id == user_id)
            .order_by(Vote.id)
            .offset(skip)
            .limit(limit)
    )
    return db.scalars(stmt).all()

@router.get("/candidate/{candidate_id}", response_model=list[VoteRead])
def get_vote_by_candidate_id(candidate_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stmt = (
        select(Vote)
            .where(Vote.candidate_id == candidate_id)
            .order_by(Vote.id)
            .offset(skip)
            .limit(limit)
    )
    return db.scalars(stmt).all()

@router.get("/election/{election_id}", response_model=list[VoteRead])
def get_vote_by_election_id(election_id: int, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stmt = (
        select(Vote)
            .where(Vote.election_id == election_id)
            .order_by(Vote.id)
            .offset(skip)
            .limit(limit)
    )
    return db.scalars(stmt).all()

@router.post("/", response_model=VoteRead, status_code=status.HTTP_201_CREATED)
def create_vote(vote: VoteCreate, db: Session = Depends(get_db)):
    election = db.get(Election, vote.election_id)
    if election is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Eleição não encontrada.")

    if not (election.starts_at <= datetime.now(timezone.utc).replace(tzinfo=None) <= election.ends_at):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Eleição fora do período de votação.")

    if vote.candidate_id is not None:
        candidate = db.get(Candidate, vote.candidate_id)
        if candidate is None or candidate.deleted_at is not None:
            raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Candidato não encontrado.")

    new_vote = Vote(
        election_id=vote.election_id,
        user_id=vote.user_id,
        candidate_id=vote.candidate_id,
    )
    db.add(new_vote)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Você já votou neste eleição.")

    db.refresh(new_vote)
    return new_vote
