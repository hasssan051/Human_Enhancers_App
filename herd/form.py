from flask import Flask
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,NumberRange, AnyOf
from herd.models import User


class RegistrationForm(FlaskForm):
    firstname = StringField('First Name', validators=[
                            DataRequired(), Length(min=2, max=26)])
    lastname = StringField('Last Name', validators=[
                           DataRequired(), Length(min=2, max=26)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[
                                     DataRequired(), Length(min=8), EqualTo('password')])
    occupation = SelectField('Occupation', choices=[
                             'Student', 'Researcher', 'Random Dude', 'With an Organization', 'Explorer'])
    submit = SubmitField('Sign Up')

    # function to check whether email already exists in db
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                'That email is already taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[
                             DataRequired(), Length(min=8)])
    remember = BooleanField('Remember Me')

    submit = SubmitField('Log in')


class UpdateAccountForm(FlaskForm):
    firstname = StringField('First Name', validators=[
                            DataRequired(), Length(min=2, max=26)])
    lastname = StringField('Last Name', validators=[
                           DataRequired(), Length(min=2, max=26)])
    email = StringField('Email')
    occupation = SelectField('Occupation', choices=[
                             'Student', 'Researcher', 'Self-Employed', 'With an Organization', 'Explorer'])
    submit = SubmitField('Update')


def validate_chromStart_chromEnd(form,chromEnd):
    if chromEnd.data<= form.chromStart.data:
        raise ValidationError('chromEnd must be larger than chromStart')


def validate_chromosome(form,chromosome):
    if chromosome.data == 'None':
        raise ValidationError('Please select a chromosome value')

class QueryForm(FlaskForm):
    chromosome = SelectField('Chromosome', choices=['None','chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10',
                             'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY'], validators=[AnyOf(['chr1', 'chr2', 'chr3', 'chr4', 'chr5', 'chr6', 'chr7', 'chr8', 'chr9', 'chr10',
                             'chr11', 'chr12', 'chr13', 'chr14', 'chr15', 'chr16', 'chr17', 'chr18', 'chr19', 'chr20', 'chr21', 'chr22', 'chrX', 'chrY'],'Please select a chromosome value')])
    chromStart = IntegerField('chromStart',validators=[DataRequired(),NumberRange(min=1,message='Please provide a number above 1')])
    chromEnd = IntegerField('chromEnd',validators=[DataRequired(),NumberRange(min=1,message='Please provide a number above 1'),validate_chromStart_chromEnd])
    system = SelectField('System',choices=['None','Embryo','Musculoskeletal','Integumentary','Endocrine','Lymphatic','Urinary','Reproductive','Circulatory','Nervous','Digestive','Respiratory'])
    organ = SelectField('Organ', choices=['Select a System first'])
    tissue = SelectField('Tissue',choices=['Select an Organ First'])
    treated = BooleanField('Treated')
    disease = BooleanField('Disease')

    submit = SubmitField('Search')

    