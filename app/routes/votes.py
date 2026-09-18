from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.routes import schemas
from app.database import get_db
from app.routes.auth import get_current_user
from datetime import datetime
from sqlalchemy import func

router = APIRouter(prefix="/votes", tags=["votes"])

# Registrar voto (somente aluno)
@router.post("/submit")
def submit_vote(candidate_id: int, election_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role.value != "aluno":
        raise HTTPException(status_code=403, detail="Apenas alunos podem votar")

    # Verifica se eleição existe e está aberta
    election = db.query(models.Election).filter(models.Election.id == election_id).first()
    if not election or election.status != models.ElectionStatus.aberta:
        raise HTTPException(status_code=400, detail="Eleição inválida ou já encerrada")

    # Verifica se aluno já votou nessa eleição
    existing_vote = db.query(models.Vote).filter(
        models.Vote.user_id == current_user.id,
        models.Vote.election_id == election_id
    ).first()
    if existing_vote:
        raise HTTPException(status_code=400, detail="Você já votou nesta eleição")

    # Registra voto
    vote = models.Vote(
        user_id=current_user.id,
        candidate_id=candidate_id,
        election_id=election_id,
        timestamp=datetime.utcnow()
    )
    db.add(vote)
    db.commit()
    db.refresh(vote)
    return {"message": "Voto registrado com sucesso"}

# Apuração de votos (somente professor)
@router.get("/results/{election_id}")
def get_results(election_id: int, db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role.value != "professor":
        raise HTTPException(status_code=403, detail="Apenas professores podem consultar resultados")

    election = db.query(models.Election).filter(models.Election.id == election_id).first()
    if not election:
        raise HTTPException(status_code=404, detail="Eleição não encontrada")

    # Conta votos por candidato
    query_results = (
        db.query(
            models.Candidate.name,
            func.count(models.Vote.id).label("total_votos")
        )
        .join(models.Vote, models.Vote.candidate_id == models.Candidate.id)
        .filter(models.Vote.election_id == election_id)
        .group_by(models.Candidate.name)
        .all()
    )

    # Converte para lista de dicts
    results = [{"name": r[0], "total_votos": r[1]} for r in query_results]

    return {
        "election": election.title,
        "status": election.status.value,
        "results": results
    }