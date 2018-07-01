from flask_restful import Resource, reqparse
from flask import request, jsonify
from core.base import images
from core.models.city import City, city_schema, cities_schema
from core.models.user import User
from core.models.jwt import RevokedToken
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

    @jwt_required
    def put(self):
        if request.files['city_image']:
            image_filename = images.save(request.files['city_image'])
            image_url = images.url(image_filename)

        return {'image_url': image_url}, 201


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
            return {'message': 'User {} doesn\'t exist.'.format(data['username'])}, 400

        error_message = {'message': 'Wrong credentials.'}, 400

        try:
            if User.verify_hash(data['password'], current_user.password):
                access_token = create_access_token(identity=data['username'])
                refresh_token = create_refresh_token(identity=data['username'])

                return {
                    'message': 'Logged in as {}.'.format(current_user.username),
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }

            return error_message

        except ValueError:
            return error_message


class UserLogoutAccess(Resource):
    @jwt_required
    def post(self):
        jti = get_raw_jwt()['jti']

        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.add()
            response = jsonify({'message': 'Access token has been revoked'})
            response.status_code = 200

            return response

        except:
            response = jsonify({'message': 'Something went wrong'})
            response.status_code = 500

            return response


class UserLogoutRefresh(Resource):

    @jwt_refresh_token_required
    def post(self):
        jti = get_raw_jwt()['jti']

        try:
            revoked_token = RevokedToken(jti=jti)
            revoked_token.add()
            response = jsonify({'message': 'Refresh token has been revoked'})
            response.status_code = 200

            return response

        except:

            response = jsonify({'message': 'Something went wrong'})
            response.status_code = 500


class TokenRefresh(Resource):

    @jwt_refresh_token_required
    def post(self):
        current_user = get_jwt_identity()
        access_token = create_access_token(identity=current_user)
        response = jsonify({'access_token': access_token})

        return response
