from flask import Blueprint, render_template, request, redirect, url_for, session
from dbModels.db import db
from dbModels.Resort import Resort
from dbModels.PurchaseHistory import Purchase

booking_bp = Blueprint("booking", __name__)

@booking_bp.route("/booking/<int:resort_id>", methods=["GET", "POST"])
def new_booking(resort_id):
    if "user_id" not in session:
        return redirect(url_for("login.login"))


    resort = Resort.query.get_or_404(resort_id)

    if request.method == "POST":
        purchase = Purchase(
            user_id=session["user_id"],
            resort_id=resort_id,
            days=request.form["days"],
            price=request.form["price"]
        )
        print("done")

        db.session.add(purchase)
        db.session.commit()
        return redirect(url_for("profile.profile"))


    return render_template("booking.html", resort=resort)
