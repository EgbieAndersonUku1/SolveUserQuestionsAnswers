from sqlite3 import connect as sqlite3_connect
from sqlite3 import Error, IntegrityError
from sqlite3 import Row


_ERROR_MSG = "Attempted to add the values <{}> but failed because it was not in a tuple format"


class SQLite3Connect(object):
    """SQLite3Connect class allows the user of the class to be able to
       create or close the connection between an existing database in the database.

       It also allows the user to add and retrieve one or more aspects of data from
       the table or tables providing those tables have already been created.
    """

    def __init__(self, db_file_name):
        self._db_file_name = db_file_name
        self._conn = None

    def create_connection(self):
        """create_connection(str) -> return sqlite connection

           Creates a database connection to the SQLite database

           :return
                Returns either a connection object or None
        """

        try:
            self._conn = sqlite3_connect(self._db_file_name)
            self._conn.row_factory = Row # returns the data as a dictionary instead of tuples
        except Error as e:
            raise e

    def create_table(self, create_table_sql):
        """ create a table from the create_table_sql statement

            :param conn: Connection object
            :param create_table_sql: a CREATE TABLE statement

        """

        try:
            conn = self._conn.cursor()
            conn.execute(create_table_sql)
        except Error as e:
            raise e

    def execute_sql_cmd(self, sql_query, sql_values):
        """insert(str, tuple) -> returns None

           Takes two parameters a sql statement and sql_values
           and executes those values

           :parameter
                sql_query (str): The sql insert query command need to execute the command
                sql_values (tuple): Any values need to execute the command
        """

        try:
            self._conn.execute(sql_query, sql_values)
        except IntegrityError:
            pass
        else:
            self._conn.commit()

    def get_all(self, sql_query, values=None):
        """get_all(str, str default value None) returns SQLite3 object

           Takes an sqlite3 select statement and any values (default None)
           and retrieves all values pertaining to that command.

           :parameter
                sql_query (str): The sql commands need to retrieve the data.
                                 Warning returns all data not one.
                values (None or tuple): The retrieved value will be filtered based
                                        on the value parameter. If no value is added
                                        then it will return all values associated
                                        with the sql command given. If the value is not none
                                        then the returned data will be filtered based on the
                                        parameter value.
        """

        if values:
            assert type(values) == tuple, _ERROR_MSG.format(values)
            cur = self._conn.execute(sql_query, values)
        else:
            cur = self._conn.execute(sql_query)
        return cur.fetchall()

    def get_one(self, sql_query, sql_values=None):
        """"""
        if sql_values:
            assert type(sql_values) == tuple, _ERROR_MSG.format(sql_values)

            cur = self._conn.execute(sql_query, sql_values)
        else:
            cur = self._conn.execute(sql_query)

        return cur.fetchone()

    def close_connection(self):
        """Close the connection"""
        self._conn.close()