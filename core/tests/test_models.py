from core.base import db
from core.models.city import City


def test_create_new_city(client):
    new_city = City(name='Parnaíba', uf='PI')

    assert new_city.name == 'Parnaíba'


def test_create_new_city_on_database(client):
    new_city = City(name='Teresina', uf='PI')
    db.session.add(new_city)
    db.session.commit()

    cities = City.query.first()

    assert cities.name == 'Teresina'


def test_list_new_cities_on_database(client):
    cities = [
        City('Sao Luis', 'MA'),
        City('Brasília', 'DF'),
        City('Campina Grande', 'PB')
    ]
    db.session.bulk_save_objects(cities)
    db.session.commit()

    cities = City.query.count()

    assert cities == 3
