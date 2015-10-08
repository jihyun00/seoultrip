from flask import Flask
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from .db import Base


__all__ = 'category',


class Category(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String, nullable=False)


    __tablename__ = 'category'
