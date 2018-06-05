from flask_restful import Resource, Api
from models.city import City
from base import create_app, db

app = create_app()
api = Api(app)
db.create_all(app=app)


class CityResource(Resource):
    def get(self):
        cities = City.query.all()
        print(cities)
        return {'hello': 'world'}


api.add_resource(CityResource, '/')

if __name__ == '__main__':
    app.run(debug=True)
