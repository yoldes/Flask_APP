from flask import Blueprint


index = Blueprint('admin', __name__)


@index.route('/', methods=['GET'])
def home():
    return 'Done'


