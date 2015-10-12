from flask import Flask
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import Integer, String

from db import Base


__all__ = 'comment',


class Comment(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)

    reputation = Column(Integer, nullable=False)

    content = Column(String, nullable=False)

    faculty_id = Column(Integer, ForeignKey('faculty.id'), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)

    faculty = relationship('faculty')

    user = relationship('user')


    __tablename__ = 'comment'

