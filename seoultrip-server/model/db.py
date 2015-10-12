from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base


__all__ = 'base',


engine = create_engine('sqlite:///root:root@localhost/seoultrip.db', echo=True)

Base = declarative_base()
