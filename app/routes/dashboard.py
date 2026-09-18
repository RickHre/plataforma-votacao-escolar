from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models
from app.routes import schemas
from app.database import get_db
from app.routes.auth import get_current_user

router = APIRouter(prefix="/dashboard", tags=["dashboard"])

@router.get("/")
def dashboard_overview(db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    if current_user.role.value != "professor":
        raise HTTPException(status_code=403, detail="Apenas professores podem acessar o dashboard")

    # Total de alunos
    total_alunos = db.query(models.User).filter(models.User.role == "aluno").count()

    # Total de candidatos
    total_candidatos = db.query(models.Candidate).count()

    # Total de eleições
    total_eleicoes = db.query(models.Election).count()

    # Votos por eleição
    eleicoes = db.query(models.Election).all()
    resultados = []
    for e in eleicoes:
        votos = db.query(models.Vote).filter(models.Vote.election_id == e.id).count()
        resultados.append({
            "eleicao": e.title,
            "status": e.status.value,
            "total_votos": votos
        })

    return {
        "professor": current_user.username,
        "total_alunos": total_alunos,
        "total_candidatos": total_candidatos,
        "total_eleicoes": total_eleicoes,
        "resultados": resultados
    }