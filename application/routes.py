from flask import render_template, redirect, url_for, flash, request
from application.Add_hazard_form import HazardForm
from application.searchdb import searchdb
from application import db
from application.models import MSDS, hazard
from application import app


@app.route('/', methods=['GET'])
@app.route('/home', methods=['GET'])
def homepage():
    q = request.args.get('q')
    if q:
        data = searchdb(q)
        return render_template('search.html',data=data)
    return render_template('homepage.html')


@app.route('/addmsds', methods=['GET', 'POST'])
def addmsds_page():
    form = HazardForm()
    if form.validate_on_submit():
        msds_to_create = MSDS(name=form.name.data,
                              cas=form.cas.data,
                              internal=form.internal.data,
                              year=form.year.data,
                              user=form.user.data,
                              vendor=form.vendor.data,
                              comments=form.comments.data)
        db.session.add(msds_to_create)
        db.session.commit()
        return redirect(url_for('msds'))
    return render_template('addmsds.html', form=form)


@app.route('/MSDS')
def msds():
    data = MSDS.query.all()
    return render_template('msds.html', data=data)


@app.route('/hazards')
def hazards():
    hazard = [
        {'Assessment': 'Ladder Use', 'ProductRef': 'Cell Bank', 'Year': 2022, 'User': 'davidli', 'Comments': 'Ladder usage in cell banking area'},
        {'Assessment': 'Forklift Usage', 'ProductRef': 'NA', 'Year': 2022, 'User': 'davidli',
         'Comments': 'Forklift usage plant wide assessment'},
        {'Assessment': 'Product Milling', 'ProductRef': 'Secret X', 'Year': 2022, 'User': 'davidli',
         'Comments': 'Ergonomic Assessment of milling activities for secret x product'},
        {'Assessment': 'Welder Usage', 'ProductRef': 'NA', 'Year': 2022, 'User': 'davidli',
         'Comments': 'Site wide assessment of welder usage'}
    ]
    return render_template('hazards.html', hazard=hazard)


@app.route('/delete')
def delete():
    return render_template('delete.html')


@app.route('/yes')
def yes():
    return render_template('no.html')


@app.route('/no')
def no():
    return render_template('no.html')

@app.route('/search', methods=['POST'])
def search():
    q = request.args.get('q')
    if q:
        data = searchdb(q)
        return render_template('search.html',data=data)
    else:
        return render_template('search.html')
