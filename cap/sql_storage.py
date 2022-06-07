from typing import List
from cap.factory import BalloonStorage
from cap.errors import NotFoundError
from cap.schemas import CorrectBalloon
from datetime import datetime

from cap.models import Balloons
from cap.db import db_session



class SQLBalloonsStorage(BalloonStorage):
    name = 'balloons'


    def add(self, balloon: CorrectBalloon) -> Balloons:
        entity = Balloons(
            firm = balloon.firm,
            paint_code = balloon.paint_code,
            color = balloon.color,
            volume = balloon.volume,
            weight = balloon.weight,
            created_at = datetime.now(),
            updated_at = datetime.now(),
            acceptance_date = balloon.acceptance_date,
        )
        db_session.add(entity)
        db_session.commit()
        return entity


    def delete(self, uid):
        entity = Balloons.query.filter(Balloons.uid == uid).first()
        if not entity:
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        db_session.delete(entity)
        db_session.commit()


    def update(self, balloon: CorrectBalloon) -> Balloons:
        entity = Balloons.query.filter(Balloons.uid == balloon.uid).first()
        if not entity:
            raise NotFoundError(self.name, f"reason: balloon id {balloon.uid} not found")
        entity.firm = balloon.firm,
        entity.paint_code = balloon.paint_code,
        entity.color = balloon.color,
        entity.voluem = balloon.volume,
        entity.weight = balloon.weight,
        entity.updated_at = datetime.now(),
        db_session.commit()
        return entity


    def get_balloon_by_id(self, uid):
        entity = Balloons.query.filter(Balloons.uid == uid).first()
        if not entity:
            raise NotFoundError(self.name, f"reason: balloon id {uid} not found")
        return entity


    def get_all(self) -> List[Balloons]:
        return Balloons.query.all()