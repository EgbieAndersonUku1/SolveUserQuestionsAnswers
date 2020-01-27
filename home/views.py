from flask import render_template, Blueprint

home_app = Blueprint("home_app", __name__)

from utils.sqlite3connector import sqlite3_connection


@home_app.route("/")
@home_app.route("/home")
def home():

    db = sqlite3_connection()
    questions = db.get_all("""SELECT questions.id AS question_id, questions.question, askers.name AS asker_name, 
                              experts.name AS expert_name
                              FROM questions JOIN users AS askers ON askers.id = questions.asked_by_id
                              JOIN users AS experts ON experts.id = questions.expert_id
                              WHERE questions.answer IS NOT NULL
                           """)

    return render_template("/home/home.html", questions=questions)
