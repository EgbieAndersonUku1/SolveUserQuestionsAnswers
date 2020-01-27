from flask import render_template, request, Blueprint

from utils.date import prettify_date
from utils.sqlite3connector import sqlite3_connection
from utils.decorators import is_admin

search_app = Blueprint("search_app", __name__)


@search_app.route("/search", methods=["GET", "POST"])
@search_app.route("/search/<user_id>")
@is_admin
def search(user_id=None):

    user = None

    db = sqlite3_connection()

    if request.method == "POST":

        if not user_id:
            user = db.get_one("""SELECT * FROM users WHERE name = ?""", (request.form["search"], ))
    if user_id:
        user = db.get_one("""SELECT * FROM users WHERE id = ?""", (user_id,))
    return render_template("search/search.html", user=user, prettify_date=prettify_date)
