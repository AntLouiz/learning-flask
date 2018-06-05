from sqlalchemy import (
    Column,
    String,
    Integer
)
from base import Base
from base import ma


class City(Base):
    """A class that represents the table City"""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    uf = Column(String(2))

    def __init__(self, name, uf):
        self.name = name
        self.uf = uf


class CitySchema(ma.Schema):

    class Meta:
        fields = ('name', 'uf')


city_schema = CitySchema()
cities_schema = CitySchema(many=True)
