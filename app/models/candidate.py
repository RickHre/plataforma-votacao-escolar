from sqlalchemy import Column, Integer, String

from app.database import Base
from app.models.mixins import TimestampMixin, SoftDeleteMixin

class Candidate(Base, TimestampMixin, SoftDeleteMixin):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, nullable=False)
    name = Column(String, nullable=False)
    number = Column(Integer, unique=True)
    description = Column(String, nullable=True)
