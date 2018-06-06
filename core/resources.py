from flask_restful import Resource, Api
from flask import request, jsonify
from core.models.city import City, city_schema, cities_schema
from core.base import app, db

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
        response = jsonify(result.data)
        response.status_code = 201

        return response


api.add_resource(CityResource, '/cities', methods=['GET', 'POST'])
