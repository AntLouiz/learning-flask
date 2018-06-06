from flask_restful import Resource, Api
from flask import request, jsonify, Blueprint
from core.models.city import City, city_schema, cities_schema
from core.base import create_app, db

app = create_app()
api = Api(app)


class CityResource(Resource):
    def get(self):
        cities = City.query.all()
        result = cities_schema.dump(cities)

        return jsonify(result.data)

    def post(self):
        new_city = City(request.form['name'], request.form['uf'])
        db.session.add(new_city)
        db.session.commit()

        result = city_schema.dump(new_city)

        return jsonify(result.data)


api.add_resource(CityResource, '/cities', methods=['GET', 'POST'])
