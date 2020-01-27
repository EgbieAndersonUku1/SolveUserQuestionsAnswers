from functools import wraps
from flask import url_for
from werkzeug.utils import redirect

from utils.session import Session


def login_required(f):
    @wraps(f)
    def login(*args, **kwargs):
        if Session.get_session_by_name("username") is None:
            return redirect(url_for("login_app.login"))
        return f(*args, **kwargs)
    return login


def is_user_already_logged_in(f):
    @wraps(f)
    def is_user_logged_in(*args, **kwargs):
        if Session.get_session_by_name("username"):
            return redirect(url_for("home_app.home"))
        return f(*args, **kwargs)
    return is_user_logged_in


def is_admin(f):
    @wraps(f)
    def admin(*args, **kwargs):
        if not Session.get_session_by_name("admin"):
            return redirect(url_for("home_app.home"))
        return f(*args, **kwargs)
    return admin