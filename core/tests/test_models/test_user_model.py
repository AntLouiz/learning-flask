import pytest
from sqlalchemy.exc import IntegrityError
from passlib.hash import pbkdf2_sha256 as sha256
from core.models.user import User, user_schema


@pytest.fixture
def new_user():
    return User(username='AntLouiz', password='123')


def test_create_new_user(init_db, new_user):
    assert new_user.username == 'AntLouiz'
    assert new_user.password == '123'


def test_save_user_method(init_db, new_user):
    new_user.save()

    user = User.query.filter_by(username='AntLouiz').first()

    assert user.username == 'AntLouiz'


def test_new_user_with_same_name(init_db, new_user):
    new_user.save()
    same_username = User(username=new_user.username, password='1234')

    with pytest.raises(IntegrityError):
        same_username.save()


def test_update_username(init_db, new_user):
    new_user.save()
    user = User.query.filter_by(username=new_user.username).first()
    user.username = 'Luiz'

    user.save()
    user = User.query.filter_by(username=user.username).first()

    assert user.username == 'Luiz'


def test_update_password(init_db, new_user):
    new_user.save()
    user = User.query.filter_by(username=new_user.username).first()
    user.password = 'another_password'

    assert user.password == 'another_password'


def test_staticmethod_generate_hash(init_db, new_user):
    user_hash = User.generate_hash(new_user.password)
    assert sha256.verify(new_user.password, user_hash)


def test_staticmethod_verify_hash(init_db, new_user):
    user_hash = User.generate_hash(new_user.password)

    assert User.verify_hash(new_user.password, user_hash)


def test_user_schema(init_db, new_user):
    new_user.save()

    result = user_schema.dump(new_user)

    assert result.data == {'username': new_user.username}
