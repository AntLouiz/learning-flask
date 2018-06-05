from slugify import slugify
from database import db, ma


class City(db.Model):
    """A class that represents the table City"""

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    slug = db.Column(db.String)
    uf = db.Column(db.String(2))

    def __init__(self, name, uf, *args, **kwargs):
        self.name = name
        self.uf = uf
        self.slug = slugify(name)


class CitySchema(ma.Schema):

    class Meta:
        fields = ('name', 'uf', 'slug')


city_schema = CitySchema()
cities_schema = CitySchema(many=True)
