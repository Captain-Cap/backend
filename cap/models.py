
from sqlalchemy import TIMESTAMP, Column, Integer, String

from cap.db import Base, engine


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

    def __repr__(self) -> str:
        return f'Balloons {self.uid} {self.firm} {self.color} {self.weight}'


if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
