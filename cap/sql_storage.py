from datetime import datetime

from sqlalchemy.exc import IntegrityError

from cap.db import db_session
from cap.errors import ConflictError, NotFoundError
from cap.models import Balloons
from cap.schemas import CorrectBalloon


class BalloonsStorage():
    name = 'balloons'

    def add(self, balloon: CorrectBalloon) -> CorrectBalloon:
        entity = Balloons(
            firm=balloon.firm,
            paint_code=balloon.paint_code,
            color=balloon.color,
            volume=balloon.volume,
            weight=balloon.weight,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            acceptance_date=balloon.acceptance_date,
            project_id=balloon.project_id,
        )
        db_session.add(entity)
        try:
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name, f'reason: project id {balloon.project_id} not found')
        return CorrectBalloon.from_orm(entity)

    def delete(self, uid) -> None:
        entity = Balloons.query.filter(Balloons.uid == uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: balloon id {uid} not found')

        db_session.delete(entity)
        db_session.commit()

    def update(self, balloon: CorrectBalloon) -> CorrectBalloon:
        entity = Balloons.query.filter(Balloons.uid == balloon.uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: balloon id {balloon.uid} not found')

        entity.firm = balloon.firm
        entity.paint_code = balloon.paint_code
        entity.color = balloon.color
        entity.voluem = balloon.volume
        entity.weight = balloon.weight
        entity.updated_at = datetime.now()
        entity.project_id = balloon.project_id

        try:
            db_session.commit()
        except IntegrityError:
            raise ConflictError(self.name, f'reason: project id {balloon.project_id} not found')

        return CorrectBalloon.from_orm(entity)

    def get_balloon_by_id(self, uid) -> CorrectBalloon:
        entity = Balloons.query.filter(Balloons.uid == uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: balloon id {uid} not found')

        return CorrectBalloon.from_orm(entity)

    def get_all(self) -> list[CorrectBalloon]:
        return [CorrectBalloon.from_orm(entity) for entity in Balloons.query.all()]

    def get_free(self):
        balloons = Balloons.query.filter(Balloons.project_id.is_(None))
        return [CorrectBalloon.from_orm(entity) for entity in balloons]
