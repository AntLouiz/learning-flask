from flask_heroku import Heroku
from flask_restful import Api
from core.base import db, app
from core.resources import CityResource


heroku = Heroku(app)
db.create_all()
api = Api(app)

api.add_resource(CityResource, '/cities', methods=['GET', 'POST'])
