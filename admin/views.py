from flask import flash, url_for, Blueprint
from werkzeug.utils import redirect

from utils.sqlite3connector import sqlite3_connection
from utils.decorators import is_admin


admin_app = Blueprint("admin_app", __name__)


@admin_app.route("/deactivate/<user_id>")
@is_admin
def change_account_status(user_id):
    """change_account_status(str) -> redirects

       Takes a user ID and de-activates or activate the user's account.
       If the account is active then this method will de-activate the account
       otherwise will activate the account.
    """
    db = sqlite3_connection()

    account_status = db.get_one("""SELECT live FROM users WHERE id = ?""", (user_id, ))

    if account_status["live"]:
        db.execute_sql_cmd("UPDATE users set live = 0 WHERE id = ?", (user_id, ))
    else:
        db.execute_sql_cmd("UPDATE users set live = 1 WHERE id = ?", (user_id,))
    db.close_connection()

    return redirect(url_for('search_app.search', user_id=user_id))


@admin_app.route("/promote/<user_id>/<username>", methods=["GET", "POST"])
@is_admin
def promote(user_id, username):
    """promote(str, str) -> return redirect template

       Takes a user id and username and promotes the user to either an
       expert user or de-promotes the user to a regular user.
    """
    db = sqlite3_connection()
    user = db.get_one("""SELECT id, expert FROM users WHERE id = ?""", (user_id, ))

    if not user["expert"]:
        _promote_user_helper(db, user_id, to_expert=True)
        flash_msg = "The user {} has been promoted to expert".format(username.upper())
    else:
        _promote_user_helper(db, user_id)
        flash_msg = "The user {} has been de-promoted to a regular user".format(username.upper())
    db.close_connection()

    flash(flash_msg)
    return redirect(url_for("users_app.users"))


def _promote_user_helper(db, user_id, to_expert=False):
    """A helper function that adds additional help to promote function"""

    if to_expert:
        db.execute_sql_cmd("""UPDATE users SET expert = 1 WHERE id = ?""", (user_id, ))
    else:
        db.execute_sql_cmd("""UPDATE users SET expert = 0  WHERE id = ?""", (user_id,))

    return True

