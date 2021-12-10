from flask_wtf import FlaskForm
from wtforms import  PasswordField, StringField
from wtforms.validators import InputRequired, Length, Email


class RegisterFrom(FlaskForm):
    """
    Form for singup
    """
    firstName = StringField('First Name ', validators=[InputRequired(), Length(min=4, max= 20)])
    lastName = StringField('Last Name', validators=[InputRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[InputRequired(), Email(message=' Invalid adress'), Length(min=5, max=50)])
    password = PasswordField('Password', validators=[InputRequired(), Length(min=5, max=50)])