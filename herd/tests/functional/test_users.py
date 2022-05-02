from herd.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from herd.models import User
import bcrypt
from flask import url_for

def _get_user():
    user = User(firstname="John",lastname="Doe",email="johndoe@gmail.com",password="1234567",occupation="Student")
    return user

def test_register_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/register' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b"Join Today" in response.data
    assert b"Register to do so much more." in response.data

def test_register_page_post(users_db):
    """
    GIVEN a Flask application
    WHEN the '/register' page is posted to using register form (POST)
    THEN check that a '200' status code is returned
    """
    url = url_for('users.register')
    test_client, db = users_db
    response = test_client.post(url,data={'firstname':'John', 'lastname':'Doe','email':'johndoe@gmail.com','password':"1234567",'occupation':"Student"},follow_redirects=True)
    assert response.status_code == 200

    # we are redirected to the login page
    assert b"Login" in response.data
    #assert b"Login to access your account." in response.data

    user_1 = User.query.filter_by(email="johndoe@gmail.com").first()
    # assert User.query.count() == 1
    assert user_1.firstname.strip() == "John"
    assert user_1.lastname == "Doe"
    # assert user_1.password != "12345678"
    # assert user_1.occupation == "Student"



def test_login_page(test_client):
    """
    GIVEN a Flask application configured for testing
    WHEN the '/login' page is requested (GET)
    THEN check that the response is valid
    """
    response = test_client.get('/login')
    assert response.status_code == 200
    assert b"Login" in response.data
    assert b"Login to access your account." in response.data

def test_login_page_post(users_db):
    """
    GIVEN a Flask application and a validated/authenticated user exists in the Users database
    WHEN the '/login' page is posted to (POST)
    THEN check that the user logs into their account
    """
    test_client, db = users_db
    user = _get_user()
    db.session.add(user)
    db.session.commit()

    user

    response = test_client.post('/login', data={'email':'johndoe@gmail.com'})
    assert response.status_code == 405
    assert b"Login" not in response.data
    assert b"Login to access your account." not in response.data