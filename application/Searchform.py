from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class SearchForm(FlaskForm):
    search = StringField(label='Search:')
    submit = SubmitField(label='Search')

