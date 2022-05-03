import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
import pymysql
from herd.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
# to redirect users not logged in to login page when they try to use account route
login_manager.login_view = 'users.login'
# customizing the error shown when users try do the above
login_manager.login_message_category = 'info'


def create_app(config=Config):
    app = Flask(__name__)
    app.config.from_object(config)

    with app.app_context():
        db.init_app(app)
        bcrypt.init_app(app)
        login_manager.init_app(app)

        from herd.users.routes import users
        from herd.main.routes import main
        from herd.searches.routes import searches
        app.register_blueprint(users)
        app.register_blueprint(main)
        app.register_blueprint(searches)

    return app