from sqlalchemy import Column, Integer, DateTime, func

from app.database import Base

class Vote(Base):
    __tablename__ = "votes"

    id = Column(Integer, primary_key=True, index=True)
    election_id = Column(Integer, nullable=False)
    user_id = Column(Integer, nullable=False)
    candidate_id = Column(Integer, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
