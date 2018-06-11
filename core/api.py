from flask_heroku import Heroku
from flask_restful import Api
from core.base import db, app
from core import resources


heroku = Heroku(app)
db.create_all()
api = Api(app)

api.add_resource(resources.UserRegistration, '/registration')
api.add_resource(resources.UserLogin, '/login')
api.add_resource(resources.UserLogoutAccess, '/logout/access')
api.add_resource(resources.UserLogoutRefresh, '/logout/refresh')
api.add_resource(resources.TokenRefresh, '/token/refresh')
api.add_resource(resources.AllUsers, '/users')
api.add_resource(resources.SecretResource, '/secret')

api.add_resource(resources.CityResource, '/cities', methods=['GET', 'POST'])
