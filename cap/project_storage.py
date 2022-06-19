from datetime import datetime

from cap.db import db_session
from cap.errors import NotFoundError
from cap.models import Project
from cap.schemas import CorrectProject


class ProjectStorage():
    name = 'project'

    def add(self, project: CorrectProject) -> CorrectProject:
        entity = Project(
            uid=project.uid,
            name=project.name,
            created_at=datetime.now(),
        )
        db_session.add(entity)
        db_session.commit()
        return CorrectProject.from_orm(entity)

    def get_all(self) -> list[CorrectProject]:
        return [CorrectProject.from_orm(entity) for entity in Project.query.all()]

    def delete(self, uid) -> None:
        entity = Project.query.filter(Project.uid == uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: project id {uid} not found')

        db_session.delete(entity)
        db_session.commit()

    def get_balloon_by_id(self, uid) -> CorrectProject:
        entity = Project.query.filter(Project.uid == uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: project id {uid} not found')

        return CorrectProject.from_orm(entity)

    def update(self, project: CorrectProject) -> CorrectProject:
        entity = Project.query.filter(Project.uid == project.uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: project id {project.uid} not found')

        entity.name = project.name
        entity.created_at = project.created_at

        db_session.commit()
        return CorrectProject.from_orm(entity)
