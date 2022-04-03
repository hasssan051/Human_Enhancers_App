from flask import jsonify, render_template, url_for, flash, redirect, request
from itsdangerous import json
from herd.form import RegistrationForm, LoginForm, UpdateAccountForm, QueryForm
from herd.models import User, UserSearches, experiment_table
from herd import app, bcrypt, db
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="HERD 1.0")


@app.route("/search", methods=['GET', 'POST'])
def search():
    form = QueryForm()
    query_system = db.session.query(experiment_table.system.distinct().label("system"))
    form.system.choices = ['None']
    form.system.choices += [row.system for row in query_system.all()]

    if form.validate_on_submit():
        if current_user.is_authenticated:
            user_query = UserSearches(chromosome=form.chromosome.data, chromStart=form.chromStart.data, chromEnd=form.chromEnd.data, system=form.system.data,
                                      tissue=form.tissue.data, organ=form.organ.data, treated=form.treated.data, disease=form.disease.data, user_id=current_user.id)
            db.session.add(user_query)
            db.session.commit()
        # starting here we query the HERD database
        if form.system.value == 'None':
            pass
        else: 
            if form.organ.value == 'None':
                pass
            else:
                if form.tissue.value == 'None':
                    pass

    return render_template('search.html', title='Query the Database', form=form)

@app.route("/organ/<system>")
def organ(system):
    if system != 'None':
        organs = db.session.query(experiment_table.organ.distinct()).filter_by(system=system).all()
        organArray = []
        organArray.append({'organ':'None'})
        for organ in organs:
            organObj = {}
            organObj['organ'] = organ[0] 
            organArray.append(organObj)
        return jsonify({'organs':organArray})
    return jsonify({'organs':[{'organ':'Select a System First'}]})

@app.route("/tissue/<organ>")
def tissue(organ):
    if organ != 'None':
        tissues = db.session.query(experiment_table.tissue.distinct()).filter_by(organ=organ).all()
        tissueArray = []
        tissueArray.append({'tissue':'None'})
        for tissue in tissues:
            tissueObj = {}
            tissueObj['tissue'] = tissue[0] 
            tissueArray.append(tissueObj)
        return jsonify({'tissues':tissueArray})
    return jsonify({'tissues':[{'tissue':'Select an Organ First'}]})


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/search_table")
def search_table():
    return render_template('search_table.html', title='Search Further')


@app.route("/help")
def help():
    return render_template('help.html', title='Help')


@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
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
        return redirect(url_for('login'))
    return render_template('register.html', title='Join Today', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            flash(f' You have been logged in!', 'success')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check email and password.', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/account', methods=['GET', 'POST'])
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
    return render_template('account.html', title='Account', form=form)
