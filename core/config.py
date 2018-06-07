from core.settings import DB_URI, TEST_DB_URI


class BaseConfig(object):
    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = DB_URI
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = DB_URI
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True


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
