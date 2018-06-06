import pytest
from core.base import create_app, db


@pytest.fixture
def client():
    app = create_app(test=True)
    client = app.test_client()
    app.app_context().push()

    with app.app_context():
        db.create_all()

    yield client

    db.drop_all()
