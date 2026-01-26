from dbModels.db import db

class Slope(db.Model):
    __tablename__ = "slopes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150))
    difficulty = db.Column(db.Enum("blu", "rossa", "nera", name="difficulty_enum"), nullable=False)
    length_km = db.Column(db.Float)

    resort_id = db.Column(
        db.Integer,
        db.ForeignKey("resorts.id"),
        nullable=False
    )
