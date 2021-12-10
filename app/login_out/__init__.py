from flask import Blueprint

login = Blueprint('login_out', __name__)
logout = Blueprint('logout', __name__)

from . import views