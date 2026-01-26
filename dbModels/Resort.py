from dbModels.Lift import Lift
from dbModels.Slope import Slope
from dbModels.db import db

class Resort(db.Model):
    __tablename__ = "resorts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    region = db.Column(db.String(100), nullable=False)
    altitude_min = db.Column(db.Integer)
    altitude_max = db.Column(db.Integer)

    # relazioni
    lifts = db.relationship(Lift, backref="resort", lazy=True, cascade="all, delete")
    slopes = db.relationship(Slope, backref="resort", lazy=True, cascade="all, delete")
