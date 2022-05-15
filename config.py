import os
# from dotenv import load_dotenv, find_dotenv


# load_dotenv(find_dotenv())
class config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    DEBUG = os.getenv('DEBUG')
    # SECRET_KEY = os.getenv('SECRET_KEY')


class ProdConfig(config):
    pass


class DevConfig(config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
