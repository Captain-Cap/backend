from datetime import datetime

from pydantic import BaseModel, PositiveInt


class CorrectBalloon(BaseModel):

    uid: int
    firm: str
    paint_code: str
    color: str
    volume: int
    weight: PositiveInt
    acceptance_date: datetime
    project: str

    class Config:
        orm_mode = True


class Project(BaseModel):

    uid: int
    name: str
    created_at: datetime

    class Config:
        orm_mode = True
