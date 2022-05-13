from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class HazardForm(FlaskForm):
    name = StringField(label='Name:')
    cas = StringField(label='CAS No.')
    internal = StringField(label='Internal Ref. No.')
    year = StringField(label='Year:')
    user = StringField(label='User:')
    vendor = StringField(label='Vendor')
    comments = StringField(label='Comments:')
    submit = SubmitField(label='Create MSDS')