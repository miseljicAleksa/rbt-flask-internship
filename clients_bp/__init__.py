from flask import Blueprint
from flask_restplus import Api

client_bp = Blueprint("client", __name__, url_prefix="/register")
client_api = Api(client_bp)

from clients_bp.api import *