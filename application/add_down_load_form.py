from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

class Downloadform(FlaskForm):
    criteria = StringField(label='Criteria:')
    submit = SubmitField(label='Download')