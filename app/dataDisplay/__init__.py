from flask import Blueprint

display = Blueprint('display', __name__)

from . import views