from schemas import Schema
from schemas import fields

class CreateMeasurements(Schema):
    air_quality = fields.Float(required = True)
    humidity = fields.Float(required = True)
    temperature = fields.Float(required = True)