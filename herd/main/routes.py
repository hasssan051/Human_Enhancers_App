from flask import Blueprint

from flask import render_template

main = Blueprint('main',__name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html',title="HERD 1.0")


@main.route("/about")
def about():
    return render_template('about.html', title='About')


# @main.route("/search_table")
# def search_table():
#     return render_template('search_table.html', title='Search Further')


@main.route("/help")
def help():
    return render_template('help.html', title='Help')
