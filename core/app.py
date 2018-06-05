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


if __name__ == '__main__':
    app.run(debug=True)
