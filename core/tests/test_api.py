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
