from flask import request, jsonify
from database import db
from base import app
from models.city import City, city_schema, cities_schema

# - generate the database schema
db.create_all()


@app.route('/')
def index():
    return "Hello World"


@app.route('/cities', methods=['GET'])
def list_cities():
    cities = City.query.all()
    result = cities_schema.dump(cities)

    return jsonify(result.data)


@app.route('/cities/<slug>', methods=['GET'])
def get_city(slug=None):
    city = City.query.filter_by(slug=slug).first_or_404()
    result = city_schema.dump(city)

    return jsonify(result.data)


@app.route('/cities', methods=['POST'])
def add_city():
    city_name = request.form['name']
    city_uf = request.form['uf']

    new_city = City(city_name, city_uf)

    db.session.add(new_city)

    db.session.commit()

    result = city_schema.dump(new_city)

    return jsonify(result.data)


@app.route('/cities/<id>', methods=['PUT'])
def update_city():
    pass


@app.route('/cities/<id>', methods=['DELETE'])
def delete_city():
    pass


if __name__ == '__main__':
    app.run(debug=True)
