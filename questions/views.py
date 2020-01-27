from flask import render_template, request, url_for, Blueprint
from werkzeug.utils import redirect

from utils.session import Session
from utils.sqlite3connector import sqlite3_connection
from utils.decorators import login_required


question_app = Blueprint("question_app", __name__)


@question_app.route("/question/<question_id>")
@login_required
def get_question(question_id):

    db = sqlite3_connection()
    question = db.get_one("""SELECT questions.question, questions.answer, askers.name AS asker_name, 
                                  experts.name AS expert_name
                                  FROM questions JOIN users AS askers ON askers.id = questions.asked_by_id
                                  JOIN users AS experts ON experts.id = questions.expert_id
                                  WHERE questions.id = ?
                               """, (question_id,))
    db.close_connection()
    return render_template("/questions/question.html", question=question)


@question_app.route("/question/ask", methods=["GET", "POST"])
@login_required
def ask_question():

    db = sqlite3_connection()

    if request.method == "POST":
        values = (request.form["question"], Session.get_session_by_name("id"), request.form["expert"])
        db.execute_sql_cmd("INSERT into questions (question, asked_by_id, expert_id) VALUES (?, ?, ?)", values)
        return redirect(url_for("home_app.home"))
    experts_list = db.get_all("""SELECT id, name FROM users WHERE expert = 1""")
    return render_template("questions/ask.html", experts_list=experts_list)


@question_app.route("/question/answered/<question_id>", methods=["GET", "POST"])
@login_required
def get_answer(question_id):

    db = sqlite3_connection()

    if request.method == "POST":
        db.execute_sql_cmd("UPDATE questions SET answer = ?  WHERE id = ?", (request.form["answer"], question_id))
        return redirect(url_for('question_app.unanswered_list_of_questions'))

    question = db.get_one("SELECT question FROM questions WHERE id = ?", (question_id, ))
    return render_template("/answers/answer.html", question=question, question_id=question_id)


@question_app.route("/question/unanswered")
@login_required
def unanswered_list_of_questions():

    sql_query = """SELECT questions.id, questions.question, users.name FROM questions JOIN users 
                   ON users.id = questions.asked_by_id WHERE questions.answer is null and questions.expert_id = ?
                """
    db = sqlite3_connection()
    questions = db.get_all(sql_query, (Session.get_session_by_name("id"), ))

    return render_template("/answers/unanswered.html", questions=questions)




