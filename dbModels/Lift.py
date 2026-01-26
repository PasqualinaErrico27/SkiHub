from dbModels.db import db

class Lift(db.Model):
    __tablename__ = "lifts"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    capacity = db.Column(db.Integer)

    resort_id = db.Column(
        db.Integer,
        db.ForeignKey("resorts.id"),
        nullable=False
    )
