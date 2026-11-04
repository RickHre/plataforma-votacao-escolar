from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.auth import AuthLogin, AuthRegister, Token
from app.security import hash_password, verify_password, generate_token, decode_token

router = APIRouter(prefix="/auth", tags=["auth"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")

@router.post("/register", response_model=Token, status_code=status.HTTP_201_CREATED)
def register(data: AuthRegister, db: Session = Depends(get_db)):
    if db.query(User).filter(User.username == data.username).first():
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Usuário já cadastrado.")

    new_user = User(
        username=data.username,
        password=hash_password(data.password),
        role="student"
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return { "access_token": generate_token(new_user.id) } # implementar token jwt

@router.post("/login")
def login(user: AuthLogin, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username, User.deleted_at.is_(None)).first()
    if not db_user or not verify_password(user.password, db_user.password):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")
    return { "access_token": generate_token(db_user.id), }

@router.post("/refresh")
def refresh(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    user_id = decode_token(token)
    db_user = db.get(User, user_id)

    if user_id is None or db_user is None or db_user.deleted_at is not None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido ou expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )

    novo_token = gerar_token(usuario_id)
    return {"access_token": novo_token }
