class Config(object):
    ENV_TYPE = None

    DEBUG = False
    FLASK_HOST = 'localhost'
    FLASK_PORT = 5000

    DB_NAME = None
    DB_USER = None
    DB_PASSWD = None
    DB_HOST = None
    DB_PORT = None

    AUTH_USERNAME = "username"
    AUTH_PASSWORD = "password"

    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SQLALCHEMY_DATABASE_URI=None
