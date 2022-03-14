from herd import db
from sqlalchemy import ForeignKey

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    lastname = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60),nullable=False)
    occupation = db.Column(db.String(20))
    searches = db.relationship('UserSearches',backref='searches',lazy=True)
    # prints out the object
    def __repr__(self):
        return f"User('{self.firstname}', '{self.lastname}', '{self.email}', '{self.occupation}')"

class UserSearches(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Search('{self.query}','{self.user_id}')"
