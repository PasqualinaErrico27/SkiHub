from flask import session, redirect, url_for, render_template, Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash

from dbModels.Purchase import Purchase
from dbModels.User import User
from dbModels.db import db

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
def profile():
    if "user_id" not in session:
        return redirect(url_for("login.login"))

    user = User.query.get(session["user_id"])

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
@profile_bp.route("/profile/changepwd", methods=["POST"])
def changepwd():
    if "user_id" not in session:
        return jsonify(error="Non autenticato"), 401

    data = request.get_json() or {}
    old = data.get("old_password")
    new = data.get("new_password")

    if not old or not new:
        return jsonify(error="Dati mancanti"), 400

    user = User.query.get(session["user_id"])

    if not check_password_hash(user.password, old):
        return jsonify(error="Password attuale errata")

    user.password = generate_password_hash(new)
    db.session.commit()

    return jsonify(success=True)

@profile_bp.route("/profile/update", methods=["POST"])
def update_profile():
    if "user_id" not in session:
        return jsonify(error="Non autenticato"), 401

    data = request.get_json()
    user = User.query.get(session["user_id"])

    user.first_name = data["firstname"]
    user.last_name = data["lastname"]
    user.email = data["email"]

    db.session.commit()
    return jsonify(success=True)
