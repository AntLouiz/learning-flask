from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask_marshmallow import Marshmallow
from settings import DB_URL

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()

app = Flask(__name__)
ma = Marshmallow(app)
