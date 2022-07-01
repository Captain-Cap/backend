
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from cap.db import Base, engine


class Project(Base):
    __tablename__ = 'projects'

    uid = Column(Integer, primary_key=True)
    name = Column(String)
    created_at = Column(TIMESTAMP(timezone=True))
    balloons = relationship('Balloons')


class Balloons(Base):
    __tablename__ = 'balloons'

    uid = Column(Integer, primary_key=True)
    firm = Column(String())
    paint_code = Column(String())
    color = Column(String())
    volume = Column(String())
    weight = Column(Integer)
    created_at = Column(TIMESTAMP(timezone=True))
    updated_at = Column(TIMESTAMP(timezone=True))
    acceptance_date = Column(TIMESTAMP(timezone=True))
    project_id = Column(Integer(), ForeignKey(Project.uid), nullable=True)

    def __repr__(self) -> str:
        return f'Balloons {self.uid} {self.firm} {self.color} {self.weight}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
