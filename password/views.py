from flask import render_template, request, flash, url_for, Blueprint
from werkzeug.utils import redirect

from utils.session import Session
from utils.sqlite3connector import sqlite3_connection
from utils.security import Password
from utils.decorators import login_required


password_app = Blueprint("password_app", __name__)


@password_app.route("/change/password", methods=["GET", "POST"])
@login_required
def change_password():

    username = Session.get_session_by_name("username")

    if request.method == "POST":
        if username:
            db = sqlite3_connection()
            current_password = db.get_one("SELECT password FROM users WHERE name =?", (username, ))

            if Password.check_password(current_password["password"], request.form["password"]):
                hashed_password = Password.hash_passwd(request.form["new_password"])
                db.execute_sql_cmd("""UPDATE users set password = ? WHERE name = ?""", (hashed_password, username))

                Session.clear_all()
                flash("Your password has been successfully changed. You may now login with the new password")
                db.close_connection()
                return redirect(url_for("login_app.login"))

            flash("The password you entered does not match the current password")
            db.close_connection()

    return render_template("password/new_password.html")

