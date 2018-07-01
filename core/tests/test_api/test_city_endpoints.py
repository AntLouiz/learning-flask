import json
import os.path
import pytest
import tempfile
from core.base import images
from core.models.city import City


@pytest.mark.resources
def test_get_cities(client):
    response = client.get('/cities', headers=client.auth_header)
    assert response.status_code == 200


@pytest.mark.resources
def test_get_cities_data(client):
    new_city = City('Parnaíba', 'PI')
    new_city.save()

    response = client.get('/cities', headers=client.auth_header)

    data = json.loads(response.data)

    assert len(data) == 1
    assert data[0]['name'] == 'Parnaíba'


@pytest.mark.resources
def test_get_cities_many_data(client):
    cities = [
        {'name': 'Fortaleza', 'uf': 'CE'},
        {'name': 'Teresina', 'uf': 'PI'},
        {'name': 'Joao Pessoa', 'uf': 'PB'}
    ]
    cities = City.save_all(cities)

    response = client.get('/cities', headers=client.auth_header)

    data = json.loads(response.data)

    assert len(data) == 3
    assert data[0]['slug'] == 'fortaleza'
    assert data[1]['slug'] == 'teresina'
    assert data[2]['slug'] == 'joao-pessoa'


@pytest.mark.resources
def test_post_city_data(client):
    city = {'name': 'Fortaleza', 'uf': 'CE'}
    response = client.post('/cities', data=city, headers=client.auth_header)
    city = City.query.filter_by(slug='fortaleza').first()

    assert response.status_code == 201
    assert city.name == 'Fortaleza'


@pytest.mark.resources
def test_post_many_cities(client):
    cities = [
        {'name': 'Fortaleza', 'uf': 'CE'},
        {'name': 'Teresina', 'uf': 'PI'},
        {'name': 'Joao Pessoa', 'uf': 'PB'}
    ]

    response = client.post('/cities', data=cities[0], headers=client.auth_header)
    city = City.query.filter_by(name=cities[0]['name']).first()

    assert response.status_code == 201
    assert city.name == cities[0]['name']

    response = client.post('/cities', data=cities[1], headers=client.auth_header)
    city = City.query.filter_by(name=cities[1]['name']).first()

    assert response.status_code == 201
    assert city.name == cities[1]['name']

    response = client.post('/cities', data=cities[2], headers=client.auth_header)
    city = City.query.filter_by(name=cities[2]['name']).first()

    assert response.status_code == 201
    assert city.name == cities[2]['name']


@pytest.mark.resources
def test_post_cities_with_same_name(client):
    city = {'name': 'Fortaleza', 'uf': 'CE'}

    response = client.post('/cities', data=city, headers=client.auth_header)

    assert response.status_code == 201

    response = client.post('/cities', data=city, headers=client.auth_header)
    data = json.loads(response.data)

    """
        409 Conflict: Indicates that the request could not 
        be processed because of conflict in the request, such 
        as an edit conflict.
    """

    assert response.status_code == 409
    assert data['message'] == 'This city already exists.'


def test_get_city_default_image_url(client):
    city = {'name': 'Fortaleza', 'uf': 'CE'}

    response = client.post('/cities', data=city, headers=client.auth_header)
    data = json.loads(response.data)

    assert data['image_url'] == 'https://localhost:8000/uploads/images/default.png'


def test_city_default_image_is_in_path(client):
    city = {'name': 'Fortaleza', 'uf': 'CE'}

    response = client.post('/cities', data=city, headers=client.auth_header)
    data = json.loads(response.data)

    image_default_name = data['image_url'].split('/')[-1]

    image_path = images.path(image_default_name)

    assert os.path.exists(image_path)


def test_city_update_image_with_put(client):
    city = {'name': 'Fortaleza', 'uf': 'CE'}

    response = client.post('/cities', data=city, headers=client.auth_header)
    data = json.loads(response.data)

    temp_image = tempfile.NamedTemporaryFile(suffix=".png")
    temp_image_name = temp_image.name[1:].replace('/', '_')

    response = client.put(
        '/cities',
        data={'name': 'Fortaleza', 'city_image': temp_image},
        content_type='multipart/form-data',
        headers=client.auth_header
    )

    assert response.status_code == 201

    data = json.loads(response.data)

    assert data['image_url'] == 'https://localhost:8000/uploads/images/{}'.format(temp_image_name)
