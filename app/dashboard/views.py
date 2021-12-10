from . import dash
from flask_login import login_required
from flask import render_template


@dash.route('/dashbord')
@login_required
def dashboard():

    return render_template("/dashboard.html")

