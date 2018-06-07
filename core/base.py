from flask import Flask, Blueprint
from core.settings import DB_URI, TEST_DB_URI
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app_blueprint = Blueprint('learning_flask', __name__)


def create_app(test=False):
    app = Flask(__name__)
    app.register_blueprint(app_blueprint)

    app.config['SQLALCHEMY_BINDS'] = {
        'development': DB_URI,
        'test': TEST_DB_URI
    }

    if not test:
        app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
        app.config['ENV'] = 'development'
        app.config['DEBUG'] = True
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    else:
        app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URI
        app.config['TESTING'] = True

    return app


app = create_app()
db = SQLAlchemy(app)

ma = Marshmallow(app)
migrate = Migrate(app, db)
