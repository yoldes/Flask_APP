from . import display
from flask_login import login_required
from flask import render_template, request
from app.models import User
from .forms import UserData


@display.route('/data', methods=["GET","POST"])
@login_required
def update():

    values = User.query.all()
    form = UserData()

    if request.method == 'POST' and form.validate_on_submit():

        return render_template("/dashboard.html")

    return render_template("dataDisplay.html", values=values, form=form)
