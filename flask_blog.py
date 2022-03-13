from flask import Flask, render_template, url_for,flash, redirect
from form import RegistrationForm, LoginForm
app = Flask(__name__)

# this secret key is used by wtforms to make shit secure 
# remember to turn this into an environment variable later on
app.config['SECRET_KEY'] = '88d99ae8d44e1eb62cd8d4f7c6dc1034'

@app.route("/")
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


if __name__ == '__main__':
    app.run(debug=True)