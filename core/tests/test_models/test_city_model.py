import pytest
import sqlalchemy
from core.models.city import City, city_schema, cities_schema


def test_create_new_city(init_db):
    new_city = City(name='Parnaíba', uf='PI')

    assert new_city.name == 'Parnaíba'
    assert new_city.uf == 'PI'
    assert new_city.slug == 'parnaiba'


def test_save_city_method(init_db):
    new_city = City(name='Parnaíba', uf='PI')
    new_city.save()

    city = City.query.filter_by(slug='parnaiba').first()

    assert city.name == 'Parnaíba'


def test_create_new_city_on_database(init_db):
    new_city = City(name='Teresina', uf='PI')
    new_city.save()

    cities = City.query.first()

    assert cities.name == 'Teresina'


def test_create_new_city_with_the_same_name(init_db):
    new_city = City('Sao Luis', 'MA')
    new_city.save()

    with pytest.raises(sqlalchemy.exc.IntegrityError):
        same_name_city = City('Sao Luis', 'MA')
        same_name_city.save()


def test_list_new_cities_on_database(init_db):
    cities = [
        {'name': 'Parnaíba', 'uf': 'PI'},
        {'name': 'Teresina', 'uf': 'PI'},
        {'name': 'Campina Grande', 'uf': 'PB'}
    ]
    cities = City.save_all(cities)
    assert len(cities) == 3

    assert cities[0].name == 'Parnaíba'
    assert cities[0].slug == 'parnaiba'
    assert cities[0].image_url == 'https://localhost:8000/uploads/images/default.png'

    assert cities[1].name == 'Teresina'
    assert cities[1].slug == 'teresina'
    assert cities[1].image_url == 'https://localhost:8000/uploads/images/default.png'

    assert cities[2].name == 'Campina Grande'
    assert cities[2].slug == 'campina-grande'
    assert cities[2].image_url == 'https://localhost:8000/uploads/images/default.png'


def test_list_new_cities_on_database_with_error(init_db):
    with pytest.raises(TypeError):
        cities = set([
            {'name': 'Parnaíba', 'uf': 'PI'},
            {'name': 'Teresina', 'uf': 'PI'},
            {'name': 'Campina Grande', 'uf': 'PB'}
        ])
        cities = City.save_all(cities)


def test_update_city_on_database(init_db):
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
    assert city.image_url == 'https://localhost:8000/uploads/images/default.png'


def test_update_city_on_database_with_error(init_db):

    with pytest.raises(AttributeError):
        city = City('Parnaíba', 'PI')
        city.save()

        city = City.query.filter_by(name='Parnaíba').first()
        city.update(some_unknow_attr='some_attr')


def test_delete_city_on_database(init_db):
    city = City('Timon', 'PI')
    city.save()

    city = City.query.filter_by(name='Timon').first()
    city.delete()

    count_search_city = City.query.filter_by(name='Timon').count()

    assert count_search_city == 0


def test_city_schema(init_db):
    new_city = City(name='Parnaíba', uf='PI')
    new_city.save()

    result = city_schema.dump(new_city)

    assert result.data == {
        'name': 'Parnaíba',
        'uf': 'PI',
        'slug': 'parnaiba',
        'image_url': 'https://localhost:8000/uploads/images/default.png'
    }


def test_cities_schema(init_db):
    cities = [
        {'name': 'Pedro II', 'uf': 'PI'},
        {'name': 'Brasília', 'uf': 'DF'},
        {'name': 'Campina Grande', 'uf': 'PB'}
    ]
    cities = City.save_all(cities)

    result = cities_schema.dump(cities)

    print(result)

    assert result.data[0] == {
        'name': 'Pedro II',
        'uf': 'PI',
        'slug': 'pedro-ii',
        'image_url': 'https://localhost:8000/uploads/images/default.png'
    }
    assert result.data[1] == {
        'name': 'Brasília',
        'uf': 'DF',
        'slug': 'brasilia',
        'image_url': 'https://localhost:8000/uploads/images/default.png'
    }
    assert result.data[2] == {
        'name': 'Campina Grande',
        'uf': 'PB',
        'slug': 'campina-grande',
        'image_url': 'https://localhost:8000/uploads/images/default.png'
    }
