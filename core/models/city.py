from slugify import slugify
from core.base import db, ma


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

    def save(self):
        self.slug = slugify(self.name)
        db.session.add(self)
        db.session.commit()

        return self

    def update(self, *args, **kwargs):
        if set(kwargs.keys()).issubset(set(self.__dict__.keys())):
            if 'slug' and 'name' in kwargs.keys():
                kwargs['slug'] = slugify(kwargs['name'])

            for key in kwargs.keys():
                setattr(self, key, kwargs[key])

            db.session.commit()

        else:
            raise AttributeError

        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

        return True


class CitySchema(ma.Schema):

    class Meta:
        fields = ('name', 'uf', 'slug')


city_schema = CitySchema()
cities_schema = CitySchema(many=True)
