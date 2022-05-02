from os import environ, path
from dotenv import load_dotenv

load_dotenv()

class Config:
    FLASK_ENV = 'development'
    SECRET_KEY = environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = environ.get('SQLITE_URI')
    SQLALCHEMY_BINDS = {'herd': environ.get('HERD_URI')}
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    
class TestConfig():
    # def __init__(self,SQLALCHEMY_DATABASE_URI):
    #     self.SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    LOGIN_DISABLED = True
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    
