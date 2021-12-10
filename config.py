from os import environ


class Config(object):

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    SECRET_KEY = environ.get('SECRET_KEY')


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False


class TestConfig(Config):

    TESTING = True


appConfig = {

    'development': DevConfig,
    'production': ProdConfig,
    'Testing': TestConfig,
    'default': DevConfig

}

