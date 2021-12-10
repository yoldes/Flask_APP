from flask import Blueprint

testlimiter = Blueprint('testLimiter', __name__)

from . import views