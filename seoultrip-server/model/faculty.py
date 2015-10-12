from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from db import Base


__all__ = 'faculty', 


class Faculty(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    composite_id = Column(Integer, nullable=False) # TODO: composite key 추가 

    category = relationship('category')


    __tablename__ = 'faculty'

