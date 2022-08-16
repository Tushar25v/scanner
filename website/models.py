from . import db
from flask_login import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class Data(db.Model):
    id= db.Column(db.Text(1000),primary_key=True)
    SYMBOL = db.Column(db.REAL(1000))
    OPEN = db.Column(db.REAL(1000))
    HIGH = db.Column(db.REAL(1000))
    LOW = db.Column(db.REAL(1000))
    CLOSE = db.Column(db.REAL(1000))
    LAST = db.Column(db.REAL(1000))
    PREVCLOSE = db.Column(db.REAL(1000))
    TOTTRDQTY = db.Column(db.REAL(1000))
    TOTTRDVAL = db.Column(db.REAL(1000))
    TOTALTRADES = db.Column(db.REAL(1000))
