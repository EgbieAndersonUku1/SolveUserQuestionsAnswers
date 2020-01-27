from utils.date import get_current_date_now
from utils.sqlite3connector import sqlite3_connection
from utils.security import Password


def create_test_users():

    joined_date = get_current_date_now()
    live, logged_in = 1, 0

    admin = """INSERT INTO users (name, password, expert, admin, joined_date, live, logged_in) 
               VALUES (?, ?, ?, ?, ?, ?, ?)
            """

    hashed_password = Password.hash_passwd("admin1234")
    admin_values = ("admin", hashed_password, 0, 1, joined_date, live, logged_in)

    expert = """INSERT INTO users (name, password, expert, admin, joined_date, live, logged_in) 
               VALUES (?, ?, ?, ?, ?, ?, ?)
            """
    hashed_password = Password.hash_passwd("expert1234")
    expert_values = ("expertuser", hashed_password, 1, 0, joined_date, live, logged_in)

    db = sqlite3_connection()
    db.execute_sql_cmd(admin, admin_values)

    db.execute_sql_cmd(expert, expert_values)
    db.close_connection()


if __name__ == "__main__":
    create_test_users()
