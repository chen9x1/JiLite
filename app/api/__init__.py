from flask import Blueprint

api_bp = Blueprint('api', __name__)

from app.api.autosys import autosys_bp
from app.api.udeploy.routes import udeploy_bp
api_bp.register_blueprint(autosys_bp, url_prefix='/autosys')
api_bp.register_blueprint(udeploy_bp, url_prefix='/udeploy')