from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, model_validator

class ElectionCreate(BaseModel):
    title: str = Field(min_length=4, max_length=100)
    starts_at: datetime
    ends_at: datetime

    @model_validator(mode="after")
    def check_dates(self):
        if self.ends_at <= self.starts_at:
            raise ValueError("ends_at deve ser mair que starts_at")
        return self

class ElectionRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    starts_at: datetime
    ends_at: datetime
