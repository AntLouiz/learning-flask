from core.models.user import User, user_schema, users_schema


def test_create_new_user(init_db):
    new_user = User(username='AntLouiz', password='123')

    assert new_user.username == 'AntLouiz'
    assert new_user.password == '123'
