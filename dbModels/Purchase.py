from dbModels.db import db

class Purchase(db.Model):
    __tablename__ = "purchase"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    resort_id = db.Column(db.Integer, db.ForeignKey("resorts.id"))
    datefrom = db.Column(db.DateTime)
    dateto = db.Column(db.DateTime)
    count = db.Column(db.Integer)
    amount = db.Column(db.Float)