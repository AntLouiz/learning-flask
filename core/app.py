from flask import request, jsonify
from base import Base, Session, engine, app
from bases.city import City, CitySchema

# - generate the database schema
Base.metadata.create_all(engine)

# - start a new session
session = Session()


@app.route('/')
def hello():
    return "Hello World"


@app.route('/cities')
def list_cities():
    cities = session.query(City).all()
    city_schema = CitySchema()

    return city_schema.jsonify(cities)


@app.route('/cities', methods=['POST'])
def add_cities():
    city_name = request.form['name']
    city_uf = request.form['uf']

    new_city = City(city_name, city_uf)
    city_schema = CitySchema()

    session.add(new_city)

    session.commit()

    return city_schema.jsonify(new_city)


if __name__ == '__main__':
    app.run(debug=True)
