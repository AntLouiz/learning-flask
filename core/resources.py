from flask_restful import Resource, reqparse
from flask import request, jsonify
from core.models.city import City, city_schema, cities_schema
from core.models.user import User, users_schema
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    jwt_required,
    jwt_refresh_token_required,
    get_jwt_identity,
    get_raw_jwt
)


class CityResource(Resource):

    @jwt_required
    def get(self):
        cities = City.query.all()
        result = cities_schema.dump(cities)

        return jsonify(result.data)

    @jwt_required
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
        if User.query.filter_by(username=data['username']).scalar():
            response = jsonify({'message': 'The user {} already exists.'.format(data['username'])})
            response.status_code = 409
            return response

        new_user = User(
            username=data['username'],
            password=User.generate_hash(data['password'])
        )

        new_user.save()

        access_token = create_access_token(identity=data['username'])
        refresh_token = create_refresh_token(identity=data['username'])

        return {
            'message': 'User {} was created.'.format(data['username']),
            'access_token': access_token,
            'refresh_token': refresh_token
        }


class UserLogin(Resource):
    def post(self):
        data = parser.parse_args()
        current_user = User.query.filter_by(username=data['username']).first()

        if not current_user:
            return {'message': 'User {} doesn\'t exist'.format(data['username'])}

        try:
            User.verify_hash(data['password'], current_user.password)
            access_token = create_access_token(identity=data['username'])
            refresh_token = create_refresh_token(identity=data['username'])

            return {
                'message': 'Logged in as {}.'.format(current_user.username),
                'access_token': access_token,
                'refresh_token': refresh_token
            }

        except ValueError:
            return {'message': 'Wrong credentials'}

class UserLogoutAccess(Resource):
    def post(self):
        return {'message': 'User logout access'}

class UserLogoutRefresh(Resource):
    def post(self):
        return {'message': 'User logout'}


class TokenRefresh(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        return {'access_token': access_token}

class AllUsers(Resource):
    def get(self):
        result = users_schema.dump(User.query.all())
        users = jsonify(result.data)

        return users

class SecretResource(Resource):
    def get(self):
        return {
            'answer': 42
        }
