
from flask_restplus import Resource
from measurements_bp import measurement_api
from config import Config
from functools import wraps
from werkzeug.exceptions import Forbidden
from flask import request,Response
from measurements_bp.models import Measurement
from app import db
from schemas import CreateMeasurements,GetMeasurements
from marshmallow import ValidationError
from clients_bp.models import Client
   

@measurement_api.route("/getCSV", methods=['GET'])
class CSVGetter(Resource):
    
    def get(self):
        def generate():

            msr_data = db.session.query(Measurement).all()
            for msr in msr_data:
                yield ','.join([msr.id,msr.air_quality,msr.humidity,msr.temperature,msr.timestamp]) + "\n"
        return Response(generate(),mimetype='text/csv')
