from werkzeug.security import generate_password_hash, check_password_hash


class Password(object):

    @staticmethod
    def hash_passwd(password, hash_method="sha256"):
        """hash_passwd(str, str) -> hashed str"""

        return generate_password_hash(password, hash_method)

    @staticmethod
    def check_password(hashed_password, password):
        """check_password(str, str) -> return Boolean"""
        return check_password_hash(hashed_password, password)