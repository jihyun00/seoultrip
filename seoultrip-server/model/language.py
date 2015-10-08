from flask import Flask
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String

from .db import Base


__all__ = 'language',


class Language(Base):
    id = Column(Integer, primary_key=True) # auto_increment?

    name = Column(String, nullable=False)


    __tablename__ = 'language'
