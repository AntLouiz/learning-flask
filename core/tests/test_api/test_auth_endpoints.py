import json
import pytest


@pytest.mark.auth
def test_register_new_user(client):
    response = client.post(
        '/registration',
        data={
            'username': 'someUser',
            'password': 'somePassword'
        }
    )

    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'User someUser was created.'


@pytest.mark.auth
def test_register_existing_user(client):
    client.post(
        '/registration',
        data={
            'username': 'someUser',
            'password': 'somePassword'
        }
    )

    response = client.post(
        '/registration',
        data={
            'username': 'someUser',
            'password': 'somePassword'
        }
    )

    assert response.status_code == 409
    assert json.loads(response.data)['message'] == 'The user someUser already exists.'


@pytest.mark.auth
def test_register_with_error(client):
    response = client.post(
        '/registration',
        data={
            'username': None,
            'password': None
        }
    )

    assert response.status_code == 400
    assert json.loads(response.data)['message']['username'] == 'This field cannot be blank'

    response = client.post(
        '/registration',
        data={
            'username': 'someUser',
            'password': None
        }
    )

    assert response.status_code == 400
    assert json.loads(response.data)['message']['password'] == 'This field cannot be blank'

    response = client.post(
        '/registration',
        data={
            'username': None,
            'password': 'somepassword'
        }
    )

    assert response.status_code == 400
    assert json.loads(response.data)['message']['username'] == 'This field cannot be blank'


@pytest.mark.auth
def test_user_login_with_success(client):
    username = 'someUsername'
    password = 'somepassword'

    client.post(
        '/registration',
        data={
            'username': username,
            'password': password
        }
    )

    response = client.post(
        '/login',
        data={
            'username': username,
            'password': password
        }
    )

    assert response.status_code == 200
    assert json.loads(response.data)['message'] == 'Logged in as {}.'.format(username)


@pytest.mark.auth
def test_user_login_does_exist(client):
    username = 'someUsername'
    unknownUsername = 'someUnknownUsername'
    password = 'somepassword'

    client.post(
        '/registration',
        data={
            'username': username,
            'password': password
        }
    )

    response = client.post(
        '/login',
        data={
            'username': unknownUsername,
            'password': password
        }
    )

    assert response.status_code == 400
    assert json.loads(response.data)['message'] == 'User {} doesn\'t exist.'.format(unknownUsername)


@pytest.mark.auth
def test_user_login_does_wrong_credentials(client):
    username = 'someUsername'
    password = 'somepassword'

    client.post(
        '/registration',
        data={
            'username': username,
            'password': password
        }
    )

    response = client.post(
        '/login',
        data={
            'username': username,
            'password': '123'
        }
    )

    assert response.status_code == 400
    assert json.loads(response.data)['message'] == 'Wrong credentials.'
