from flask_restplus import Resource
from measurements_bp import measurement_api
from config import Config
from functools import wraps
from werkzeug.exceptions import Forbidden
from flask import request
from measurements_bp.models import Measurement
from app import db
from schemas import GetRangeMeasurements
from marshmallow import ValidationError
from clients_bp.models import Client


@measurement_api.route("/get_range/<start_time>/<end_time>", methods=['GET'])
class Range(Resource):

    def get(start_time, end_time):
        db_data = db.session.query(Measurement).filter(Measurement.timestamp > start_time, Measurement.timestamp < end_time)
        if db_data == None :
            return {"ErrMsg" : "No enteries found"}

        data = {
            "data" : db_data,
            "start_time" : start_time,
            "end_time" : end_time,
            "count" : len(db_data)
        }

        dumped = GetRangeMeasurements().dump(data)

        return dumped