from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import InputRequired, Length


class UpdateForm(FlaskForm):
    """
    Form for singup
    """
    firstName = StringField('First Name ', validators=[InputRequired(), Length(min=4, max= 20)])
    lastName = StringField('Last Name', validators=[InputRequired(), Length(min=4, max=20)])
