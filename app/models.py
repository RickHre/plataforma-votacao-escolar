from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum
from sqlalchemy.orm import relationship
from app.database import Base
import enum
from datetime import datetime

# Definição de papéis
class UserRole(enum.Enum):
    aluno = "aluno"
    professor = "professor"

class ElectionStatus(enum.Enum):
    aberta = "aberta"
    fechada = "fechada"

# Usuários
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password_hash = Column(String, nullable=False)
    role = Column(Enum(UserRole), nullable=False)

    votes = relationship("Vote", back_populates="user")

# Candidatos
class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    turma = Column(String, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id"))

    votes = relationship("Vote", back_populates="candidate")

# Eleições
class Election(Base):
    __tablename__ = "elections"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    status = Column(Enum(ElectionStatus), default=ElectionStatus.aberta)
    created_by = Column(Integer, ForeignKey("users.id"))

    votes = relationship("Vote", back_populates="election")

# Votos
class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    candidate_id = Column(Integer, ForeignKey("candidates.id"))
    election_id = Column(Integer, ForeignKey("elections.id"))
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="votes")
    candidate = relationship("Candidate", back_populates="votes")
    election = relationship("Election", back_populates="votes")