from os import getcwd
from os.path import join

from utils.database import SQLite3Connect


def sqlite3_connection():
    db = SQLite3Connect(db_file_name=join(getcwd(), "question.db"))
    db.create_connection()
    return db