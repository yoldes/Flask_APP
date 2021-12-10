from flask_wtf import FlaskForm
from wtforms import SubmitField


class UserData(FlaskForm):

    submit = SubmitField(label='Back')

