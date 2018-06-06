import pytest
from core.base import db
from core.models.city import City


def test_create_new_city(client):
    new_city = City(name='Parnaíba', uf='PI')

    assert new_city.name == 'Parnaíba'


def test_save_city_method(client):
    new_city = City(name='Parnaíba', uf='PI')
    new_city.save()

    city = City.query.filter_by(slug='parnaiba').first()

    assert city.name == 'Parnaíba'


def test_create_new_city_on_database(client):
    new_city = City(name='Teresina', uf='PI')
    new_city.save()

    cities = City.query.first()

    assert cities.name == 'Teresina'


def test_list_new_cities_on_database(client):
    cities = [
        {'name': 'Parnaíba', 'uf': 'PI'},
        {'name': 'Teresina', 'uf': 'PI'},
        {'name': 'Campina Grande', 'uf': 'PB'}
    ]
    cities = City.save_all(cities)
    assert len(cities) == 3

    assert cities[0].name == 'Parnaíba'
    assert cities[0].slug == 'parnaiba'

    assert cities[1].name == 'Teresina'
    assert cities[1].slug == 'teresina'

    assert cities[2].name == 'Campina Grande'
    assert cities[2].slug == 'campina-grande'


def test_list_new_cities_on_database_with_error(client):
    with pytest.raises(TypeError):
        cities = set([
            {'name': 'Parnaíba', 'uf': 'PI'},
            {'name': 'Teresina', 'uf': 'PI'},
            {'name': 'Campina Grande', 'uf': 'PB'}
        ])
        cities = City.save_all(cities)


def test_update_city_on_database(client):
    city = City('Parnaíba', 'PI')
    city.save()

    city = City.query.filter_by(name='Parnaíba').first()
    city.update(name='Fortaleza', uf='CE')

    count_search_city = City.query.filter_by(name='Parnaíba').count()
    city = City.query.filter_by(name='Fortaleza').first()

    assert count_search_city == 0
    assert city.name == 'Fortaleza'
    assert city.slug == 'fortaleza'
    assert city.uf == 'CE'


def test_update_city_on_database_with_error(client):

    with pytest.raises(AttributeError):
        city = City('Parnaíba', 'PI')
        city.save()

        city = City.query.filter_by(name='Parnaíba').first()
        city.update(some_unknow_attr='some_attr')


def test_delete_city_on_database(client):
    city = City('Timon', 'PI')
    city.save()

    city = City.query.filter_by(name='Timon').first()
    city.delete()

    count_search_city = City.query.filter_by(name='Timon').count()

    assert count_search_city == 0
