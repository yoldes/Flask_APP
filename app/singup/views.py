from . import register
from flask import render_template, flash
from .forms import RegisterFrom
from app.models import User
from app import hash, db


@register.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterFrom()
    # Available : is_submitted() | validate()
    if form.validate_on_submit():
        # Check Database existent users
        user = User.query.filter_by(email=form.email.data).first()
        if user is None:
            hashed_pass = hash.generate_password_hash(form.password.data).decode('UTF-8')
            new_user = User(firstname=form.firstName.data, lastname=form.lastName.data, email=form.email.data,
                            password=hashed_pass)
            db.session.add(new_user)
            db.session.commit()
            return 'Done'
        else:
            form.firstName.data = ' '
            form.lastName.data = ' '
            form.email.data = ' '
            form.password.data = ' '
            return 'User already exists'

    return render_template('register.html', form=form)
