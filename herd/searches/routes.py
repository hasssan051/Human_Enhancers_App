from flask import jsonify, render_template, flash, session
from herd.searches.forms import QueryForm
from herd.models import UserSearches, experiments, merged_peak, mp_overlap_vista,vista
from herd import db
from herd.searches.utils import return_search_result
from flask_login import current_user

from flask import Blueprint

searches = Blueprint('searches', __name__)


@searches.route("/search", methods=['GET', 'POST'])

def search():
    form = QueryForm()
    query_system = db.session.query(
        experiments.system.distinct().label("system"))
    form.system.choices = ['Any']
    form.system.choices += [row.system for row in query_system.all()]

    if form.validate_on_submit():
        if current_user.is_authenticated:
            user_query = UserSearches(chromosome=form.chromosome.data, chromStart=form.chromStart.data, chromEnd=form.chromEnd.data, system=form.system.data,
                                      tissue=form.tissue.data, organ=form.organ.data, treated=form.treated.data, disease=form.disease.data, user_id=current_user.id)
            db.session.add(user_query)
            db.session.commit()
        # starting here we query the HERD database
        result = return_search_result(chrom=form.chromosome.data, chromStart=form.chromStart.data, chromEnd=form.chromEnd.data, system=form.system.data,
                                    tissue=form.tissue.data, organ=form.organ.data, treated=form.treated.data, disease=form.disease.data)
        # session["herd_query_form"] = form
        return render_template('search.html', title='Query the Database', form=form, result=result)
    return render_template('search.html', title='Query the Database', form=form)

# @searches.route("/", methods=['GET', 'POST'])


@searches.route("/organ/<system>")
def organ(system):
    if system != 'Any':
        organs = db.session.query(
            experiments.organ.distinct()).filter_by(system=system).all()
        organArray = []
        organArray.append({'organ': 'Any'})
        for organ in organs:
            organObj = {}
            organObj['organ'] = organ[0]
            organArray.append(organObj)
        return jsonify({'organs': organArray})
    return jsonify({'organs': [{'organ': 'Any'}]})


@searches.route("/tissue/<organ>")
def tissue(organ):
    if organ != 'Any':
        tissues = db.session.query(
            experiments.tissue.distinct()).filter_by(organ=organ).all()
        tissueArray = []
        tissueArray.append({'tissue': 'Any'})
        for tissue in tissues:
            tissueObj = {}
            tissueObj['tissue'] = tissue[0]
            tissueArray.append(tissueObj)
        return jsonify({'tissues': tissueArray})
    return jsonify({'tissues': [{'tissue': 'Any'}]})





# @searches.route('/api/data')
# def data():
#     return {'data': []}