from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine


__all__ = 'base',


engine = create_engine('sqlite:///root:root@localhost/seoultrip.db', echo=True)
#engine.connect()

Base = declarative_base()
#Session = sessionmaker(bind=engine)
