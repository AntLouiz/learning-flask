from core.models.city import City, city_schema, cities_schema


def test_city_schema(client):
    new_city = City(name='Parnaíba', uf='PI')
    new_city.save()

    result = city_schema.dump(new_city)

    assert result.data == {'name': 'Parnaíba', 'uf': 'PI', 'slug': 'parnaiba'}


def test_cities_schema(client):
    cities = [
        {'name': 'Pedro II', 'uf': 'PI'},
        {'name': 'Brasília', 'uf': 'DF'},
        {'name': 'Campina Grande', 'uf': 'PB'}
    ]
    cities = City.save_all(cities)

    result = cities_schema.dump(cities)

    assert result.data[0] == {'name': 'Pedro II', 'uf': 'PI', 'slug': 'pedro-ii'}
    assert result.data[1] == {'name': 'Brasília', 'uf': 'DF', 'slug': 'brasilia'}
    assert result.data[2] == {'name': 'Campina Grande', 'uf': 'PB', 'slug': 'campina-grande'}
