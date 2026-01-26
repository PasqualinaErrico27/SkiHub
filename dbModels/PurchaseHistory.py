from dbModels.db import db

class Purchase(db.Model):
    __tablename__ = "purchase"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    resort_id = db.Column(db.Integer, db.ForeignKey("resort.id"))
    item = db.Column(db.String(255))
    date = db.Column(db.DateTime)
    amount = db.Column(db.Float)
