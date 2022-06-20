from datetime import datetime

from cap import schemas
from cap.db import db_session
from cap.errors import NotFoundError
from cap.models import Project


class ProjectStorage():
    name = 'project'

    def add(self, project: schemas.Project) -> schemas.Project:
        entity = Project(
            uid=None,
            name=project.name,
            created_at=datetime.now(),
        )
        db_session.add(entity)
        db_session.commit()
        return schemas.Project.from_orm(entity)

    def get_all(self) -> list[schemas.Project]:
        return [schemas.Project.from_orm(entity) for entity in Project.query.all()]

    def delete(self, uid) -> None:
        entity = Project.query.filter(Project.uid == uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: project id {uid} not found')

        db_session.delete(entity)
        db_session.commit()

    def get_by_id(self, uid) -> schemas.Project:
        entity = Project.query.filter(Project.uid == uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: project id {uid} not found')

        return schemas.Project.from_orm(entity)

    def update(self, project: schemas.Project) -> schemas.Project:
        entity = Project.query.filter(Project.uid == project.uid).first()
        if not entity:
            raise NotFoundError(self.name, f'reason: project id {project.uid} not found')

        entity.name = project.name
        entity.created_at = project.created_at

        db_session.commit()
        return schemas.Project.from_orm(entity)
