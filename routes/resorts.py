from flask import Blueprint, render_template
from dbModels.Resort import Resort

resort_bp = Blueprint("resort", __name__)

@resort_bp.route("/resort/<int:resort_id>")
def resort_detail(resort_id):
    resort = Resort.query.get_or_404(resort_id)

    return render_template(
        "resort_detail.html",
        resort=resort
    )
