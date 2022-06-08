from datetime import datetime
from typing import Optional

from pydantic import BaseModel, PositiveInt


class CorrectBalloon(BaseModel):

    uid: Optional[PositiveInt]
    firm: str
    paint_code: str
    color: str
    volume: int
    weight: PositiveInt
    acceptance_date: datetime

    class Config:
        orm_mode = True
