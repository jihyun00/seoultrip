from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String, Float

from db import Base


__all__ = 'traditional_market', 'traditional_market_en',


class TraditionalMarket(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)

    addr = Column(String)

    phone = Column(String)

    lat = Column(Float)

    lng = Column(Float)
    
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    lang_id = Column(Integer, ForeignKey('lang.id'), nullable=False)

    region = relationship('region')

    category = relationship('category')

    lang = relationship('lang')


    __tablename__ = 'traditional_market'


class TraditionalMarketEn(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)

    addr = Column(String)

    phone = Column(String)

    lat = Column(Float)

    lng = Column(Float)
    
    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    lang_id = Column(Integer, ForeignKey('lang.id'), nullable=False)

    traditional_market_id = Column(Integer, ForeignKey('traditional_market.id'), nullable=False)

    region = relationship('region')

    category = relationship('category')

    lang = relationship('lang')

    traditional_market = relationship('traditional_market')


    __tablename__ = 'traditional_market_en'
