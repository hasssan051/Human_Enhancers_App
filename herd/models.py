from herd import db, login_manager
from sqlalchemy import ForeignKey
from flask_login import UserMixin
from sqlalchemy.dialects.mysql import INTEGER

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
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
    chromosome = db.Column(db.String(30),nullable=False)
    chromStart = db.Column(db.Integer,nullable=False)
    chromEnd = db.Column(db.Integer,nullable=False)
    system = db.Column(db.String(50))
    organ = db.Column(db.String(50))
    tissue = db.Column(db.String(50))
    treated = db.Column(db.Boolean)
    disease = db.Column(db.Boolean)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'),nullable=False)

    def __repr__(self):
        return f"Search('{self.chromosome}', '{self.chromStart}', '{self.chromEnd}', '{self.tissue}', '{self.organ}', '{self.treated}', '{self.disease}', '{self.user_id}')"


class experiment_table(db.Model):
    __bind_key__ = 'herd'
    experimentAccession = db.Column(db.String(50),nullable=False)
    system = db.Column(db.String(500),nullable=False)
    organ = db.Column(db.String(500),nullable=False)
    tissue = db.Column(db.String(1000),nullable=False)
    treated = db.Column(db.String(20))
    diseased = db.Column(db.String(20))
    biosampleSummary = db.Column(db.String(1000))
    Description = db.Column(db.String(1000))
    lifeStage = db.Column(db.String(45))
    biosampleAge = db.Column(db.String(100))
    narrowPeaksAccession = db.Column(db.String(100),primary_key=True, nullable=False)

class erna(db.Model):
    __bind_key__ = 'herd'
    ernaId = db.Column(db.Integer,primary_key=True, nullable=False)
    chrom = db.Column(db.String(10))
    chromStart = db.Column(INTEGER(unsigned=True),nullable=False)
    chromEnd = db.Column(INTEGER(unsigned=True),nullable=False)
    name = db.Column(db.String(100), unique=True)

class merged_peak(db.Model):
    __bind_key__ = 'herd'
    mergedPeakId = db.Column(db.Integer,primary_key=True, nullable=False)
    chrom = db.Column(db.String(5),nullable=False)
    herdAccessionNum = db.Column(db.String(50),nullable=False,unique=True)
    chromStart = db.Column(db.Integer,nullable=False)
    chromEnd = db.Column(db.Integer,nullable=False)
    Prefixes = db.Column(db.String(10),nullable=False)
    Location = db.Column(db.String(50))

class vista(db.Model):
    __bind_key__ = 'herd'
    chrom = db.Column(db.String(10),nullable=False)
    chromStart = db.Column(db.Integer,nullable=False)
    chromEnd = db.Column(db.Integer,nullable=False)
    vistaId = db.Column(db.Integer,primary_key=True,nullable=False)

class erna_in_mp(db.Model):
    __bind_key__ = 'herd'
    mergedPeakId = db.Column(db.Integer,db.ForeignKey('merged_peak.mergedPeakId'),primary_key=True, nullable=False)
    ernaId = db.Column(db.Integer,db.ForeignKey('erna.ernaId'),primary_key=True,nullable=False)
    
