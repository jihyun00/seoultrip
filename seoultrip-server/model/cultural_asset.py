from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from .db import Base


__all__ = 'cultural_asset', 'cultural_asset_en',


class CultrualAsset(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)

    addr = Column(String, nullable=False)

    board = Column(String, nullable=False)

    phone = Column(String, nullable=False)

    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    lang_id = Column(Integer, ForeignKey('lang.id'), nullable=False)

    region = relationship('region')

    category = relationship('category')

    lang = relationship('lang')


    __tablename__ = 'cultural_asset'


class CuturalAssetEn(Base, CulturalAsset):
    cultural_asset_id = Column(Integer, ForeignKey('cutural_asset.id'), nullable=False)

    cultural_asset = relationship('cutural_asset')

    __tablename__ = 'cultural_asset_en'
