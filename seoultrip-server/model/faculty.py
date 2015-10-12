from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from .db import Base


__all__ = 'faculty', 


class Faculty(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    category = relationship('category')

    # TODO: 


    __tablename__ = 'faculty'

