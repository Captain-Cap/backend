from datetime import datetime

from cap.db import db_session
from cap.errors import NotFoundError
from cap.models import Balloons, Project
from cap.schemas import CorrectBalloon


class BalloonsStorage():
    name = 'balloons'

    def add(self, balloon: CorrectBalloon) -> CorrectBalloon:
        entity = Project.query.filter(Project.uid == balloon.id_project).first()
        if not entity:
            raise NotFoundError(self.name, f'reaseon: project id {balloon.id_project} not found')

        entity = Balloons(
            firm=balloon.firm,
            paint_code=balloon.paint_code,
            color=balloon.color,
            volume=balloon.volume,
            weight=balloon.weight,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            acceptance_date=balloon.acceptance_date,
            id_project=balloon.id_project,
        )
        db_session.add(entity)
        db_session.commit()
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

        entity_project = Project.query.filter(Project.uid == balloon.id_project).first()
        if not entity_project:
            raise NotFoundError(self.name, f'reaseon: project id {balloon.id_project} not found')

        entity.firm = balloon.firm
        entity.paint_code = balloon.paint_code
        entity.color = balloon.color
        entity.voluem = balloon.volume
        entity.weight = balloon.weight
        entity.updated_at = datetime.now()
        entity.project = balloon.id_project

        db_session.commit()
        return CorrectBalloon.from_orm(entity)

    def get_balloon_by_id(self, uid) -> CorrectBalloon:
        entity = Balloons.query.filter(Balloons.uid == uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: balloon id {uid} not found')

        return CorrectBalloon.from_orm(entity)

    def get_all(self) -> list[CorrectBalloon]:
        return [CorrectBalloon.from_orm(entity) for entity in Balloons.query.all()]

    def get_balloons_by_name_project(self, uid) -> list[CorrectBalloon]:
        balloons = Balloons.query.filter(Balloons.id_project == uid)
        return [CorrectBalloon.from_orm(entity) for entity in balloons]
