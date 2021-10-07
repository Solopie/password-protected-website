from flask import Blueprint, render_template, request, redirect ,url_for, session
from util import generate_hash, verify_access
from db import access_db
import config

access_bp = Blueprint("access", __name__, template_folder="templates")

@access_bp.route("/", methods=["GET", "POST"])
def login():
    if "access" in session and session["access"] == True:
        return redirect(url_for("index"))

    if request.method == "POST":
        token = request.form.get("token")
        if verify_access(token):
            session["access"] = True 
            return redirect(url_for("index"))
        else:
            return render_template("login.html", error="Access failed")

    return render_template("login.html")

@access_bp.route("/setup", methods=["GET", "POST"])
def setup():
    # Shouldn't be able to setup token if already set
    if config.SETUP_REQUIRED == False:
        return "Setup already completed"

    if request.method == "POST":
        token = request.form.get("token")
        key,salt = generate_hash(token)
        access_db.query("INSERT INTO tokens VALUES (?,?)", (key,salt), True)
        config.SETUP_REQUIRED = False
        return redirect(url_for(".login"))

    return render_template("setup.html")
