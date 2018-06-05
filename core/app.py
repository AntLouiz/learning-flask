from flask import request, jsonify
from base import Base, Session, engine, app
from bases.city import City, city_schema, cities_schema

# - generate the database schema
Base.metadata.create_all(engine)

# - start a new session
session = Session()


@app.route('/')
def hello():
    return "Hello World"


@app.route('/cities', methods=['GET'])
def list_cities():
    cities = session.query(City).all()
    result = cities_schema.dump(cities)

    return jsonify(result.data)


@app.route('/cities', methods=['POST'])
def add_cities():
    city_name = request.form['name']
    city_uf = request.form['uf']

    new_city = City(city_name, city_uf)

    session.add(new_city)

    session.commit()

    result = city_schema.dump(new_city)

    return jsonify(result.data)


if __name__ == '__main__':
    app.run(debug=True)
