from flask import Flask, Blueprint
from core.settings import DB_URI, TEST_DB_URI
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app_blueprint = Blueprint('learning_flask', __name__)
db = SQLAlchemy()


def create_app(test=False):
    app = Flask(__name__)
    app.register_blueprint(app_blueprint)
    app.app_context().push()

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_BINDS'] = {
        'devlopment': DB_URI,
        'test': TEST_DB_URI
    }

    if test:
        app.config['SQL_ALCHEMY_DATABASE_URI'] = TEST_DB_URI
        app.config['TESTING'] = True

    db.init_app(app)

    return app


app = create_app()
ma = Marshmallow(app)
migrate = Migrate(app, db)
