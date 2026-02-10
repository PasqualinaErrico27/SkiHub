from dbModels.db import db
from functools import wraps
from flask import session,redirect,url_for,abort

class User(db.Model):
    __tablename__ = "user"  # obbligatorio per allineamento con il DB

    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(5), default='user', nullable=False)
    username = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=False)
    last_name = db.Column(db.String(255), nullable=False)
    birth_date = db.Column(db.Date, nullable=False)
    password = db.Column(db.String(255), nullable=False)



def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login.login'))
        user = User.query.get(session['user_id'])
        if user.role != 'admin' or not user:
            abort(403)
        return f(*args, **kwargs)
    return decorated_function
