def test_get_cities(client):
    with client:
        response = client.get('/')
        assert response.status_code == 200
