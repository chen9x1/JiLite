from flask import Blueprint, request
from .views import UdeployService
from .schemas import ProcessTriggerSchema, WorkflowTraceSchema, LogQuerySchema, ResponseSchema

udeploy_bp = Blueprint('udeploy', __name__)

@udeploy_bp.route('/trigger', methods=['POST'])
def trigger_process():
    data = ProcessTriggerSchema().load(request.json)
    result = UdeployService.run_process(data)
    return ResponseSchema().dump(result)

@udeploy_bp.route('/trace', methods=['GET'])
def get_workflow_trace():
    data = WorkflowTraceSchema().load(request.args)
    result = UdeployService.get_workflow_trace(data['request_id'])
    return ResponseSchema().dump(result)

@udeploy_bp.route('/logs', methods=['GET'])
def get_deployment_logs():
    data = LogQuerySchema().load(request.args)
    result = UdeployService.get_deployment_logs(data['log_path'])
    return ResponseSchema().dump(result)