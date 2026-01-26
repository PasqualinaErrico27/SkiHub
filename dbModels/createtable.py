from app import app
# NON RUNNARE A CASO
from dbModels.db import db
from dbModels.PurchaseHistory import Purchase
from dbModels.User import User
from dbModels.Resort import Resort
from dbModels.Lift import Lift
from dbModels.Slope import Slope
from dbModels.SavedResort import SavedResort

with app.app_context():
    db.drop_all()
    db.create_all()
