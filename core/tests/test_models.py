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
