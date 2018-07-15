from flask_heroku import Heroku
from flask_restful import Api
from flask_jwt_extended import JWTManager
from core.base import db, app
from core.models.jwt import RevokedToken
from core import resources


heroku = Heroku(app)
jwt = JWTManager(app)
db.create_all()
api = Api(app)

api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')

api.add_resource(resources.CityResource, '/cities', methods=['GET', 'POST', 'PUT'])


@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    jti = decrypted_token['jti']
    return RevokedToken.is_jti_blacklisted(jti)
