import pytest
from core.base import db
from core.resources import app
from core.settings import DB_URI, TEST_DB_URI


@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = TEST_DB_URI
    client = app.test_client()

    with app.app_context():
        db.create_all(app=app)
        yield client

    db.drop_all()
