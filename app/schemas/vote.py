from typing import Literal
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class VoteCreate(BaseModel):
    election_id: int
    user_id: int
    candidate_id: int | None = None

class VoteRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    election_id: int
    user_id: int
    candidate_id: int | None
    created_at: datetime
