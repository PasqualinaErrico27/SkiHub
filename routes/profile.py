from flask import session, redirect, url_for, render_template, Blueprint, request
from werkzeug.security import generate_password_hash

from dbModels.Purchase import Purchase
from dbModels.User import User
from dbModels.db import db

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login.login"))

    user = User.query.get(session["user_id"])


    if user.role == "admin":
        return redirect(url_for("admin.dashboard"))

    if not user:
        session.clear()
        return redirect(url_for("login.login"))
    purchases = Purchase.query.filter_by(user_id=user.id).all()
    return render_template(
        "profile.html",
        user=user,
        purchases=purchases
    )

@profile_bp.route("/profile/delete_booking/<int:purchase_id>", methods=["POST"])
def delete(purchase_id):
    purchase = Purchase.query.get_or_404(purchase_id)
    db.session.delete(purchase)
    db.session.commit()
    return redirect(url_for("profile.profile"))

@profile_bp.route("/profile/changepwd", methods=["POST"])
def changepwd():
    user_id = session["user_id"]
    user = User.query.get(user_id)
    password = request.form["password"]
    print(password)
    hashed_password = generate_password_hash(
        password,
        method="pbkdf2:sha256",
        salt_length=16
    )
    user.password = hashed_password
    return render_template("profile.html", user=user)