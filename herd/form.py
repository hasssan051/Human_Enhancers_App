from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField, SubmitField, BooleanField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired(),Length(min=2,max=26)])
    lastname = StringField('Last Name', validators=[DataRequired(),Length(min=2,max=26)])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), Length(min=8),EqualTo('password')])
    occupation = SelectField('Occupation',choices=['Student','Researcher','Random Dude','With an Organization','Explorer'])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Log in')