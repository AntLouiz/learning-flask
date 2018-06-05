from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from settings import DB_URL

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
db = SQLAlchemy(app)
ma = Marshmallow(app)
migrate = Migrate(app, db)
