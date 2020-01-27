from flask import render_template, request, flash, url_for, Blueprint
from werkzeug.utils import redirect

from utils.session import Session
from utils.sqlite3connector import sqlite3_connection
from utils.security import Password
from utils.decorators import is_user_already_logged_in

login_app = Blueprint("login_app", __name__)


@login_app.route("/login", methods=["GET", "POST"])
@is_user_already_logged_in
def login():

    if request.method == "POST":

        db = sqlite3_connection()
        name, password = request.form["name"].lower(), request.form["password"]

        sql_query = "SELECT id, name, password, expert, admin, live FROM users WHERE name = ?"

        result = db.get_one(sql_query, sql_values=(name,))

        if result["live"]:
            db.execute_sql_cmd("""UPDATE users SET logged_in = 1 WHERE name = ?""", (name,))
            db.close_connection()

            if result and Password.check_password(result["password"], password):
                Session.add("username", result["name"])
                Session.add("admin", result["admin"])
                Session.add("expert", result["expert"])
                Session.add("id", result["id"])
                return redirect(url_for("home_app.home"))
            flash("Incorrect user and password")
        else:
            flash("Your account has been de-activated")
    return render_template("/login/login.html")
