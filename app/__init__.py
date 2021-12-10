from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
Env_config = os.environ['MYAPP_CONFIG']
app.config.from_object(Env_config)


db = SQLAlchemy(app)
Bootstrap(app)
db.init_app(app)
db.create_all()
hash = Bcrypt(app)


# Combination of app and flask_login
logManager = LoginManager(app)
logManager.init_app(app)
logManager.login_view = 'login_out'


from .login_out import login as login_blueprint
app.register_blueprint(login_blueprint)

from .singup import register as register_blueprint
app.register_blueprint(register_blueprint)

from .dashboard import dash as dash_blueprint
app.register_blueprint(dash_blueprint)

from .login_out import logout as logout_blueprint
app.register_blueprint(logout_blueprint)

from .limiter import testlimiter as testlimiter_blueprint
app.register_blueprint(testlimiter_blueprint)

from .update import update as update_blueprint
app.register_blueprint(update_blueprint)

from .dataDisplay import display as display_blueprint
app.register_blueprint(display_blueprint)

from app.models import User
