from flask import Flask
from settings import DB_URI, TEST_DB_URI


def create_app(name, test=False):
    app = Flask(name)

    if not test:
        app.config['SQL_ALCHEMY_DATABASE_URI'] = DB_URI
    else:
        app.config['SQL_ALCHEMY_DATABASE_URI'] = TEST_DB_URI
        app.config['TESTING'] = True

    return app

app = create_app(__name__)
