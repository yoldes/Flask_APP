from . import update
from flask_login import login_required
from flask import render_template, request, flash
from app import db
from .forms import UpdateForm
from app.models import User


@update.route('/update/<int:id>', methods=['GET', 'POST'])
@login_required
def update(id):
    form = UpdateForm()
    user_update = User.query.get_or_404(id)

    if request.method == "POST" and form.validate_on_submit():
        user_update.firstname = request.form['firstName']
        user_update.lastname = request.form['lastName']
        try:
            db.session.commit()
            return render_template("dashboard.html", form=form, user_update=user_update)
        except:

            flash("Oups, Something wrong")
            return render_template("update.html", form=form, user_update=user_update)
    else:
        return render_template("update.html", form=form, user_update=user_update)


