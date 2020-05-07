import os
from config import Config


class Production(Config):
    """ The class whose fields act as configuration production environment constants """
    ENV_TYPE = "Production"

    DB_NAME = "d2d2gbsp5g7kel"
    DB_USER = "kndndqqqfvrvnt"
    DB_PASSWD = "50805cc707b0380d7f2a1cd14197131449287821531f412fccb06d2af30da5e8"
    DB_HOST = "ec2-54-247-170-5.eu-west-1.compute.amazonaws.com"
    DB_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{DB_USER}:{DB_PASSWD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'