from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user import User
from app.schemas.user import UserCreate, UserRead, UserUpdate
from app.security import hash_password

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[UserRead], status_code=status.HTTP_201_CREATED)
def get_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    stmt = (
        select(User)
            .where(User.deleted_at.is_(None))
            .order_by(User.id)
            .offset(skip)
            .limit(limit)
    )
    return db.scalars(stmt).all()

@router.get("/{user_id}", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = db.get(User, user_id)
    if user is None or user.deleted_at is not None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")
    return user

@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    stmt = select(User.id).where(User.username == user.username)
    if db.scalar(stmt) is not None:
        raise HTTPException(status.HTTP_409_CONFLICT, detail="Usuário já cadastrado.")

    new_user = User(
        role=user.role,
        username=user.username,
        password=hash_password(user.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.patch("/{user_id}", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id)
    if db_user is None or db_user.deleted_at is not None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")

    # separar uma rota só para trocar a senha...

    data = user.model_dump(exclude_unset=True)
    for field, value in data.items():
        setattr(db_user, field, value)

    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.get(User, user_id)
    if db_user is None or db_user.deleted_at is not None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado.")
    db_user.deleted_at = datetime.now(timezone.utc)
    db.commit()
