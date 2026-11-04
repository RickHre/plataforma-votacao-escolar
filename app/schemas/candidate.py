from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class CandidateCreate(BaseModel):
    fullname: str = Field(min_length=3, max_length=100)
    name: str = Field(min_length=3, max_length=100)
    number: int = Field(ge=0, le=999999)
    description: str | None = None

class CandidateRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    fullname: str
    name: str
    number: int
    description: str | None
    created_at: datetime
    updated_at: datetime

class CandidateUpdate(BaseModel):
    fullname: str | None = Field(default=None, min_length=3, max_length=100)
    name: str | None = Field(default=None, min_length=3, max_length=100)
    number: int | None = Field(default=None, ge=0, le=999999)
    description: str | None = Field(default=None, min_length=3)
