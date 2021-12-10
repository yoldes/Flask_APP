from app import db, logManager
from flask_login import UserMixin


# Set up user_loader
@logManager.user_loader
def load_user(ident):
    return User.query.get(int(ident))


class User(db.Model, UserMixin):
    """
    Adding id(primary key)
    ensures that email set is unique
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstname = db.Column(db.String(40),  nullable=False)
    lastname = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(80), nullable=False, unique=True)
    password = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<User: {}>'.format(self.email)


