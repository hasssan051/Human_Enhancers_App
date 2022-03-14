from flask import render_template, url_for,flash, redirect, request
from herd.form import RegistrationForm, LoginForm
from herd.models import User,UserSearches
from herd import app


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Putative Enhancer Database")

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f' You can now start using ENHANCER DB {form.firstname.data}!','success')
        return redirect(url_for('search'))
    return render_template('register.html', title='Join Today', form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f' You have been logged in!','success')
        return redirect(url_for('search'))
    return render_template('login.html', title='Login', form=form)
