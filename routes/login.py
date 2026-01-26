from flask import Blueprint, request, render_template, jsonify, session, redirect
from werkzeug.security import check_password_hash
from dbModels.User import User

login_bp = Blueprint("login", __name__)

@login_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    data = request.get_json()

    user = User.query.filter_by(username=data["username"]).first()

    if not user:
        return jsonify({"success": False, "error": "Username non trovato"}), 401

    if not check_password_hash(user.password, data["password"]):
        return jsonify({"success": False, "error": "Password errata"}), 401

    # ✅ LOGIN OK
    session["user_id"] = user.id
    session["username"] = user.username

    print("LOGIN ROLE:", user.role)

    return jsonify({"success": True}), 200

@login_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")