from schemas import Schema
from schemas import fields

class GetMeasurements(Schema):
    id = fields.Integer(required = True)
    air_quality = fields.Float(required = True)
    humidity = fields.Float(required = True)
    temperature = fields.Float(required = True)
