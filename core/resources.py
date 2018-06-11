from flask_restful import Resource, reqparse
from flask import request, jsonify
from core.models.city import City, city_schema, cities_schema
from core.models.user import User


class CityResource(Resource):
    def get(self):
        cities = City.query.all()
        result = cities_schema.dump(cities)

        return jsonify(result.data)

    def post(self):

        if City.query.filter_by(name=request.form['name']).scalar():
            response = jsonify({'message': 'This city already exists.'})
            response.status_code = 409
            return response

        new_city = City(request.form['name'], request.form['uf'])
        new_city.save()
        result = city_schema.dump(new_city)
        response = jsonify(result.data)
        response.status_code = 201

        return response


parser = reqparse.RequestParser()
parser.add_argument('username', help='This field cannot be blank', required=True)
parser.add_argument('password', help='This field cannot be blank', required=True)


class UserRegistration(Resource):
    def post(self):
        data = parser.parse_args()
        return data


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()

        if User.query.filter_by(name=request.form['username']).scalar():
            response = jsonify({'message': 'This user already exists.'})
            response.status_code = 409
            return response

        new_user = User(
            username=data['username'],
            password=data['password']
        )

        new_user.save()

        return {'message': 'The user {} was created.'.format(data['username'])}

class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout access'}

class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}

class TokenRefresh(Resource):
    def post(self):
        return {'message': 'Token refresh'}

class AllUsers(Resource):
    def get(self):
        return {'users': []}

class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }
