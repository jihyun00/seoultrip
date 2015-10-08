from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base


__all__ = ('Base')


def get_engine(config: dict=None) -> Engine:
    if config is None:
        config = current_app.config
    if 'DATABASE_ENGINE' in config:
        return config['DATABASE_ENGINE']
    config['DATABASE_ENGINE'] = create_engine(config['DATABASE_URL'])
    return config['DATABASE_ENGINE']


Base = declarative_base()
