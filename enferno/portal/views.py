from flask import Blueprint
from flask.templating import render_template
from flask_security import auth_required, current_user

from enferno.user.models import Activity, Role, User

portal = Blueprint("portal", __name__, static_folder="../static")


@portal.before_request
@auth_required("session")
def before_request():
    pass


@portal.route("/dashboard/")
def dashboard():
    stats = {}
    if current_user.has_role("admin"):
        stats = {
            "users": User.query.count(),
            "roles": Role.query.count(),
            "activities": Activity.query.count(),
        }
    return render_template("dashboard.html", stats=stats)
