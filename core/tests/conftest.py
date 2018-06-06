import pytest
from core.base import db
from core.resources import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()

    with app.app_context():
        db.create_all(app=app)
        yield client

    db.drop_all()
