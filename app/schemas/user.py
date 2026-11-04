from typing import Literal
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class UserCreate(BaseModel):
    role: str = Field()
    username: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=4, max_length=128)

class UserRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    role: Literal["teacher", "student"]
    username: str
    created_at: datetime
    updated_at: datetime

class UserUpdate(BaseModel):
    role: str = Field(default=None)
    username: str = Field(default=None, min_length=3, max_length=100)
    password: str = Field(default=None, min_length=4, max_length=128)
