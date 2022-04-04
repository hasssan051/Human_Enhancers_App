from flask import jsonify, render_template
from herd.searches.forms import QueryForm
from herd.models import UserSearches, experiment_table
from herd import db
from flask_login import current_user

from flask import Blueprint

searches = Blueprint('searches',__name__)


@searches.route("/search", methods=['GET', 'POST'])
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

@searches.route("/organ/<system>")
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

@searches.route("/tissue/<organ>")
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