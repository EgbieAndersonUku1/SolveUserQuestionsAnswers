from flask import url_for, Blueprint
from werkzeug.utils import redirect

from utils.session import Session
from utils.sqlite3connector import sqlite3_connection
from utils.decorators import login_required


logout_app = Blueprint("logout_app", __name__)


@logout_app.route("/logout")
@login_required
def logout():
    db = sqlite3_connection()

    db.execute_sql_cmd("""UPDATE users SET logged_in = 0 WHERE name = ?""", (Session.get_session_by_name("username"),))

    db.close_connection()
    Session.clear_all()
    return redirect(url_for("home_app.home"))
