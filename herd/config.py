from os import environ, path
from dotenv import load_dotenv

load_dotenv()

class Config_FYP:
    FLASK_ENV = 'development'
    SECRET_KEY = '88d99ae8d44e1eb62cd8d4f7c6dc1034'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///users.db'
    SQLALCHEMY_BINDS = {'herd': 'mysql+pymysql://goot:123@192.168.1.6:3306/herd'}
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    
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
    
