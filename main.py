from flask import Flask, request, session, render_template, redirect, url_for
from blueprints.access import access_bp
from db import access_db
import config

app = Flask(__name__)
app.secret_key = config.APP_KEY

# Only enable access functionality if enabled
if config.ENABLE_TOKEN:
    @app.before_first_request
    def setup():
        # ----- CHECK IF ACCESS (SETUP) REQUIRED -----
        # Check if token is set already for application (incase of restart)
        if len(access_db.query("SELECT * FROM tokens")) > 0:
            config.SETUP_REQUIRED = False
        # ----- ------------------------------ -----

    @app.before_request
    def hook():
        # ----- ACCESS ROUTE PROTECTION -----
        # Only check for access if token is enabled
        # Check if token setup has been done
        if config.SETUP_REQUIRED:
            if request.endpoint not in ["access.setup", "static", None]:
                return redirect(url_for("access.setup"))
        else:
            # Don't want to allow access to setup when setup already done
            if request.endpoint == "access.setup":
                return redirect(url_for("access.login"))

            # Check if user has access
            if "access" not in session and request.endpoint not in ["access.login", "static", None]:
                return redirect(url_for("access.login"))
        # ----- ----------------------- -----

    # ----- ACCESS BLUEPRINT -----
    # Sorry you can't use the /access route :'(
    app.register_blueprint(access_bp, url_prefix="/access")
    # ----- ---------------- -----

# You can write your routes here!

@app.route("/")
def index():
    return render_template("index.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
