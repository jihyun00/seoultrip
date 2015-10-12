from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from db import Base


__all__ = 'cultural_asset', 'cultural_asset_en',


class CulturalAsset(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)

    addr = Column(String)

    board = Column(String)

    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    lang_id = Column(Integer, ForeignKey('language.id'), nullable=False)

    region = relationship('region')

    category = relationship('category')

    language = relationship('language')


    __tablename__ = 'cultural_asset'


class CulturalAssetEn(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)

    addr = Column(String)

    board = Column(String)

    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    lang_id = Column(Integer, ForeignKey('language.id'), nullable=False)

    cultural_asset_id = Column(Integer, ForeignKey('cultural_asset.id'), nullable=False)

    region = relationship('region')

    category = relationship('category')

    language = relationship('language')

    cultural_asset = relationship('cultural_asset')


    __tablename__ = 'cultural_asset_en'
