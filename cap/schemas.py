from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class CorrectBalloon(BaseModel):

    uid: int
    firm: str
    paint_code: str
    color: str
    volume: int
    weight: PositiveInt
    acceptance_date: datetime
    project_id: Optional[int]

    class Config:
        orm_mode = True


class Project(BaseModel):

    uid: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True
