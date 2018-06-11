from flask_heroku import Heroku
from flask_restful import Api
from core.base import db, app


heroku = Heroku(app)
db.create_all()
api = Api(app)

from resources import CityResource

api.add_resource(CityResource, '/cities', methods=['GET', 'POST'])
