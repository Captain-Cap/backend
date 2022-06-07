from datetime import datetime
from typing import Optional
from pydantic import BaseModel, conint


class CorrectBalloon(BaseModel):

    uid: Optional[conint(gt=0)]
    firm: str
    paint_code: str
    color: str
    volume: int
    weight: conint(gt=0)
    acceptance_date: datetime

    class Config:
        orm_mode = True