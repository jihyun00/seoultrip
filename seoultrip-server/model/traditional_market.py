from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Float

from .db import Base


__all__ = 'traditional_market',


class TraditionalMarket(Base):
    id = Column(Integer, primary_key=True) # auto_increment?

    name = Column(String, nullable=False)

    addr = Column(String, nullable=False)

    phone = Column(String, nullable=False)

    lat = Column(Float, primary_key=True)

    lng = Column(Float, primary_key=True)
    
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    lang_id = Column(Integer, ForeignKey('lang.id'), nullable=False)

    region = relationship('region')

    category = relationship('category')

    lang = relationship('lang')


    __tablename__ = 'traditional_market'
