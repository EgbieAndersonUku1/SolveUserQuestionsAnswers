from flask import session


class Session(object):

    @staticmethod
    def add(session_name, value):
        session[session_name] = value

    @staticmethod
    def remove_session_by_name(session_name):
        session.pop(session_name)

    @staticmethod
    def get_session_by_name(session_name):
        return session.get(session_name)

    @staticmethod
    def clear_all():
        session.clear()
