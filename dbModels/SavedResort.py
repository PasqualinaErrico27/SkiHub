from dbModels.db import db

class SavedResort(db.Model):
    __tablename__ = "saved_resort"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    name = db.Column(db.String(255))
    region = db.Column(db.String(255))
