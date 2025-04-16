from marshmallow import Schema, fields

class AutosysJobSchema(Schema):
    """Schema for serializing AutosysJob objects."""
    job_name = fields.Str(required=True)
    job_type = fields.Str(required=True)
    owner = fields.Str(allow_none=True)
    machine = fields.Str(allow_none=True)
    condition = fields.Str(allow_none=True)
    box_name = fields.Str(allow_none=True)
    attributes = fields.Dict(keys=fields.Str(), values=fields.Raw(), allow_none=True)

class ResponseSchema(Schema):
    """Schema for API responses."""
    data = fields.Raw(allow_none=True)
    message = fields.Str(allow_none=True)
    code = fields.Int(required=True)