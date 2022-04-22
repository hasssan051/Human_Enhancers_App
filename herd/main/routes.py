from flask import Blueprint,url_for
import pandas as pd
import os
from flask import render_template

main = Blueprint('main',__name__,template_folder='templates',static_folder='static')


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
    return render_template('help.html', title='HERD App Documentation')

@main.route("/api/documentation_table")
def documentation_table():
    # find a better way to read this csv, right now it is an absolute path
    doc_table = pd.read_csv('C:\Putative_Enhancers_App\herd\static\imgs_documentation\documentation_table.csv',sep=',')
    #os.path.join(os.getcwd(),url_for('static',filename='imgs_documentation/documentation_table.csv')
    
    return {'data': doc_table.to_dict('records')}


