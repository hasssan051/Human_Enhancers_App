from flask import Blueprint
from flask import  render_template, url_for, flash, redirect, request
from itsdangerous import json
from herd.users.forms import RegistrationForm, LoginForm, UpdateAccountForm
from herd.models import User
from herd import bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required
users = Blueprint('users',__name__)


@users.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
            form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data,
                    email=form.email.data, password=hashed_password, occupation=form.occupation.data)
        db.session.add(user)
        db.session.commit()
        flash(
            f' Account Created! Login to HERD {form.firstname.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Join Today', form=form)


@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f' You have been logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash(f'Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.firstname = form.firstname.data
        current_user.lastname = form.lastname.data
        #current_user.email = current_user.email
        current_user.occupation = form.occupation.data
        db.session.commit()
        flash("Your Account has been Updated!", 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.email.data = current_user.email
        form.occupation.data = current_user.occupation
    return render_template('account.html', title='Account', form=form)


