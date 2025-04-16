from marshmallow import Schema, fields, validate

class ProcessTriggerSchema(Schema):
    process_name = fields.String(required=True)
    environment = fields.String(required=True)
    parameters = fields.Dict()

class WorkflowTraceSchema(Schema):
    request_id = fields.String(required=True)

class LogQuerySchema(Schema):
    log_path = fields.String(required=True)

class ResponseSchema(Schema):
    code = fields.Integer()
    data = fields.Raw()
    message = fields.String()