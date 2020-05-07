from schemas import Schema
from schemas import fields
from schemas import get_measurements_schema

class GetRangeMeasurements(Schema):
    data = fields.Nested(get_measurements_schema, required = True, many = True)
    start_time = fields.DateTime(required = True)
    end_time = fields.DateTime(required = True)
    count = fields.Integer(required = True)
