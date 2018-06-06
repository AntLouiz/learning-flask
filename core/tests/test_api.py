import json
from core.models.city import City


def test_get_cities(client):
    with client:
        response = client.get('/cities')
        assert response.status_code == 200


def test_get_cities_data(client):
    with client:
        new_city = City('Parnaíba', 'PI')
        new_city.save()

        response = client.get('/cities')

        data = json.loads(response.data)

        assert len(data) == 1
        assert data[0]['name'] == 'Parnaíba'


def test_get_cities_many_data(client):
    with client:
        cities = [
            {'name': 'Fortaleza', 'uf': 'CE'},
            {'name': 'Teresina', 'uf': 'PI'},
            {'name': 'Joao Pessoa', 'uf': 'PB'}
        ]
        cities = City.save_all(cities)

        response = client.get('/cities')

        data = json.loads(response.data)

        assert len(data) == 3
        assert data[0]['slug'] == 'fortaleza'
        assert data[1]['slug'] == 'teresina'
        assert data[2]['slug'] == 'joao-pessoa'


def test_post_city_data(client):
    with client:
        city = {'name': 'Fortaleza', 'uf': 'CE'}
        response = client.post('/cities', data=city)
        city = City.query.filter_by(slug='fortaleza').first()

        assert response.status_code == 201
        assert city.name == 'Fortaleza'


def test_post_many_cities(client):
    cities = [
        {'name': 'Fortaleza', 'uf': 'CE'},
        {'name': 'Teresina', 'uf': 'PI'},
        {'name': 'Joao Pessoa', 'uf': 'PB'}
    ]

    response = client.post('/cities', data=cities[0])
    city = City.query.filter_by(name=cities[0]['name']).first()

    assert response.status_code == 201
    assert city.name == cities[0]['name']

    response = client.post('/cities', data=cities[1])
    city = City.query.filter_by(name=cities[1]['name']).first()

    assert response.status_code == 201
    assert city.name == cities[1]['name']

    response = client.post('/cities', data=cities[2])
    city = City.query.filter_by(name=cities[2]['name']).first()

    assert response.status_code == 201
    assert city.name == cities[2]['name']
