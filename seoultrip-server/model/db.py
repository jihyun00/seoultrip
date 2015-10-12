from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import declarative_base


__all__ = 'Base',

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqllite://seoultrip:seoultrip@bbaba.kr/seoultrip.db'
db = SQLAlchemy(app)
