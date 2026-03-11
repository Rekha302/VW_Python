



from flask import Blueprint, render_template, request, redirect, session
from models import User

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username, password=password).first()

        if user:

            session["user_id"] = user.id
            session["role"] = user.role

            return redirect("/employees")

    return render_template("login.html")