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

    if not test:
        app.config['SQL_ALCHEMY_DATABASE_URI'] = 'postgres://wumsefgkxgonss:4bcb08540bfb80f7f1a4f45424ac5d99a8949db7b360ba39618c1f63979bfa3e@ec2-54-204-18-53.compute-1.amazonaws.com:5432/d9661451o3plqo'
    else:
        app.config['SQL_ALCHEMY_DATABASE_URI'] = TEST_DB_URI
        app.config['TESTING'] = True

    db.init_app(app)

    return app


app = create_app()
ma = Marshmallow(app)
migrate = Migrate(app, db)
