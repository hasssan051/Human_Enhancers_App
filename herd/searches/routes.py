from flask import jsonify, render_template, flash, request
from herd.searches.forms import QueryForm
from herd.models import UserSearches, experiments, merged_peak, mp_overlap_vista,vista
from herd import db
from herd.searches.utils import return_search_result,return_if_result_zero
from flask_login import current_user,login_required

from flask import Blueprint

searches = Blueprint('searches', __name__)


@searches.route("/search", methods=['GET', 'POST'])
def search():
    form = QueryForm()
    query_system = db.session.query(
        experiments.system.distinct().label("system"))
    form.system.choices = ['All']
    form.system.choices += [row.system for row in query_system.all()]
    if request.method:
        form.query_history.data = 'None'
    if form.validate_on_submit():
        if current_user.is_authenticated:
            user_query = UserSearches(chromosome=form.chromosome.data, chromStart=form.chromStart.data, chromEnd=form.chromEnd.data, system=form.system.data,
                                      tissue=form.tissue.data, organ=form.organ.data, treated=form.treated.data, disease=form.disease.data, user_id=current_user.id)
            db.session.add(user_query)
            db.session.commit()
        # starting here we query the HERD database
        result = return_search_result(chrom=form.chromosome.data, chromStart=form.chromStart.data, chromEnd=form.chromEnd.data, system=form.system.data,
                                    tissue=form.tissue.data, organ=form.organ.data, treated=form.treated.data, disease=form.disease.data)
        category = "success"
        message = f"Successfully found {len(result)} ACRs in area specified"
        if len(result) < 1:
            result = return_if_result_zero(form.chromosome.data, chromStart=form.chromStart.data, chromEnd=form.chromEnd.data)
            message = f"Failed to find any enhancers in specified region, showing {len(result)} closest enhancer/s"
            category = "info"
        flash(message,category)
        return render_template('search.html', title='Query the Database', form=form, result=result)
    return render_template('search.html', title='Query the Database', form=form)




@searches.route("/organ/<system>")
def organ(system):
    if system != 'All':
        organs = db.session.query(
            experiments.organ.distinct()).filter_by(system=system).all()
        organArray = []
        organArray.append({'organ': 'All'})
        for organ in organs:
            organObj = {}
            organObj['organ'] = organ[0]
            organArray.append(organObj)
        return jsonify({'organs': organArray})
    return jsonify({'organs': [{'organ': 'All'}]})


@searches.route("/tissue/<organ>")
def tissue(organ):
    if organ != 'All':
        tissues = db.session.query(
            experiments.tissue.distinct()).filter_by(organ=organ).all()
        tissueArray = []
        tissueArray.append({'tissue': 'All'})
        for tissue in tissues:
            tissueObj = {}
            tissueObj['tissue'] = tissue[0]
            tissueArray.append(tissueObj)
        return jsonify({'tissues': tissueArray})
    return jsonify({'tissues': [{'tissue': 'All'}]})



@searches.route("/api/prevQueries")
@login_required
def prevQueries():
    searches = UserSearches.query.filter(UserSearches.user_id==current_user.get_id()).all()
    searches_array = [{'search': 'None'}] + [{'search':search.to_dict()} for search in searches][::-1]
    return jsonify({'searches': searches_array})
    

# @searches.route('/api/data')
# def data():
#     return {'data': []}