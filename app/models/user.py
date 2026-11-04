from sqlalchemy import Column, Integer, String

from app.database import Base
from app.models.mixins import TimestampMixin, SoftDeleteMixin

class User(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    role = Column(String, nullable=False) 
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    # Dados opcionais para 
    birth_date = Column(String, nullable=True)
    cep = Column(String, nullable=True)

