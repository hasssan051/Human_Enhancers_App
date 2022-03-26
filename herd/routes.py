from flask import render_template, url_for,flash, redirect, request
from herd.form import RegistrationForm, LoginForm, UpdateAccountForm
from herd.models import User,UserSearches
from herd import app, bcrypt, db
from flask_login import login_user,current_user,logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="HERD 1.0")

@app.route("/search")
def search():
    return render_template('search.html', title='Query the Database')

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/search_table")
def search_table():
    return render_template('search_table.html', title='Search Further')

@app.route("/help")
def help():
    return render_template('help.html', title='Help')

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(firstname=form.firstname.data, lastname=form.lastname.data, email=form.email.data, password=hashed_password, occupation=form.occupation.data)
        db.session.add(user)
        db.session.commit()
        flash(f' Account Created! Login to HERD {form.firstname.data}!','success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Join Today', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f' You have been logged in!','success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check email and password.','danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account',methods=['GET','POST'])
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
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.firstname.data = current_user.firstname
        form.lastname.data = current_user.lastname
        form.email.data = current_user.email
        form.occupation.data = current_user.occupation
    return render_template('account.html', title='Account',form=form)