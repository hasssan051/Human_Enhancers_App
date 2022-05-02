from herd.models import User


def _get_user():
    user = User(firstname="John",lastname="Doe",email="johndoe@gmail.com",password="1234567",occupation="Student")
    return user


def test_adding_users(users_db) -> None:
    '''
    GIVEN A FLASK application configured for testing with a freshly created Users database
    WHEN a new user is added to this database
    THEN test if the details of this user have correctly been added  
    '''
    test_client, users_db = users_db
    user = _get_user()
    users_db.session.add(user)
    users_db.session.commit()

    user_1 = User.query.filter_by(email="johndoe@gmail.com").first()
    assert User.query.count() == 1
    assert user_1.firstname == "John"
    assert user_1.lastname == "Doe"
    assert user_1.password != "12345678"
    assert user_1.occupation == "Student"

