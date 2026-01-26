from flask import session, redirect, url_for, render_template, Blueprint, request
from dbModels.SavedResort import SavedResort
from dbModels.PurchaseHistory import Purchase
from dbModels.db import db
from dbModels.User import User

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login.login"))

    user = User.query.get(session["user_id"])

    if user.role == "admin":
        return render_template("dashboard.html", user=user)

    if not user:
        session.clear()
        return redirect(url_for("login.login"))
    purchases = Purchase.query.filter_by(user_id=user.id).all()
    saved_resorts = SavedResort.query.filter_by(user_id=user.id).all()

    return render_template(
        "profile.html",
        user=user,
        purchases=purchases,
        saved_resorts=saved_resorts
    )

@profile_bp.route("/save",methods=["POST"])
def save():
    if "user_id" not in session:
        return {"success": False}, 401
    data = request.get_json()

    try:
        saved = SavedResort(user_id=session["user_id"],name = data["name"],region = data["region"])
        db.session.add(saved)
        db.session.commit()
    except Exception as e:
        print(e)
        return {"success": False}, 500
    return {"success": True}