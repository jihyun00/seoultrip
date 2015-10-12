from alembic.config import Config
from flask import Flask, current_app
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine import Engine
from sqlalchemy.orm import Session as SqlalchemySession, sessionmaker

__all__ = 'base',

engine = create_engine('sqlite:///seoultrip.db', convert_unicode=True)

def init_db():
    import category, comment, cultural_asset, faculty, language, region, shop, stay, traditional_market, user
    Base.metadata.create_all(bind=engine)


Base = declarative_base()
Session = sessionmaker()
#session = LocalProxy(get_session)
