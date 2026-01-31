from datetime import datetime

from flask import Blueprint, request, render_template, jsonify
from werkzeug.security import generate_password_hash

from dbModels.db import db
from dbModels.User import User

register_bp = Blueprint("register", __name__)

@register_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")

    if not request.is_json:
        print("Content-Type non JSON:", request.content_type)
        return jsonify({"error": "Invalid Content-Type"}), 415

    data = request.get_json()
    print("DATA RECEIVED:", data)

    try:
        hashed_password = generate_password_hash(
            data["password"],
            method="pbkdf2:sha256",
            salt_length=16
        )

        user = User(
            username=data["username"],
            first_name=data["firstname"],
            last_name=data["lastname"],
            birth_date=datetime.strptime(
                data["dateOfBirth"], "%Y-%m-%d"
            ).date(),
            email=data["email"],
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return jsonify({"success": True}), 200

    except Exception as e:
        db.session.rollback()
        print("REGISTER ERROR:", type(e).__name__, e)
        return jsonify({"success": False, "error": str(e)}), 400
