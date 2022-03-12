from flask import Flask, render_template, url_for
from form import RegistrationForm, LoginForm
app = Flask(__name__)

# this secret key is used by wtforms to make shit secure 
# remember to turn this into an environment variable later on
app.config['SECRET_KEY'] = '88d99ae8d44e1eb62cd8d4f7c6dc1034'

@app.route("/home")
def home():
    return render_template('home.html', title = 'Home')

@app.route("/")
@app.route("/search")
def search():
    return render_template('search.html')


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)