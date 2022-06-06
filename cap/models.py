from sqlalchemy import Column, Integer, String, Date
from db import Base, engine


class Balloons(Base):
    __tablename__ = "balloons"

    uid = Column(Integer, primary_key=True)
    firm = Column(String())
    paint_code = Column(String())
    color = Column(String())
    volume = Column(String())
    weight = Column(Integer)
    created = Column(Date())