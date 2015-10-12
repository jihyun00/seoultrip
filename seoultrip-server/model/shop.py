from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from db import Base


__all__ = 'shop', 'shop_en',


class Shop(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)

    addr = Column(String)

    kind = Column(Integer)

    phone = Column(String)

    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    lang_id = Column(Integer, ForeignKey('language.id'), nullable=False)

    region = relationship('region')

    category = relationship('category')

    language = relationship('language')


    __tablename__ = 'shop'


class ShopEn(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)

    addr = Column(String)

    kind = Column(Integer)

    phone = Column(String)

    region_id = Column(Integer, ForeignKey('region.id'), nullable=False)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    lang_id = Column(Integer, ForeignKey('language.id'), nullable=False)

    shop_id = Column(Integer, ForeignKey('shop.id'), nullable=False)

    region = relationship('region')

    category = relationship('category')

    language = relationship('language')

    shop = relationship('shop')


    __tablename__ = 'shop_en'
