import pytest
import json
from core.base import db
from core.api import app
from core.config import TestingConfig


@pytest.fixture
def init_db():
    with app.app_context():
        db.create_all(app=app)
        yield db

    db.drop_all()


@pytest.fixture
def client():
    app.config.from_object(TestingConfig)
    client = app.test_client()

    with app.app_context():
        db.create_all(app=app)
        response = client.post(
            '/registration',
            data={
                'username': 'test',
                'password': 'test'
            }
        )
        client.auth_header = {
            'Authorization': 'Bearer {}'.format(
                json.loads(response.data)['access_token']
            )
        }
        yield client

    db.drop_all()
