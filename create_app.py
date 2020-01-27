from flask import Flask


app = Flask(__name__)


def create_app():

    app.config.from_pyfile("settings.py")


    #import
    from home.views import home_app
    from password.views import password_app
    from register.views import register_app
    from login.views import login_app
    from search.views import search_app
    from users.views import users_app
    from admin.views import admin_app
    from questions.views import question_app
    from logout.views import logout_app

    # register the app
    app.register_blueprint(home_app)
    app.register_blueprint(password_app)
    app.register_blueprint(register_app)
    app.register_blueprint(login_app)
    app.register_blueprint(search_app)
    app.register_blueprint(users_app)
    app.register_blueprint(admin_app)
    app.register_blueprint(question_app)
    app.register_blueprint(logout_app)

    return app