from . import testlimiter
from app import app
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address


# every time we request a route based on a specific ip address,
# flask limiter catch that ip address  from get_remote_address
# and compare (key_func return String) it to the list of ip address in the memory
limiter = Limiter(

    app,
    key_func=get_remote_address,

)


@limiter.limit("3/day")
@testlimiter.route('/limiter')
def limiter():

    return 'You only have 3 requests authorized'
