from flask import jsonify
from app.api.autosys import autosys_bp
from app.api.autosys.views import AutosysService

@autosys_bp.route('/jobs', methods=['GET'])
def get_all_jobs():
    """Get all Autosys jobs."""
    response = AutosysService.get_all_jobs()
    return jsonify(response), 200

@autosys_bp.route('/jobs/<job_name>', methods=['GET'])
def get_job_by_name(job_name):
    """Get a specific Autosys job by name."""
    response = AutosysService.get_job_by_name(job_name)
    return jsonify(response), 200
