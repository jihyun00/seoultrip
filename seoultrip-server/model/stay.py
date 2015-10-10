from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from .db import Base


__all__ = 'stay', 'stay_en',


class Stay(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)

    addr = Column(String, nullable=False)

    grade = Column(Integer)

    faculty = Column(String)

    room = Column(Integer)

    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    lang_id = Column(Integer, ForeignKey('lang.id'), nullable=False)

    region = relationship('region')

    category = relationship('category')

    lang = relationship('lang')


    __tablename__ = 'stay'


class StayEn(Base, Stay):
    stay_asset_id = Column(Integer, ForeignKey('stay.id'), nullable=False)

    stay = relationship('stay')

    __tablename__ = 'stay_en'
