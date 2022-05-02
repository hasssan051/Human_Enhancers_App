
import flask
from herd import create_app, db
from herd.models import User
from herd.config import TestConfig
import pytest
import os
import tempfile

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(TestConfig)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            yield testing_client  


@pytest.fixture(scope='module')
def users_db():
    #db_fd, db_fname = tempfile.mkstemp()
    # flask_app = create_app(TestConfig( "sqlite://"))
    flask_app = create_app(TestConfig)
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    flask_app.config['TESTING'] =True
    flask_app.config['WTF_CSRF_ENABLED'] = False

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
           
            db.create_all()
            # user = User(firstname="John",lastname="Doe",email="johndoe@gmail.com",password="1234567",occupation="Student")
            # db.session.add(user)
            # db.session.commit()
            yield testing_client,db
    db.session.remove()
    # os.close(db_fd)
    # os.unlink(db_fname)

@pytest.fixture(scope='function')
def logged_in_user_client():

    flask_app = create_app(TestConfig)
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"
    flask_app.config['TESTING'] =True
    

    with flask_app.test_client() as testing_client:
        # Establish an application context
        with flask_app.app_context():
            flask_app.config['WTF_CSRF_ENABLED'] = False
            db.create_all()
            # user = User(firstname="John",lastname="Doe",email="johndoe@gmail.com",password="1234567",occupation="Student")
            # db.session.add(user)
            # db.session.commit()
            yield testing_client,db
    db.session.remove()
    # os.close(db_fd)
    # os.unlink(db_fname)