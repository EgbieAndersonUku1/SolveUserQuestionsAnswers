from os import getcwd
from os.path import join

from utils.database import SQLite3Connect


def main():
    """Creates all the table in the database"""

    db = SQLite3Connect(db_file_name=join(getcwd(), "question.db"))
    db.create_connection()

    user_table = """CREATE TABLE users (
                        id integer primary key autoincrement,
                        name text not null,
                        password text not null,
                        expert boolean not null,
                        admin boolean not null,
                        joined_date date not null,
                        live boolean not null,
                        logged_in boolean not null
                );"""

    questions_table = """CREATE TABLE questions (
                            id integer primary key autoincrement,
                            question text not null,
                            answer text,
                            asked_by_id integer not null,
                            expert_id integer not null
                         );
                      
                      """

    #db._conn.execute("DROP TABLE users;")
    #db._conn.execute("DROP TABLE questions;")
    db.create_table(user_table)
    db.create_table(questions_table)
    db.close_connection()

if __name__ == "__main__":
    main()