from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# this secret key is used by wtforms to make shit secure 
# remember to turn this into an environment variable later on
app.config['SECRET_KEY'] = '88d99ae8d44e1eb62cd8d4f7c6dc1034'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from herd import routes