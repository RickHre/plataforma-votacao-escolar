from pydantic import BaseModel
from typing import List

# Usuários
class UserCreate(BaseModel):
    username: str
    password: str
    role: str

class UserOut(BaseModel):
    id: int
    username: str
    role: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

# Candidatos
class CandidateCreate(BaseModel):
    name: str
    turma: str

class CandidateOut(BaseModel):
    id: int
    name: str
    turma: str
    class Config:
        orm_mode = True

class ElectionCreate(BaseModel):
    title : str

class ElectionOut(BaseModel):
    id: int
    title : str
    status : str
    created_by : int

    class Config:
        from_attributes = True  # substitui orm_mode no Pydantic v2