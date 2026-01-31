from flask import Blueprint, render_template, request, redirect, url_for, session,jsonify
from dbModels.db import db
from dbModels.Resort import Resort
from dbModels.Slope import Slope
from dbModels.User import admin_required
from dbModels.Lift import Lift

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')

@admin_bp.route('/dashboard')
@admin_required
def dashboard():
    adminid= session["user_id"]
    resorts = Resort.query.filter(Resort.admin_id == adminid).all()
    return render_template("dashboard.html",resorts=resorts)


@admin_bp.route('/resort/new', methods=['GET', 'POST'])
@admin_required
def new_resort():
    if request.method == "GET":
        return render_template("resort_form.html")

    data = request.get_json()

    resort = Resort(
        name=data['nome'],
        region=data['region'],
        altitude_min=data['min'],
        altitude_max=data['max'],
        price=data['price'],
        admin_id=session['user_id'],
    )

    db.session.add(resort)
    db.session.commit()

    return jsonify({
        "success": True,
        "redirect": url_for("admin.dashboard")
    })


@admin_bp.route("/resort/<int:resort_id>/edit", methods=["GET", "POST"])
@admin_required
def edit_resort(resort_id):
    resort = Resort.query.get_or_404(resort_id)

    if request.method == "POST":
        resort.name = request.form["name"]
        resort.region = request.form["region"]
        resort.altitude_min = request.form["altitude_min"]
        resort.altitude_max = request.form["altitude_max"]

        db.session.commit()
        return redirect(url_for("admin.dashboard"))

    return render_template("resort_edit.html", resort=resort)

@admin_bp.route("/resort/<int:resort_id>/lifts", methods=["GET","POST"])
@admin_required
def add_lift(resort_id):
    if request.method == "POST":
        lift = Lift(
        name=request.form["name"],
        type=request.form["type"],
        capacity=request.form["capacity"],
        resort_id=resort_id
    )
        db.session.add(lift)
        db.session.commit()
        return redirect(url_for("admin.edit_resort", resort_id=resort_id))
    return render_template("new_lift.html",resort_id=resort_id)

@admin_bp.route("/resort/<int:resort_id>/slopes", methods=["GET", "POST"])
@admin_required
def add_slope(resort_id):
    if request.method == "POST":
        slope = Slope(
            name=request.form["name"],
            difficulty=request.form["difficulty"],
            length_km=request.form["length_km"],
            resort_id=resort_id
        )
        db.session.add(slope)
        db.session.commit()
        return redirect(url_for("admin.edit_resort", resort_id=resort_id))

    return render_template("new_slope.html", resort_id=resort_id)
