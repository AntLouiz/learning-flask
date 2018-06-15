import pytest
from core.base import db
from core.api import app
from core.config import TestingConfig


@pytest.fixture
def client():
    app.config.from_object(TestingConfig)
    client = app.test_client()

    with app.app_context():
        db.create_all(app=app)
        yield client

    db.drop_all()
