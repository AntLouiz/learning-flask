import os.path
from core.settings import DB_URI, TEST_DB_URI, JWT_SECRET_KEY


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    JWT_SECRET_KEY = JWT_SECRET_KEY
    SQLALCHEMY_BINDS = {
        'test': TEST_DB_URI
    }
    UPLOADS_DEFAULT_DEST = os.path.join(
        os.path.abspath('core'),
        'uploads'
    )
    UPLOADS_DEFAULT_URL = 'https://localhost:8000/uploads/'
    UPLOADED_DEFAULT_DEST = os.path.join(
        os.path.abspath('core'),
        'uploads'
    )
    UPLOADED_DEFAULT_URL = 'https://localhost:8000/uploads/'


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = DB_URI
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = DB_URI
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = TEST_DB_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}
