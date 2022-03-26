from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField,PasswordField, SubmitField, BooleanField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from herd.models import User

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(),Length(min=2,max=26)])
    lastname = StringField('Last Name', validators=[DataRequired(),Length(min=2,max=26)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8),EqualTo('password')])
    occupation = SelectField('Occupation',choices=['Student','Researcher','Random Dude','With an Organization','Explorer'])
    submit = SubmitField('Sign Up')

    # function to check whether email already exists in db
    def validate_email(self,email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is already taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Log in')


class UpdateAccountForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(),Length(min=2,max=26)])
    lastname = StringField('Last Name', validators=[DataRequired(),Length(min=2,max=26)])
    email = StringField('Email')
    occupation = SelectField('Occupation',choices=['Student','Researcher','Self-Employed','With an Organization','Explorer'])
    submit = SubmitField('Update')

    