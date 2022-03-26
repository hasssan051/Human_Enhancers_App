import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# this secret key is used by wtforms to make shit secure 
# remember to turn this into an environment variable later on
app.config['SECRET_KEY'] = '88d99ae8d44e1eb62cd8d4f7c6dc1034'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
# to redirect users not logged in to login page when they try to use account route
login_manager.login_view = 'login'
# customizing the error shown when users try do the above
login_manager.login_message_category = 'info'
from herd import routes