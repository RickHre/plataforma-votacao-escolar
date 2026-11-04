from typing import Literal
from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

class Token(BaseModel):
    access_token: str

class AuthLogin(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=4, max_length=128)

class AuthRegister(BaseModel):
    username: str = Field(min_length=3, max_length=100)
    password: str = Field(min_length=4, max_length=128)
