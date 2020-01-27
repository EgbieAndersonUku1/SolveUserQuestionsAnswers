from flask import render_template, Blueprint
from utils.sqlite3connector import sqlite3_connection
from utils.decorators import is_admin

users_app = Blueprint("users_app", __name__)


@users_app.route("/users")
@is_admin
def users():

    db = sqlite3_connection()
    result = db.get_all("""SELECT id, name, expert, admin, logged_in FROM users""")
    db.close_connection()

    return render_template("/users/user_setup.html", result=result)