from flask import Flask, Blueprint
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet, IMAGES, configure_uploads
from core.settings import ENV
from core.config import config


app_blueprint = Blueprint('learning_flask', __name__)


def create_app(test=False):
    app = Flask(__name__)
    app.register_blueprint(app_blueprint)

    return app


app = create_app()
app.config.from_object(config[ENV])

db = SQLAlchemy(app)

ma = Marshmallow(app)
migrate = Migrate(app, db)

images = UploadSet('images', IMAGES)
configure_uploads(app, images)
