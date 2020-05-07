from flask import Blueprint
from flask_restplus import Api
from marshmallow import ValidationError


measurement_bp = Blueprint("measurement", __name__, url_prefix="/measurement")
measurement_api = Api(measurement_bp)

@measurement_api.errorhandler(ValidationError)
def _handle_api_error(ex):
    return "greska"

from measurements_bp.api import *