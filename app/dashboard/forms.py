from flask_wtf import FlaskForm
from wtforms import SubmitField


class UserData(FlaskForm):

    user_data = SubmitField(label='Send')

