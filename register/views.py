from flask import render_template, request, flash, url_for, Blueprint
from werkzeug.utils import redirect

from utils.date import get_current_date_now
from utils.sqlite3connector import sqlite3_connection
from utils.security import Password
from utils.decorators import is_user_already_logged_in, is_admin


register_app = Blueprint("register_app", __name__)


@register_app.route("/register", methods=["GET", "POST"])
@is_user_already_logged_in
def register():

    if request.method == "POST":

        db = sqlite3_connection()

        if _does_user_already_exist(db, username=request.form["register_name"]):
            flash("A user by the name already exists")
            db.close_connection()

        else:

            _add_registed_user_to_db_helper(db, request)
            flash("A new user by the name of {} has been created in the database".format(request.form["register_name"].upper()))

            return redirect(url_for('login_app.login'))

    return render_template("/register/register.html")


@register_app.route("/create/new/user", methods=["GET", "POST"])
@is_admin
def create_new_user():
    if request.method == "POST":

        db = sqlite3_connection()
        expert = 0
        username = request.form["register_name"]

        user = _does_user_already_exist(db, username=username)

        if not user:
            if request.form["select_id"].lower() == "expert":
                expert = 1

            _add_registed_user_to_db_helper(db, request, expert)
            return redirect(url_for("users_app.users"))
        flash("The user by the name of {} already exists".format(username))
    return render_template("register/register.html")


def _add_registed_user_to_db_helper(db, request, expert=0, admin=0):

    live, logged_in = 1, 0
    sql_query = """INSERT INTO users (name, password, expert, admin, joined_date,  live, logged_in)
                               VALUES (?, ?, ?, ?, ?, ?, ?)
                            """
    sql_values = (request.form["register_name"].lower(), Password.hash_passwd(request.form["register_password"]),
                  expert, admin, get_current_date_now(), live, logged_in)

    db.execute_sql_cmd(sql_query, sql_values)
    db.close_connection()


def _does_user_already_exist(db, username):

    user = db.get_one("""SELECT name FROM users WHERE name = ? """, (username,))

    if user:
        db.close_connection()
    return user
